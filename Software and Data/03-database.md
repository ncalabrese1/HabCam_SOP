# Database Architecture & Operations

## 1. Archiving and Data Processing Workflow

### Database Archiving
* **Realtime Image Check:** During realtime processing, the HabCam software periodically checks for newly created `.img` files.
* **Write Verification Buffer:** To ensure a file is fully written before processing, the software never archives the newest `.img` file immediately; it waits until the subsequent `.img` file is created (e.g., `20250110_2010.img` is not archived until `20250110_2020.img` exists).
* **Database Ingestion:** Archiving ingests the `.img` file into the active survey's PostgreSQL database under the `img` table, which serves as a virtual archive for all metadata and parameters pertaining to each image.
* **Access Tools:** Software applications used to access and query this metadata include **pgAdmin** (PostgreSQL client), **R**, and **Matlab**.

---

### Realtime Processing & Annotation Pipeline

#### Processing GUI Functions
The HabCam realtime processing GUI is used for image processing, creating annotation assignments, generating lightmaps, and serving images to annotators. The PostgreSQL database provides the GUI with metadata required for:
1. **Lightmap Construction:** Building lightmaps using survey images collected at vehicle altitudes between 1 and 4 meters above the seafloor.
2. **Stereo Image Processing:** Processing images using vehicle altimeter depth (height above seafloor), combining intrinsic/extrinsic parameters calculated from pre-survey stereo camera calibrations with the survey's generated lightmap.

#### Annotation Workflow
* Processed images are organized into **primary**, **secondary**, and **special assignments**.
* Assignments are served via the HabCam annotation webserver, allowing scientists to annotate and analyze images in near-realtime while at sea.
* All annotation records and metadata are immediately written back to the PostgreSQL database.

---

### Data Review and Quality Assurance (QA)

* **Watch Chief Responsibilities:** At sea, the watch chief is responsible for training scientific party members and conducting periodic QA reviews on completed annotations.
* **Validation Criteria:** QA personnel review annotated images for completeness, taxonomic accuracy, and bounding box consistency.
* **Error Tracking:** Any discrepancies or errors identified during review are logged and reviewed directly with the annotator to ensure proper corrections are executed.

---

### Survey Archival Workflows

| Phase | Operational Steps |
| :--- | :--- |
| **At-Sea Archival** | Data managers continuously back up all metadata and raw optical data onto external hard drives. Processed images are redundantly backed up across multiple onboard HabCam servers. |
| **Post-Survey / Inter-Leg** | External hard drives and a complete PostgreSQL database export are handed over to NOAA ITD for backup on landservers. The database is restored on land to allow processing and annotation to continue seamlessly between survey legs. |

---

### Data Archival Infrastructure

#### Physical & Physical Server Methods
* **Physical Media:** Raw optical data and metadata are continuously written to formatted external hard drives at sea. Raw metadata is also continuously `rsync`-ed across onboard servers.

#### Landserver Infrastructure (Habcam-DS Series)
| Server | Primary Purpose & Workflow |
| :--- | :--- |
| **`Habcam-DS1`** | **Backup Server:** Automatically and recursively archives all relevant data directories from `Habcam-DS2` every 24 hours, maintaining daily execution log files. |
| **`Habcam-DS2`** | **Processing & Annotation Duplicate:** Mirrors the seagoing realtime processing and annotation server. Used on land to continue processing optical data, serving assignments, and providing assessment scientists with relational database access. |
| **`Habcam-DS3`** | **Storage & Media Swap Server:** Functions as a software backup for `DS2` and serves as the primary node for swapping hard disks containing images and metadata. Processed images from `DS2` are transferred here before being backed up offline. |

#### Relational Database Architecture
* **PostgreSQL (pgAdmin):** Serves as the primary operational database engine for active HabCam survey data and image metadata.
* **Oracle Cloud Infrastructure (`ORAPROD`):** Databases are migrated into an Oracle cloud database (`HABCAM` schema) to provide an additional layer of security, disaster recovery, and long-term multi-cruise archival safety.

---

## 2. Two-Stage Database Lifecycle

```text
[ At-Sea Acquisition & Annotations ] 
                │
                ▼
  Stage 1: Active PostgreSQL DB (pgAdmin)
  ├── Real-time Image Telemetry (img / img_lrauv)
  ├── Assignment Manifests (assignments)
  └── Raw Annotations (annotations)
                │
                ▼
      [ QA/QC & Validation Phase ]
  ├── Watch Chief Annotation Review
  ├── Bounding Box & Taxonomic Verification
  └── Data Quality Flagging (DATA_IDENTIFIER)
                │
                ▼
  Stage 2: Enterprise Oracle Cloud (ORAPROD)
  ├── Historical Multi-Cruise Warehouse (2009–Present)
  ├── Stock Assessment Ingestion (CASA / SAMS)
  └── Centralized GIS & Public Data Products
```

### Stage 1: Active Operations (PostgreSQL)
During sea operations and active survey legs, all real-time sensor streams, image manifests, and manual/AI annotations are written directly to a year-specific PostgreSQL database (`pgAdmin`).
* **Real-time Ingestion:** Image telemetry (`img` / `img_lrauv`) is staged via `temp_img` and written in 10-minute intervals.
* **Web Serving:** The active PostgreSQL instance connects directly to the HabCam web annotator to serve image assignments (`assignments`, `imagelist`) to scientists at sea or on land.

### Stage 2: QA/QC & Validation
Before permanent archival, watch chiefs and QA teams review all completed annotations:
* **Validation Criteria:** Taxonomic accuracy, bounding box precision, percent cover estimates, and completeness.
* **Flagging:** Deprecated or incorrect records are marked (`deprecated = true`), and the assignment is assigned a specific `data_identifier` code.

### Stage 3: Enterprise Archival (Oracle Cloud)
Once QA/QC is complete, the finalized current-year dataset is migrated into the NOAA Oracle Cloud database (`ORAPROD.HABCAM` schema).
* **Multi-Cruise Linkage:** Every record is assigned composite keys (`HABCAM_PK`, `CRUISE_ID`, `DATA_IDENTIFIER`) to link it within the multi-decade historical repository (2009–present).
* **Stock Assessment Ingestion:** Data from Oracle feeds directly into Catch-At-Size-Analysis (CASA) models and the Scallop Area Management Simulator (SAMS).

---

## 2. PostgreSQL vs. Oracle Schema Comparison

While the relational structures mirror each other logically, technical schema differences exist between the operational PostgreSQL database and the enterprise Oracle warehouse.

| Metric / Feature | Active PostgreSQL Database (`pgAdmin`) | Enterprise Oracle Database (`ORAPROD.HABCAM`) | Architectural & Query Impact |
| :--- | :--- | :--- | :--- |
| **Table Naming** | Lowercase, unprefixed (e.g., `annotations`, `assignments`, `img`) | Uppercase, `HABCAM_` prefixed (e.g., `HABCAM_ANNOTATIONS`, `HABCAM_ASSIGNMENTS`) | SQL queries targeting Oracle must use table prefixes (e.g., `HABCAM.HABCAM_ANNOTATIONS`). |
| **Primary Keys & Linkage** | Local text/integer IDs (e.g., `annotation_id`, `assignment_id`) | Composite surrogate keys (`HABCAM_PK`, `CRUISE_ID`, `DATA_IDENTIFIER`) | Oracle ties every record to a master cruise ID for multi-year historical queries. |
| **URL Identifiers** | Text strings in primary ID fields | Separate text and URL columns (`ANNOTATION_URL_ID`, `IMAGE_URL_ID`) | Oracle explicitly separates numeric database IDs from web-facing URL links. |
| **Spatial / Geometry** | Native PostGIS geometry types (`USER-DEFINED` / `POLYGON`) | `CLOB` text strings (`GEOMETRY_TEXT`, `THE_GEOMETRY`) | Oracle stores spatial bounding boxes as JSON/WKT CLOBs rather than PostGIS types. |
| **Data Types** | `text`, `integer`, `numeric`, `boolean` | `VARCHAR2(255/4000)`, `NUMBER`, `CLOB`, `TIMESTAMP WITH TIME ZONE` | Oracle uses `NUMBER` for all integers/floats and size-constrained `VARCHAR2` strings. |
| **Deprecation Flags** | Generic `deprecated` (`boolean`) | Table-prefixed `ANNOTATION_DEPRECATED`, `CLASS_DEPRECATED` (`NUMBER 0/1`) | Oracle uses numeric flags (`0` = active, `1` = deprecated) with table-prefixed column names. |

---

## 3. PostgreSQL Database Schema Architecture

The active PostgreSQL database contains 20 tables categorized into four functional modules.

### Schema Overview

| Category | Table Name | Columns | Purpose / Description |
| :--- | :--- | :--- | :--- |
| **Annotation Core** | `annotations` | 17 | Master bounding box annotations, measurements, and species classifications per image. |
| **Annotation Core** | `assignments` | 17 | Master records of annotation assignments (`YYYYNN`) and project goals. |
| **Annotation Core** | `imagelist` | 5 | References specific images assigned to an active annotation assignment. |
| **Annotation Core** | `imagelist_offline` | 5 | Image manifest lists assigned for offline / disconnected at-sea annotation. |
| **Telemetry & Payload** | `img` | 24 | Master telemetry and sensor metadata table for every acquired HabCam V4 image. |
| **Telemetry & Payload** | `img_lrauv` | 25 | Master telemetry for LRAUV AUV images and payload sensors (*Stella* / *Polaris*). |
| **Training Workflow** | `annotations_training` | 17 | Annotations produced during annotator training and calibration assignments. |
| **Training Workflow** | `assignments_training` | 17 | Training assignment records for onboarding annotators. |
| **Training Workflow** | `imagelist_training` | 5 | Image manifest lists assigned for training assignments. |
| **Data Staging** | `temp_img` | 19 | Staging table for temporary ingestion of HabCam V4 image telemetry. |
| **Data Staging** | `temp_lrauv_img` | 18 | Staging table for temporary ingestion of LRAUV AUV image telemetry. |
| **Metadata & Lookup** | `auth` | 3 | Annotator user credentials, access permissions, and authentication salts. |
| **Metadata & Lookup** | `classes` | 5 | Master taxonomic and target classification lookup table. |
| **Metadata & Lookup** | `facets` | 4 | Maps facet IDs to scope IDs to dictate how classes are evaluated in the GUI. |
| **Metadata & Lookup** | `idmodes` | 4 | Assignment-specific lists of annotation classes enabled in the GUI. |
| **Metadata & Lookup** | `scopes` | 3 | Defines scope categories (`1` = target, `2` = dominant substrate, `5` = % cover). |
| **Metadata & Lookup** | `substrate` | 10 | Automated % cover model predictions for seafloor substrate classes. |
| **PostGIS System** | `geometry_columns` | 7 | PostGIS spatial reference metadata view for geometry columns. |
| **PostGIS System** | `geography_columns` | 7 | PostGIS spatial reference metadata view for geography columns. |
| **PostGIS System** | `spatial_ref_sys` | 5 | PostGIS coordinate reference systems (CRS) definitions (e.g., EPSG:4326). |

---

### Key Table Definitions

#### `annotations` (Annotation Core)
Stores individual bounding box detections, percent cover estimates, and species labels.

| Col | Field Name | Data Type | Description | Example Value |
| :-: | :--- | :--- | :--- | :--- |
| 1 | `annotation_id` | `text` | Unique HTTP ID | `http://habcam.noaa.gov/ann_9000207e13f...` |
| 2 | `image_id` | `text` | Image URL | `http://habcam-data.whoi.edu/data/202501.png` |
| 3 | `scope_id` | `integer` | Scope code (1=target, 2=substrate, 5=% cover) | `1` |
| 4 | `category_id` | `text` | Category identifier URL | `http://habcam-data.whoi.edu/data/1102` |
| 5 | `geometry_text` | `text` | Bounding box coordinates (JSON format) | `"boundingBox":[[1054.67, 51.88], [1253.33, 346.54]]` |
| 6 | `thegeom` | `USER-DEFINED` | PostGIS polygon geometry | `SRID=4326;POLYGON((...))` |
| 7 | `annotator_id` | `text` | Annotator username | `ncalabrese` |
| 8 | `assignment_id` | `text` | Assignment HTTP URL ID | `http://habcam-data.whoi.edu/data/202501` |
| 9 | `timestamp` | `timestamp with tz` | Timestamp when annotation was created | `2025-05-22 14:12:57+00` |
| 10 | `class_id` | `integer` | Unique class ID mapping to `classes.class_id` | `185` (*Placopecten magellanicus*) |
| 11 | `deprecated` | `boolean` | Flag indicating if annotation is invalidated | `false` |
| 12 | `geometry_id` | `integer` | Geometry identifier reference | `12` |
| 13 | `imagename` | `text` | Raw image filename reference | `202501.20250528.100444831.772211.png` |
| 14 | `assignment_num` | `integer` | Assignment ID in form `YYYYNN` | `202501` |
| 15 | `percent_cover` | `integer` | Recorded percent cover (if applicable) | `25` |
| 16 | `comment` | `text` | Annotator notes or QA/QC comments | `High quality scallop identification` |
| 17 | `source` | `text` | Source model or interface version | `manual_annotator_v4` |

---

#### `assignments` (Annotation Core)
Defines structured annotation tasks assigned to scientists during a survey leg.

| Col | Field Name | Data Type | Description | Example Value |
| :-: | :--- | :--- | :--- | :--- |
| 1 | `assignment_id` | `integer` | Unique assignment ID (`YYYYNN`) | `202501` |
| 2 | `idmode` | `text` | Enabled species class list name | `NMFS 2025 ScallopsNFish` |
| 3 | `site_description` | `text` | Assignment location or objective | `At-Sea Primary Leg 1` |
| 4 | `project_name` | `text` | Survey project title | `NEFSC Scallop Survey` |
| 5 | `priority` | `text` | Assignment priority (`HIGH`, `MEDIUM`, `LOW`) | `HIGH` |
| 6 | `initials` | `text` | Creator initials or `AUTO` | `BVS` |
| 7 | `idmode_id` | `integer` | ID referencing `idmodes.idmode_id` | `202501` |
| 8 | `added_timestamp` | `timestamp with tz` | Creation timestamp | `2025-05-22 10:00:00+00` |
| 9 | `num_images` | `integer` | Total images in assignment | `39000` |
| 10 | `comment` | `text` | Assignment description notes | `Primary Leg 1 assignment` |
| 11 | `status` | `text` | Status (`ready`, `in_review`, `done`) | `ready` |
| 12 | `tracknum` | `integer` | Trackline sequence number | `101` |
| 13 | `startimage` | `text` | Starting image filename | `202501.20250522.000001.png` |
| 14 | `stopimage` | `text` | Ending image filename | `202501.20250522.039000.png` |
| 15 | `subsample` | `text` | Subsampling interval rule | `1:10` |
| 16 | `date` | `text` | Creation date (`YYYY-MM-DD`) | `2025-05-22` |
| 17 | `time` | `text` | Creation time (`HH:MM:SS`) | `10:00:00` |

---

#### `img` (HabCam V4 Telemetry)
Stores physical sensor measurements, geospatial coordinates, and calculated optical field-of-view for every HabCam frame.

| Col | Field Name | Data Type | Description | Example Value |
| :-: | :--- | :--- | :--- | :--- |
| 1 | `imagename` | `text` | Mapped PNG/TIF image filename | `202501.20250528.100444831.772211.png` |
| 2 | `lat` | `numeric` | Latitude in decimal degrees (NAD83) | `40.645128` |
| 3 | `lon` | `numeric` | Longitude in decimal degrees (NAD83) | `-72.065175` |
| 4 | `head` | `numeric` | Vehicle compass heading (degrees) | `322.77` |
| 5 | `pitch` | `numeric` | Vehicle pitch angle (degrees) | `4.83` |
| 6 | `roll` | `numeric` | Vehicle roll angle (degrees) | `-0.20` |
| 7 | `alt1` | `numeric` | Altitude off seabed in meters (Altimeter 1) | `2.22` |
| 8 | `alt2` | `numeric` | Altitude off seabed in meters (Altimeter 2) | `-99.99` |
| 9 | `vehicle_depth` | `numeric` | Water depth in meters (CTD pressure) | `47.44` |
| 10 | `s` | `numeric` | Practical Salinity (PSS-78) from CTD | `32.90` |
| 11 | `t` | `numeric` | Water temperature (°C) from CTD | `8.02` |
| 12 | `o2` | `numeric` | Dissolved Oxygen (mg/L or raw counts) | `5.92` |
| 13 | `cdom` | `numeric` | CDOM fluorescence (RFU) | `75.00` |
| 14 | `chlorophyll` | `numeric` | Chlorophyll-a fluorescence (RFU) | `64.00` |
| 15 | `backscatter` | `numeric` | Optical backscatter reading | `254.00` |
| 16 | `therm` | `integer` | Raw thermistor voltage reading | `549` |
| 17 | `internal_ph` | `numeric` | SeaFET internal pH reading | `8.05` |
| 18 | `external_ph` | `numeric` | SeaFET external pH reading | `8.07` |
| 19 | `timestamp` | `timestamp with tz` | Capture timestamp (UTC) | `2025-05-28 10:04:44.831+00` |
| 20 | `st_alt` | `numeric` | Stereo-calculated altitude off bottom (m) | `2.10` |
| 21 | `bottom_depth` | `numeric` | Ship fathometer seafloor depth (m) | `47.88` |
| 22 | `fov` | `numeric` | Calculated field-of-view width (m) | `1.02` |
| 23 | `fov_src` | `text` | Altitude source used for FOV (`alt1` or `st_alt`) | `st_alt` |
| 24 | `mm_px` | `numeric` | Image resolution (millimeters per pixel) | `0.55` |

---

#### `img_lrauv` (LRAUV AUV Telemetry)
Dedicated telemetry schema for long-range autonomous underwater vehicle payloads (*Stella* and *Polaris*).

| Col | Field Name | Data Type | Description | Example Value |
| :-: | :--- | :--- | :--- | :--- |
| 1 | `imagename` | `text` | LRAUV image filename | `LRAUV_Stella.20260601.120000.png` |
| 2 | `lat` / `lon` | `numeric` | Decimal degree coordinates (NAD83) | `39.81234`, `-73.12345` |
| 3 | `head` / `pitch` / `roll` | `numeric` | Vehicle 3D orientation (degrees) | `180.5`, `-1.2`, `-8.1` |
| 4 | `alt1` / `pathfinder_alt` | `numeric` | Altimeter / Pathfinder DVL altitude (m) | `2.50`, `2.51` |
| 5 | `vehicle_depth` | `numeric` | LRAUV water depth (m) | `52.3` |
| 6 | `o2` / `cdom` / `chlorophyll` | `numeric` | Calibrated environmental sensor metrics | `5.24 mg/L`, `4.79 RFU`, `1.43 ug/L` |
| 7 | `dq_energy` / `dq_corr` | `numeric` | Data quality energy & correlation metrics | `0.98`, `0.95` |
| 8 | `sea_water_salinity` / `temp` | `numeric` | Calibrated salinity (PSS-78) & temp (°C) | `32.85`, `7.85` |
| 9 | `vehicle` | `text` | Vehicle platform tag | `LRAUV_Stella` |

---

## 4. Oracle Query Filtering (`HABCAM_DATA_IDENTIFIER`)

When querying the enterprise Oracle Cloud database (`ORAPROD.HABCAM`), queries **must filter by `DATA_IDENTIFIER`** to separate assessment-grade data from training, calibration, and historical RSA surveys.

| `DATA_IDENTIFIER` | Operational Category & Assessment Status | Description & Usage Notes |
| :-: | :--- | :--- |
| **`1.0`** | **NEFSC V4 Scallop Assessment (QA/QCed)** | Official NOAA HabCam V4 survey data used in scallop stock assessments. Fully QA/QCed (2019–present). |
| **`1.1`** | **NEFSC V4 Invalid / Excluded** | Data NOT used in stock assessments (e.g., equipment malfunction or invalid trackline). |
| **`1.2`** | **NEFSC V4 Assessment Usable (QA/QCed)** | Supplemental survey data cleared for assessment use. |
| **`1.3`** | **NEFSC V4 Assessment Usable (Pending QA/QC)** | Valid survey data pending final QA/QC sign-off. |
| **`2.0`** | **Annotator Training** | Internal training assignments used for onboarding and calibrating annotators. |
| **`3.0`** | **Vehicle Calibration** | Optical, lightmap, or altimeter calibration runs. |
| **`4.0` – `4.2`** | **Special Projects** | Special research projects (e.g., `4.1` = 2022 Sand Dollar project; `4.2` = 2018 Testset selection). |
| **`6.0`** | **Historical RSA Data (No Metadata)** | Research Set-Aside (RSA) annotations from 2009, 2011, and 2012 without image metadata. |
| **`6.1`** | **RSA CFF HabCam V3 (2016)** | Coonamessett Farm Foundation V3 survey data used in scallop assessments. |
| **`6.2` – `6.3`** | **RSA Richard Taylor V2 (2012, 2014)** | Historical V2 HabCam survey data used in scallop assessments. |
| **`7.0`** | **NEFSC LRAUV Assessment Data (QA/QCed)** | Official LRAUV AUV survey data cleared and QA/QCed for stock assessment use. |
| **`7.1` – `7.3`** | **NEFSC LRAUV Secondary / Pending** | LRAUV AUV datasets categorized by assessment usability and QA/QC status. |

:::{.callout-note}
### Standard Stock Assessment Query Filter
For official stock assessment queries targeting HabCam V4 optical counts, filter for `DATA_IDENTIFIER = 1.0` (or `7.0` for LRAUV AUV data) in `HABCAM_ANNOTATIONS` and `HABCAM_IMAGE_METADATA`.
:::
