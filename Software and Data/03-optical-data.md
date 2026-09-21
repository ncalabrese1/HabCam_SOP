# Optical Data Management

## Purpose
This document outlines standard procedures for managing, storing, and analyzing optical data and related data products to ensure accuracy, consistency, and compliance with regulatory and organizational standards.

## Scope
This Standard Operating Procedure (SOP) applies to all personnel involved in collecting, processing, and maintaining optical data across the **NOAA NEFSC HabCam** and **Tethys AUV** teams.

---

## Key Definitions

| Term | Definition |
| :--- | :--- |
| **Raw Optical Data** | Unprocessed imagery collected via optical instruments (e.g., machine vision or stereo cameras) and stored in RAW formats such as Grayscale TIFFs or Bayer-encoded files. |
| **Processed Optical Data** | Optical images that have undergone stereo calibration, stereo rectification, debayering, color correction, lightmap calibration, or lightmap smoothing. |
| **Annotated Optical Data** | Optical images manually annotated using HabCam annotation software, with recorded data stored in HabCam relational databases. |
| **Raw Data** | Unprocessed oceanographic data directly collected from instruments on HabCam or Tethys stereo imaging payloads. |
| **Image Metadata** | Raw sensor streams processed into standardized formats for ingestion into HabCam relational databases and processing pipelines. |
| **Relational Databases** | PostgreSQL or Oracle database systems containing survey image metadata and annotated optical datasets. |

---

## Roles & Responsibilities

* **Technicians:** Execute live data collection and perform initial data validation.
* **Data Managers:** Oversee proper storage architecture, access permissions, and maintenance of optical data repositories and relational databases.
* **Quality Assurance Team:** Periodically review data accuracy and compliance across all operational phases—including calibration, lightmapping, processing, database ingestion, and manual annotations.
