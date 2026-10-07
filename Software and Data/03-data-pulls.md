# NEFSC HabCam & AUV Data Query Pipeline

This pipeline extracts, cleans, and structures image annotations and associated telemetry metadata for NEFSC HabCam (V4, V3) and Tethys-Class LRAUV (*Stella* and *Polaris*) surveys from the NEFSC Oracle database (`ORAPROD`, `HABCAM` schema). The workflow filters out unusable images, applies environmental quality thresholds, isolates target taxa (such as live sea scallops or specific fish/invertebrate phyla), and generates standardized outputs for species analyses.

---

## 1. HABCAM Database Architecture & Reference Tables

### 1.1 Relational Table Architecture
The enterprise Oracle database (`ORAPROD.HABCAM`) consists of core relational tables used for tracking cruise assignments, image metadata, and species annotations.

| Table Name | Years Available | Description & Usage Notes |
| :--- | :--- | :--- |
| `HABCAM_ANNOTATIONS` | 2009 – Present | Master image annotation records. Includes manual, AI, and Research Set-Aside (RSA) records. |
| `HABCAM_ASSIGNMENTS` | 2012 – Present | Web annotator assignment records and project goals (information incomplete prior to 2018). |
| `HABCAM_CLASSES` | 2012 – Present | Species names and class ID lookup table (mapped via `SpeciesList_V6.csv`). |
| `HABCAM_DATA_IDENTIFIER` | 2012 – Present | Defines gear, purpose, and QA/QC status codes for query filtering. |
| `HABCAM_ID_MODES` | 2012 – Present | Target species lists enabled for specific annotation assignments. |
| `HABCAM_IMAGE_LIST` | 2012 – Present | Image manifest lists assigned per annotation assignment. |
| `HABCAM_IMAGE_METADATA` | 2012 – Present | Vehicle telemetry and sensor metadata for NEFSC HabCam V4. |
| `HABCAM_IMAGE_METADATA_LRAUV` | 2024 – Present | Vehicle telemetry and sensor metadata for NEFSC Tethys LRAUVs (*Stella* / *Polaris*). |
| `HABCAM_IMAGE_METADATA_V3` | 2017 | Image metadata for CFF HabCam V3 surveys (contains no annotations). |

---

### 1.2 Data Identifier Reference Table (`DATA_IDENTIFIER`)
The `DATA_IDENTIFIER` attribute is the primary quality-control filter used when querying HabCam and AUV records.

| `DATA_IDENTIFIER` | Operational Category & Assessment Status | Description & Usage Notes |
| :-: | :--- | :--- |
| **`1.0`** | **NEFSC V4 Assessment (QA/QCed)** | Official HabCam V4 survey data used in scallop stock assessments; fully QA/QCed since 2019. |
| **`1.1`** | **NEFSC V4 Invalid / Excluded** | Data NOT used and should not be used in scallop assessments. |
| **`1.2`** | **NEFSC V4 Assessment Usable (QA/QCed)** | Supplemental survey data cleared for assessment use. |
| **`1.3`** | **NEFSC V4 Assessment Usable (Pending QA/QC)** | Valid survey data pending final QA/QC sign-off; use with caution. |
| **`2.0`** | **Annotator Training** | Internal training assignments used for onboarding annotators. |
| **`3.0`** | **Vehicle Calibration** | Vehicle, optical, or sensor calibration runs. |
| **`4.0` – `4.2`** | **Special Projects** | Special research projects (`4.1` = 2022 Hollings Sand Dollar project; `4.2` = 2018 Testset selection). |
| **`5.0`** | **Unknown / Unverified** | Unverified annotation data (most likely wrong assignment numbers). |
| **`6.0`** | **Historical RSA (No Metadata)** | Historical RSA annotations (2009, 2011, 2012) without image metadata. |
| **`6.1`** | **RSA CFF V3 (2016)** | RSA CFF HabCam V3 2016 annotation data used in scallop assessments (no metadata). |
| **`6.2` – `6.4`** | **RSA Richard Taylor V2** | Historical V2 RSA annotation data (2012, 2014). |
| **`7.0`** | **NEFSC LRAUV Assessment Data (QA/QCed)** | Official LRAUV AUV survey data cleared and QA/QCed for stock assessment use. |
| **`7.1` – `7.3`** | **NEFSC LRAUV Secondary / Pending** | LRAUV AUV datasets categorized by assessment usability and QA/QC status (`7.3` pending QA/QC). |

---

## 2. Setup & Pipeline Prerequisites

### 2.1 Required R Packages
Ensure the following R libraries are installed and loaded prior to executing the pipeline:

```r
install.packages(c("tidyverse", "dbplyr", "DBI", "ROracle", "stringr", "tictoc", "arrow"))
```

```r
library(DBI)
library(ROracle)
library(dplyr)
library(dbplyr)
library(stringr)
```

---

### 2.2 Configure Query Parameters
Set the Oracle connection credentials, target survey year, taxonomic target, vehicle gear type, altitude cutoffs, and output preferences in the parameter block:

```r
# 1. Oracle Credentials
ora_username <- "your_oracle_username"
ora_password <- "your_oracle_password"
tns_alias    <- "NEFSC_pw_oraprod"

# 2. Target Year & Species Query Mode
year <- 2024  # Target survey year (some years include multiple cruises)
using_what_to_query <- c("class_id_list", "class_phylum_list")[2]

# Option A: Query by specific numeric class_ids
class_id_list <- c(258, 268)

# Option B: Query by broader taxonomic phylum/category
# Note: "Live Scallop" must be queried independently on its own
class_phylum_list <- c("Live Scallop", "Scallop", "Fish", "Roundfish")[3:4]

# Available phylum options in SpeciesList_V6.csv:
# "Live Scallop", "Scallop", "Fish", "Roundfish", "Flatfish", "Skate", "Algae", 
# "Proteobacteria", "Chordata - Tunicate", "Invertebrate", "Invertebrate - Echinodermata", 
# "Invertebrate - Crustacean", "Invertebrate - Cnidaria", "Invertebrate - Mollusca", 
# "Invertebrate - Annelida", "Invertebrate - Porifera", "Invertebrate - Brachiopoda", 
# "Invertebrate - Bryozoa", "Invertebrate - Ctenophora", "Invertebrate - Chelicerata", 
# "Substrate", "Message", "Misc", "Man-made Object"

# 3. Vehicle Gear & Environmental Cutoffs
gear <- c("Habcam-V4", "AUV", "Habcam-V3")[1]

# Match DATA_IDENTIFIER list to selected gear:
# HabCam: c(1, 1.2, 1.3) | AUV: c(7, 7.2, 7.3)
data_identifier_list <- list(
  Habcam = c(1, 1.2, 1.3),
  AUV    = c(7, 7.2, 7.3)
)[[1]]

# Altitude Cutoff (m): <= 2.5m for HabCam V4; >= 3.0m for AUV (flies ~2.6m)
alt_cutoff <- 2.5

# 4. Input & Output Configuration
species_list <- read.csv("SpeciesList_V6.csv")
output_dir   <- "C:/Users/jui-han.chang/Desktop/"
target_label <- "live_scallop"
output_name  <- paste0(gear, "_", year, "_", target_label)
output_type  <- c("rds", "csv")[1]
```

---

## 3. Oracle Database Queries

### 3.1 Open Oracle Connection
Connects to the NEFSC Oracle database instance using `ROracle` and `DBI`:

```r
connec <- tryCatch({
  conn <- dbConnect(
    DBI::dbDriver("Oracle"),
    username = ora_username,
    password = ora_password,
    dbname   = tns_alias
  )
  print("Database connected successfully!")
  conn
}, error = function(e) {
  message("Unable to connect to database.")
  message(paste("Error details:", e$message))
  return(NULL)
})
```

---

### 3.2 Execute Database Queries
Extracts cruise metadata, data identifiers, image telemetry, and annotations. Applies environmental and operational filters directly within the lazy query before downloading data to local memory (`collect()`):

```r
if (is.null(connec)) {
  stop("Script halted: Could not connect to the database.")
} else {
  # 1. Query Master Cruise Details for target year
  cruise_id <- dbGetQuery(
    connec,
    paste0("
      SELECT
        a.CRUISE6 AS CRUISE_ID,
        a.YEAR,
        b.SEASON,
        b.STARTDATE,
        b.ENDDATE,
        d.PURPOSE,
        c.VESSEL_NAME,
        e.GEAR_DEFINITION
      FROM SVDBS.MASTER_CRUISE_DETAILS a
      INNER JOIN SVDBS.MASTER_CRUISE_TABLE b
        ON a.SVVESSEL = b.SVVESSEL AND a.VESSEL_NUM = b.VESSEL_NUM AND a.YEAR = b.YEAR AND a.PURPOSE_CODE = b.PURPOSE_CODE
      INNER JOIN SVDBS.SV_VESSEL c ON a.SVVESSEL = c.VESSEL_ABBREV
      INNER JOIN SVDBS.SVCRUISE_PURPOSE d ON a.PURPOSE_CODE = d.PURPOSE_CODE
      INNER JOIN SVDBS.SVGEAR e ON b.SVGEAR = e.SVGEAR
      WHERE (UPPER(e.GEAR_DEFINITION) LIKE '%HABCAM%' OR UPPER(e.GEAR_DEFINITION) LIKE '%AUV%')
        AND a.YEAR = ", year, "
      ORDER BY CRUISE_ID"
    )
  )

  # 2. Query Data Identifier Reference Table
  data_identifier <- dbGetQuery(connec, "SELECT * FROM HABCAM.HABCAM_DATA_IDENTIFIER")

  # 3. Lazy Connection to Annotation & Metadata Tables
  ann_memory <- tbl(connec, in_schema("HABCAM", "HABCAM_ANNOTATIONS"))

  if (gear == "Habcam-V4") {
    img_memory <- tbl(connec, in_schema("HABCAM", "HABCAM_IMAGE_METADATA"))
  } else if (gear == "AUV") {
    img_memory <- tbl(connec, in_schema("HABCAM", "HABCAM_IMAGE_METADATA_LRAUV"))
  } else if (gear == "Habcam-V3") {
    img_memory <- tbl(connec, in_schema("HABCAM", "HABCAM_IMAGE_METADATA_V3"))
  } else {
    stop("Invalid gear selected.")
  }

  # 4. Filter Image Metadata (Lazy Query)
  img_lazy <- img_memory |>
    filter(CRUISE_ID %like% paste0(!!year, "%")) |>
    filter(ALTIMETER_ALTITUDE_METER <= !!alt_cutoff) |>
    filter(FIELD_OF_VIEW_SQ_METER > 0) |>
    filter(SHIP_LATITUDE > 0) |>
    filter(SHIP_LONGITUDE >= -180) |>
    filter(CTD_VEHICLE_DEPTH_METER > 5) |>
    filter(abs(VEHICLE_PITCH_ANGLE) < 15) |>
    filter(abs(VEHICLE_ROLL_ANGLE) < 15)

  # 5. Join Annotations to Filtered Image Telemetry & Download
  start_time <- Sys.time()
  ann <- ann_memory |>
    filter(CRUISE_ID %like% paste0(!!year, "%")) |>
    filter(DATA_IDENTIFIER %in% !!data_identifier_list) |>
    filter(ANNOTATION_DEPRECATED == 0) |>
    select(
      CRUISE_ID, DATA_IDENTIFIER, ASSIGNMENT_ID, IMAGE_NAME,
      ANNOTATION_TIMESTAMP, ANNOTATOR_USER_ID, GEOMETRY_TEXT, CLASS_ID
    ) |>
    mutate(GEOMETRY_TEXT = sql("CAST(GEOMETRY_TEXT AS VARCHAR2(4000))")) |>
    inner_join(img_lazy, by = c("IMAGE_NAME", "CRUISE_ID")) |>
    select(-HABCAM_PK) |>
    arrange(desc(IMAGE_NAME)) |>
    collect()
  end_time <- Sys.time()
  print(paste0("Finished annotation query. Downloaded ", nrow(ann), " rows."))

  # 6. Download Full Filtered Image Metadata
  start_time <- Sys.time()
  img <- img_lazy |>
    select(-HABCAM_PK) |>
    arrange(desc(IMAGE_NAME)) |>
    collect()
  end_time <- Sys.time()
  print(paste0("Finished image metadata query. Downloaded ", nrow(img), " rows."))

  # 7. Close Database Connection
  DBI::dbDisconnect(connec)
  print("Finished all queries; Oracle database connection closed successfully.")
}
```

---

## 4. Data Cleaning & Unusable Image Filtering

Images flagged as `"unusable"` during annotation (due to turbidity, dark frames, or deck frames) and all annotations associated with those images must be removed prior to analysis.

```r
# Join downloaded annotations with master species list
ann <- ann |>
  left_join(species_list, by = "CLASS_ID")

# Calculate summary of total vs. unusable image and annotation counts
dashboard_ann_summary <- tibble(
  Category = c("Images", "Annotations"),
  Total    = c(n_distinct(ann$IMAGE_NAME), nrow(ann)),
  Unusable = c(
    n_distinct(ann$IMAGE_NAME[ann$CLASS_NAME == "unusable"]),
    sum(ann$IMAGE_NAME %in% ann$IMAGE_NAME[ann$CLASS_NAME == "unusable"])
  ),
  Usable   = Total - Unusable
)

knitr::kable(dashboard_ann_summary)

# Extract list of unusable image names and filter them out
images_to_remove <- ann |>
  filter(CLASS_NAME == "unusable") |>
  distinct(IMAGE_NAME)

ann_usable <- ann |>
  anti_join(images_to_remove, by = "IMAGE_NAME")

# Verify that usable counts match expected totals
dashboard_ann_summary |>
  mutate(
    ann_usable = c(n_distinct(ann_usable$IMAGE_NAME), nrow(ann_usable)),
    Match      = (Usable == ann_usable)
  ) |>
  knitr::kable()
```

---

## 5. Target Species Isolation Pipelines

The pipeline branches into two specialized processing tracks depending on whether the query targets **Live Sea Scallops** or **Other Taxonomic Groups**.

### 5.1 Track A: Live Sea Scallop Pipeline
Isolates live sea scallops, removes clappers/dead shell counts, and builds a zero-count image manifest (`ann_scallop_zero`) containing one record per usable image where no live scallops were observed.

```r
# 1. Filter all scallop annotations
ann_scallop <- ann_usable |>
  filter(CLASS_CATEGORY_PHYLUM == "Scallop")

# 2. Exclude dead/clapper classes
ann_scallop_live <- ann_scallop |>
  filter(!str_detect(CLASS_NAME, regex("clapper|dead", ignore_case = TRUE)))

# 3. Create zero-count image manifest (one row per image with no live scallops)
ann_scallop_zero <- ann_usable |>
  anti_join(ann_scallop_live, by = "IMAGE_NAME") |>
  distinct(IMAGE_NAME, .keep_all = TRUE) |>
  mutate(
    GEOMETRY_TEXT         = NA,
    CLASS_ID              = 1102,
    CLASS_NAME            = "Sediment Unassessed",
    CLASS_CATEGORY_PHYLUM = "Substrate"
  )

# 4. Verify that live_images + zero_images = total_usable_images
dashboard_ann_summary |>
  mutate(
    ann_scallop_live           = c(n_distinct(ann_scallop_live$IMAGE_NAME), nrow(ann_scallop_live)),
    ann_scallop_zero           = c(n_distinct(ann_scallop_zero$IMAGE_NAME), NA),
    ann_scallop_live_plus_zero = ann_scallop_live + ann_scallop_zero,
    Match                      = (Usable == ann_scallop_live_plus_zero)
  ) |>
  knitr::kable()

# 5. Compile output list
output_list <- list(
  cruise     = cruise_id,
  identifier = data_identifier,
  usable     = ann_usable,
  live       = ann_scallop_live,
  zero       = ann_scallop_zero,
  img        = img
)
```

---

### 5.2 Track B: Other Species Pipeline
Isolates target fish or invertebrate species (via `class_id_list` or `class_phylum_list`) and constructs a corresponding zero-count image manifest.

```r
# 1. Filter target species annotations by Class ID or Phylum
if (using_what_to_query == "class_id_list") {
  ann_species <- ann_usable |>
    filter(CLASS_ID %in% class_id_list)
} else {
  ann_species <- ann_usable |>
    filter(CLASS_CATEGORY_PHYLUM %in% class_phylum_list)
}

# 2. Create zero-count image manifest
ann_species_zero <- ann_usable |>
  anti_join(ann_species, by = "IMAGE_NAME") |>
  distinct(IMAGE_NAME, .keep_all = TRUE) |>
  mutate(
    GEOMETRY_TEXT         = NA,
    CLASS_ID              = 1102,
    CLASS_NAME            = "Sediment Unassessed",
    CLASS_CATEGORY_PHYLUM = "Substrate"
  )

# 3. Verify image count alignment
dashboard_ann_summary |>
  mutate(
    ann_species           = c(n_distinct(ann_species$IMAGE_NAME), nrow(ann_species)),
    ann_species_zero       = c(n_distinct(ann_species_zero$IMAGE_NAME), NA),
    ann_species_plus_zero = ann_species + ann_species_zero,
    Match                 = (Usable == ann_species_plus_zero)
  ) |>
  knitr::kable()

# 4. Compile output list
output_list <- list(
  cruise     = cruise_id,
  identifier = data_identifier,
  usable     = ann_usable,
  species    = ann_species,
  zero       = ann_species_zero,
  img        = img
)
```

---

## 6. Output File Structure & Export

### 6.1 Pipeline Output Definitions
The pipeline generates structured R list objects (`output_list`) or exported `.csv` files.

| Output Element | Description & Contents |
| :--- | :--- |
| **`cruise`** | Summary table of active cruise IDs, season, operational dates, vessel, and gear definitions. |
| **`identifier`** | Reference table of `HABCAM_DATA_IDENTIFIER` descriptions used in the query. |
| **`img`** | Telemetry and metadata for all collected images meeting core environmental criteria. |
| **`ann`** | Raw annotations matching image filtering criteria, joined with class names and phyla. |
| **`usable` / `ann_usable`** | Primary dataset of all annotations associated strictly with usable images. |
| **`live` / `ann_scallop_live`** | Live sea scallop annotations on usable images (excluding clappers and dead shells). |
| **`species` / `ann_species`** | Target species annotations on usable images for requested Class IDs or Phyla. |
| **`zero` (`ann_scallop_zero` / `ann_species_zero`)** | Manifest of usable images containing zero target species (one record per zero-count image). |

---

### 6.2 Export Output Code
Saves finalized pipeline outputs as serialized `.rds` workspace files or flat `.csv` spreadsheets:

```r
if (output_type == "rds") {
  saveRDS(
    output_list, 
    file = file.path(output_dir, paste0(output_name, ".", output_type))
  )
}

if (output_type == "csv") {
  if ("Live Scallop" %in% class_phylum_list) {
    write_csv(
      ann_scallop_live, 
      file = file.path(output_dir, paste0(output_name, "_ann_live.", output_type))
    )
    write_csv(
      ann_scallop_zero, 
      file = file.path(output_dir, paste0(output_name, "_ann_zero.", output_type))
    )
  } else {
    write_csv(
      ann_species, 
      file = file.path(output_dir, paste0(output_name, "_ann_species.", output_type))
    )
    write_csv(
      ann_species_zero, 
      file = file.path(output_dir, paste0(output_name, "_ann_zero.", output_type))
    )
  }
}
```



