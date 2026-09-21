# Data Acquisition

## Overview of Software Components

* **Part 1: Engineering GUI**
  * **Sensor Status:** Displays real-time operational status for all acquiring sensors (indicated in green). At sea, all sensors except the deprecated SeaFET will show green.
  * **Monitored Sensors:**
    * **AHRS:** Attitude sensor
    * **CTD:** Sea-Bird 49
    * **Oxygen:** Sea-Bird 39
    * **GPS:** Ship's GPS feed
    * **Fathometer:** Ship's fathometer feed
    * **Altimeter:** Benthos PSA 916

* **Part 2: Image Viewer (Both Cameras Online)**
  * Displays the live feed of the stereo cameras in real time as frames are acquired.
  * Controls the winchfly plot display as well as the trigger rate for both cameras and strobes.

* **Part 3: Stereo Acquisition**
  * A terminal script that loads configuration files onto each camera and initiates the acquisition feed.

* **Part 4: Event Logger**
  * Utilized by the co-pilot to record timestamped operational notes, trackline changes, image highlights, shift changes, and system events.

---

## HabCam Vehicle Network Addresses

| Component / Device | IP Address |
| :--- | :--- |
| **Port Camera** | `192.168.125.120` |
| **Starboard Camera** | `192.168.125.121` |
| **Moxa Nport #1** | `192.168.135.200` |
| **Moxa Nport #2** | `192.168.135.202` |
| **Gardasoft #1** | `192.168.135.91` |
| **Gardasoft #2** | `192.168.135.92` |
| **BlueView Sonar** | `192.168.1.45` |

---

## At-Sea Data Management Workflow

### System Initialization & Time Synchronization
* All HabCam computers and servers are time-synchronized to the NOAA time server using Network Time Protocol (NTP).
* The main topside computer (`Dixon`) connects directly to the HabCam vehicle, onboard servers, ship GPS, and ship fathometer.
* Raw unprocessed environmental data is recorded directly into text files with associated timestamps for every entry.
* A processed CSV file is continuously generated to store vehicle sensor measurements, GPS coordinates, and corresponding stereo-paired image filenames formatted as `cruiseID.Timestamp.image#.tif`.

### Starting Acquisition
1. Power on the HabCam vehicle and launch the `habcamDataAq` software suite.

![Topside Workstation showing Engineering GUI and Image Viewer](https://github.com/user-attachments/assets/bb6b4c41-2fd1-4ab3-b57d-4075d76de282)

3. Launch the following desktop shortcuts: **Engineering GUI**, **Image Viewer**, and **StereoAq**.
4. Verify in the **Engineering GUI** that all active sensor indicators display a green light. 
   > **Note:** A red light indicates an offline or inactive sensor. The only expected red indicator during sea operations is the 5th sensor down on the left sidebar (the deprecated SeaFET sensor).
5. Open the **Image Viewer GUI** to confirm live video streams from both Port and Starboard cameras. Ensure the 3 status indicators relating to **recording**, **writing**, and **acquisition** are green.

---

## Metadata Directories & Verification

### Data File Formats
* **`.hab` Files:** Hourly raw data logs containing raw output streams from every sensor connected to the vehicle according to the HabCam v4 architecture.
* **`.img` Files:** Processed metadata CSV files containing timestamped image names, geospatial location coordinates, and aligned sensor metrics.

### Directory Structures
Verify that hourly raw data (`.hab`) and processed metadata (`.img`) files are actively being written to the following topside paths:

* **Hourly Raw Sensor Data (`.hab`):**
  ```bash
  /mnt/dixon-data/YYYY/hab/
