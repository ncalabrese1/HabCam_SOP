# Database

## Archiving and Data Processing

### Database Archiving

* **Realtime Image Check:** During realtime processing, the HabCam software periodically checks for newly created `.img` files.
* **Write Verification Buffer:** To ensure a file is fully written before processing, the software never archives the newest `.img` file immediately; it waits until the subsequent `.img` file is created (e.g., `20250110_2010.img` is not archived until `20250110_2020.img` exists).
* **Database Ingestion:** Archiving ingests the `.img` file into the active survey's PostgreSQL database under the `IMG` table, which serves as a virtual archive for all metadata and parameters pertaining to each image.
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
* **PostgreSQL (pgAdmin):** Serves as the primary operational database engine for HabCam survey data and image metadata.
* **Oracle Cloud Infrastructure:** Databases are migrated into an Oracle cloud database to provide an additional layer of security, disaster recovery, and long-term archival safety.
