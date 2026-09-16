## Field Team Roles Table {#field-team-roles-table}

**Cruise Manning Structure & Shift Operations:** The HabCam scientific party typically consists of 9 to 10 personnel operating on 24-hour continuous sea trials divided into two 12-hour watch rotations (e.g., 11:30 AM to 11:30 PM and 11:30 PM to 11:30 AM). Each shift is managed by a Watch Chief and includes a rotating team of Pilots, Co-Pilots, and Annotators who cycle stations every 30 to 60 minutes to prevent screen fatigue. The Chief Scientist maintains active oversight across both watches (6 AM to 6 PM baseline plus as-needed response).

<table class="table table-striped">
<thead>
<tr>
<th width="20%">Role</th>
<th width="15%">Manning / Shift</th>
<th width="65%">Primary High-Level Responsibilities</th>
</tr>
</thead>
<tbody>
<tr>
<td><b>Chief Scientist</b></td>
<td>1 Person (Floating / Day)</td>
<td>Primary liaison between scientific party, vessel crew, and shore support; leads survey trackline design, staffing, daily safety briefings, and on-the-spot decision making.</td>
</tr>
<tr>
<td><b>HabCam Lead</b></td>
<td>1 Person (Technical Lead)</td>
<td>Technical authority for hardware, fiberoptic terminations, server configuration, GPS time syncing, navigation integration, light maps, and data redundancy.</td>
</tr>
<tr>
<td><b>Watch Chief</b></td>
<td>2 People (1 per 12-hr shift)</td>
<td>Direct shift supervisor; manages station role rotations, controls core flight software startup/shutdown, trains new scientists, and conducts shift QA/QC.</td>
</tr>
<tr>
<td><b>Pilot</b></td>
<td>Rotating (30–60 min blocks)</td>
<td>Actively flies vehicle via hydraulic winch joystick; maintains target altitude above seafloor using live camera feeds, flight GUI, and forward-looking sonar.</td>
</tr>
<tr>
<td><b>Co-Pilot</b></td>
<td>Rotating (30–60 min blocks)</td>
<td>Second pair of eyes for Pilot; monitors dual camera feeds, telemetry, and sonar for sand waves/boulders; optimizes camera/sonar settings; mitigates software glitches.</td>
</tr>
<tr>
<td><b>Annotator</b></td>
<td>Rotating (30–60 min blocks)</td>
<td>Frontline image processor; logs primary targets (scallops/fish) and secondary substrate/habitat data from incoming 10-minute image batches.</td>
</tr>
<tr>
<td><b>QA/QC Lead</b></td>
<td>1 Person / PopDyn</td>
<td>Hosts pre-cruise training, maintains identification guides, instructs scientists on protocols, and audits/certifies ~30 baseline images per annotator.</td>
</tr>
<tr>
<td><b>Population Dynamics</b></td>
<td>1–2 People</td>
<td>Quantitative scientist; collaborates on trackline design, executes camera calibrations, verifies altimeter confidence, and synthesizes population data.</td>
</tr>
</tbody>
</table>

<br>
<hr>

## 5. Field Team Roles Overview {#field-team-roles-overview}

### Chief Scientist {#role-chief-scientist}

Acts as the primary liaison between the scientific party, the vessel's crew, and shore-based support. Responsible for overall cruise execution, safety, trackline planning, and maintaining an open-door policy.

* **Submit Ship Time Requests:** Draft and submit formal administrative requests to secure vessel availability aligned with scientific objectives.
* **Plan the Survey and Tracklines:** Lead overarching scientific design, mapping out geographical scope and adjusting routes dynamically for weather or bathymetry.
* **Personnel Selection and Staffing:** Recruit and assemble a balanced scientific team with the necessary technical and watchstanding expertise.
* **Cruise Plan Updates:** Finalize operational schedules and delegate updates to co-leads for uninterrupted operational continuity.
* **Inter-Crew Communication & Captain Liaison:** Facilitate daily communication with the Captain and ship's command regarding navigation, weather, and safety.
* **Brief Watch Chiefs & Shift Transitions:** Proactively update shift leaders on scientific priorities, altered tracklines, and operational changes prior to watch changes.
* **Active Oversight & Daily Safety Briefings:** Maintain active presence for at least half of every watch shift and lead mandatory daily safety meetings at sea.


### HabCam Lead {#role-habcam-lead}

The primary technical authority responsible for vehicle hardware deployment, data integrity, and subsea/shipboard IT infrastructure.

* **Execute Fiberoptic Termination:** Perform precise fiberoptic splicing and clevis termination through the hydraulic winch line to guarantee low-loss telemetry.
* **Configure IT Infrastructure & Servers:** Set up main HabCam servers, control stations, annotation computers, and local network switches.
* **Install GPS Time Server & Navigation Integration:** Configure master GPS time synchronization and link shipboard GPS/fathometer feeds to vehicle logging systems.
* **Server Maintenance & Data Monitoring:** Verify storage drive mounting, Apache web server status, and real-time raw image/sensor data writes.
* **Build Light Maps & Oversee Image Pipeline:** Generate illumination correction maps and verify processed images serve smoothly to annotation workstations.
* **Metadata QA/QC & Continuous Data Backups:** Verify PostgreSQL database integrity and execute automated redundant backups onto spare drives.
* **Vehicle Pre-Dive Checks & Troubleshooting:** Lead pre-deployment deck inspections and rapidly resolve electrical, mechanical, or software faults.


### Watch Chief {#role-watch-chief}

Direct shift supervisor managing personnel, flight software operations, and biological data collection during assigned 12-hour rotations.

* **Manage 12-Hour Operational Shifts:** Command continuous watch shifts and execute thorough handovers with the counterpart Watch Chief.
* **Assign Station Rotations:** Create and enforce station schedules (Pilot, Co-Pilot, Annotator) rotating personnel every 30–60 minutes to manage fatigue.
* **Control Flight Software Systems:** Safely launch, monitor, and shut down pilot and co-pilot control software and logging interfaces.
* **Train & Onboard Scientific Staff:** Conduct standardized training for new annotators and flight standers using reference slide decks.
* **Integrate into Active Rotation:** Lead by example by taking regular turns at pilot, co-pilot, and annotation stations.
* **Shift Data QA/QC:** Review logged species identifications and habitat classifications to correct entry errors before shift sign-off.


### Pilot {#role-pilot}

Responsible for the active, real-time underwater navigation and altitude control of the HabCam vehicle above the seabed.

* **Execute Timed Rotations (30–60 Minutes):** Operate in short, high-concentration blocks to maintain sharp reflexes and situational awareness.
* **Maintain Safe Seafloor Altitude:** Continuously adjust winch controls to keep the vehicle at the target photographic altitude (typically ~2m) above bottom.
* **Operate Winch Joystick:** Command vertical vehicle movement using the physical winch joystick to pay out or haul in tow cable.
* **Monitor Telemetry & Forward Sonar:** Synthesize live camera video, flight GUI metrics (pitch, roll, tension), and forward-looking sonar to detect and avoid subsea hazards (boulders, wrecks, drop-offs).


### Co-Pilot {#role-copilot}

Acts as the technical support partner and second pair of eyes for the Pilot to ensure flight safety and sensor data quality.

* **Execute Timed Rotations (30–60 Minutes):** Rotate alongside the Pilot to maintain continuous vigilance across telemetry displays.
* **Monitor Dual Cameras & Sensor Telemetry:** Verify camera lighting, exposure, and continuous data logging across all environmental sensors (CTD, Oxygen, Fluorometer).
* **Sonar Hazard & Topography Analysis:** Interpret sonar displays for upcoming hazards and terrain changes (e.g., sand waves) requiring rhythmic winch adjustments.
* **Pilot Verbal Communication:** Maintain clear, concise verbal alerts to notify the Pilot immediately of upcoming obstacles or depth changes.
* **Real-Time Instrument Optimization & Software Mitigation:** Adjust camera frame rates, sonar ranges, and winch settings; immediately troubleshoot station software freezes or network glitches.


### Annotator {#role-annotator}

Frontline scientific data processor responsible for identifying, counting, and recording biological and habitat targets from incoming imagery.

* **Execute Timed Rotations (30–60 Minutes):** Process imagery in focused blocks alongside co-annotators to maintain high visual accuracy.
* **Process Image Assignments:** Rapidly review 10-minute image batches, logging primary targets (commercial species/fish) and secondary environmental parameters (substrate, encrusting organisms).
* **Complete Mandatory Protocol Training:** Complete pre-cruise or under-sail identification training to align species classification standards with project guidelines.


### QA/QC Lead {#role-qaqc-lead}

Primary auditor and educator guarding scientific data integrity across the annotation team.

* **Host Pre-Cruise Training Overview:** Lead mandatory orientation outlining data quality standards, species identification guides, and target priorities.
* **Instruct Standardized Protocols:** Teach exact identification criteria, substrate classifications, and efficient software operation.
* **Audit & Certify Annotators:** Review, grade, and verify a baseline sample set of ~30 images for every annotator to calibrate accuracy before independent logging.


### Population Dynamics Specialist {#role-population-dynamics}

Lead quantitative scientist linking field data acquisition with statistical modeling, stock assessment, and spatial analysis.

* **Strategic Trackline Planning & Dynamic Routing:** Collaborate with Chief Scientist to design survey routes based on depth stratification and historical distribution, updating lines dynamically for weather or time constraints.
* **Integrate into Operational Watch Rotation:** Stand regular shifts as Pilot, Co-Pilot, and Annotator to maintain direct understanding of data collection conditions.
* **Camera Calibrations & Altimeter Verification:** Oversee tank/field camera calibrations, calculate altimeter confidence intervals, and determine exact swept-area scale metrics.
* **Data Synthesis & Reporting:** Aggregate biological annotations, identify spatial coverage gaps, summarize population trends, and present preliminary statistical findings to leadership.

<br>
<hr>

## Detailed Field Team Roles {#field-team-roles-full-spec}

### CHIEF SCIENTIST {#spec-chief-scientist}

As the Chief Scientist, you act as the primary liaison between the scientific party, the vessel's crew, and shore-based support. You must be prepared to make decisive, on-the-spot decisions at any time of day or night to ensure the success and safety of the mission. Maintaining an open-door policy is essential to foster a communicative and supportive environment.

In addition to these duties, you are responsible for:

* **Submit Ship Time Requests:** Take charge of the administrative process required to secure vessel availability. This involves drafting and submitting formal requests to the appropriate scheduling bodies or funding, ensuring that the requested dates align with the mission's scientific objectives and seasonal requirements.
* **Plan the Survey and Decide on Tracklines:** Lead the overarching scientific design of the survey. You will map out the geographical scope of the survey, establish precise tracklines (routes) for data collection, and determine the most efficient deployment of instruments. You must also be ready to adapt these plans dynamically in response to weather, sea conditions, or preliminary findings.
* **Personnel Selection and Staffing:** Assemble a highly capable scientific team. You are responsible for identifying, recruiting, and selecting qualified researchers, technicians, and watchstanders, ensuring the team possesses a balanced mix of skills, experience, and expertise necessary to achieve the cruise's specific goals.
* **Complete and Delegate Cruise Plan Updates:** Maintain the official cruise plan as a living document. You will finalize all operational schedules, scientific protocols, and logistical details, keeping the document updated as parameters change. You must pass these updates onto your co-lead to ensure uninterrupted operational continuity and shared leadership.
* **Facilitate Communications Between Crews:** Serve as the central communication hub. You must bridge the gap between the scientific party and the maritime professionals operating the vessel, ensuring that both groups understand each other's needs, limitations, and daily objectives to maintain a harmonious and productive working environment.
* **Interact with the Vessel Captain and Crew:** Cultivate a strong, collaborative relationship with the ship's command. This requires regular, professional meetings with the Captain and senior crew to discuss navigation, logistical feasibility, impending weather systems, and the safe execution of complex scientific operations.
* **Update Watch Chiefs:** Empower your shift leaders. You are responsible for consistently briefing the Watch Chiefs on the broader scientific objectives, current equipment status, and any deviations from the primary plan, ensuring they have the information required to effectively manage their respective teams.
* **Communicate Changes for the Upcoming Watch:** Guarantee smooth shift transitions. Before a new watch takes over, you must proactively communicate any immediate shifts in strategy, altered tracklines, weather-related delays, or new scientific priorities so the oncoming team can hit the ground running without confusion.
* **Maintain Active Oversight During Watches:** Provide hands-on leadership and support. You are expected to be awake, physically present, and actively engaged for at least half of every single watch shift (day and night). This ensures you are available to troubleshoot equipment, guide data collection, and make immediate judgment calls.
* **Conduct Daily Safety Briefings at Sea:** Champion a culture of safety. You will lead mandatory daily meetings with the scientific team to review general emergency protocols, address specific operational hazards anticipated for that day's operations, and ensure that all personnel remain vigilant and secure while at sea.

<br>

### HABCAM LEAD {#spec-habcam-lead}

As the HABCAM Lead, you are the primary technical authority responsible for the deployment, operation, and data integrity of the imaging system. You manage both the physical hardware of the vehicle and the IT infrastructure required to process its data.

Your responsibilities include:

* **Perform Fiberoptic Termination:** Execute precise fiberoptic splicing and termination through the hydraulic winch line to ensure high-speed data transmission between the underwater HABCAM vehicle and the shipboard servers. This requires minimizing signal loss to guarantee reliable, real-time communication and video feeds.
* **Configure HABCAM IT Infrastructure:** Lead the setup of all specialized hardware and networking. This includes deploying and configuring the main HABCAM servers, pilot and co-pilot control stations, and annotation machines, ensuring seamless network integration and communication across the entire system.
* **Install and Calibrate the GPS Time Server:** Configure the dedicated GPS used for the network's time server. This guarantees that all scientific data, images, and metadata collected by the HABCAM are precisely time-stamped and synchronized to a single, highly accurate master clock.
* **Integrate Shipboard Navigation Systems:** Establish stable, reliable connections between the HABCAM system and the vessel's primary navigation instruments, specifically the ship's GPS and fathometer (depth sounder). This integration is crucial for accurate geographical and depth referencing of all collected imagery.
* **Maintain Server Operations:** Verify that all essential server infrastructure is fully operational at all times. This requires routinely checking that all necessary storage drives are correctly mounted and ensuring the Apache web server is running smoothly to host and distribute data to the science team without interruption.
* **Monitor Raw Data Acquisition:** Monitor the data pipeline to confirm that all raw imagery and sensor telemetry captured by the HABCAM are being successfully and continuously written to the primary storage servers, preventing any loss of data.
* **Build and Optimize Light Maps:** Generate and implement accurate light maps for the underwater camera systems. This calibration process corrects for uneven illumination caused by the strobes, ensuring consistent exposure and quality, evenly lit visuals for accurate scientific analysis and annotation.
* **Oversee Image Processing Workflow:** Supervise the real time image processing. You must verify that incoming raw images are being correctly processed, formatted, and reliably served to the annotation machines so that the scientific team can seamlessly identify and log marine life and habitats.
* **Perform Quality Assurance on Metadata:** Conduct quality control checks within the PostgreSQL database. This involves regularly verifying the accuracy, completeness, and integrity of all metadata (e.g., timestamps, location coordinates, altitude, depth) associated with the HABCAM imagery to ensure the final dataset is scientifically valid.
* **Execute Continuous Data Backups:** Implement and oversee a data redundancy protocol. You are responsible for continuously backing up all raw data, processed images, and database records onto spare, secure drives to safeguard against hardware failure, data corruption, or loss during the survey.
* **Conduct Pre-Deployment Vehicle Checks and Troubleshooting:** Lead the pre-dive inspection of the physical HABCAM vehicle. You must test all mechanical and electronic systems on deck, quickly identify potential faults, and troubleshoot any electrical or software issues before deployment to ensure a safe, successful, and uninterrupted dive.

<br>

### WATCH CHIEF {#spec-watch-chief}

As a Watch Chief, you are the direct shift supervisor responsible for managing the personnel, operations, and data collection during your assigned rotation. You ensure that the scientific objectives set by the Chief Scientist are executed safely and efficiently while maintaining the standards required for accurate data logging.

Your responsibilities include:

* **Manage 12-Hour Operational Shifts:** As one of exactly two Watch Chiefs assigned to the cruise, you are responsible for commanding a continuous 12-hour shift. You must maintain operational efficiency during your watch and ensure a seamless, detailed handover of information and system status to your counterpart during shift changes.
* **Assign and Manage Rotating Station Roles:** Orchestrate the team's workflow to maximize focus and prevent fatigue. You will create and enforce a schedule, rotating your assigned scientific personnel through the active stations (Pilot, co-pilot, and image annotator). You are also responsible for verifying that all team members are present, rested, and prepared for their assigned blocks.
* **Control Core Operational Software:** Serve as the gatekeeper for the vehicle's flight systems. You hold the direct responsibility for properly and securely starting up, monitoring, and shutting down the specialized pilot and co-pilot software systems used to fly and monitor the HABCAM, ensuring all programs are stable and communicating correctly with the hardware.
* **Train and Onboard New Scientists:** Act as the primary shift educator. You will conduct comprehensive training sessions for new or inexperienced scientists using standardized materials, such as the annotation PowerPoint. You must ensure they thoroughly understand the established protocols for identifying marine life, geological features, and logging accurate metadata.
* **Actively Participate in the Operational Cycle:** Lead by example. Rather than solely acting in a supervisory capacity, you are expected to fully integrate into the active rotation schedule. You will regularly take your turn at the pilot, co-pilot, and annotator stations, bearing a portion of the continuous operational workload alongside your team.
* **Perform Quality Assurance and Quality Control (QA/QC):** Safeguard the integrity of the scientific data. You will actively review the biological and habitat annotations logged by your team members during the shift. This involves cross checking complex species identifications, identifying and correcting entry errors, and ensuring that the data collected under your watch meets the survey's scientific standards.

<br>

### PILOT {#spec-pilot}

You are directly responsible for the safe, precise, and active underwater navigation of the HABCAM vehicle. Because this role requires intense concentration and quick reflexes to protect scientific equipment, you operate in short, focused intervals.

Your responsibilities include:

* **Execute Rotational Shifts (30 to 60 Minutes):** Maintain concentration and prevent operational fatigue. Because flying the vehicle requires uninterrupted attention, you will rotate into the pilot's seat for strictly timed blocks of 30 minutes to one hour. This rotation ensures your reflexes and situational awareness remain sharp during your entire time at the helm.
* **Maintain Safe Altitude Over the Seafloor:** Safeguard the physical integrity of the HABCAM vehicle. Your primary, overriding objective is to "fly" the vehicle at the optimal target altitude for photography (typically just a few meters above the bottom). You must constantly adjust to sudden changes in bathymetry to prevent catastrophic impacts with the seabed or entanglement in benthic structures.
* **Operate the Ship's Winch System via Joystick:** Manually control the vertical movement of the towed vehicle. Utilizing a specialized joystick interface, you will directly command the heavy machinery of the ship's winch. You must actively pay out or haul in the tow cable, making precise, real time micro-adjustments to the HABCAM's depth as the vessel moves forward through the water column.
* **Monitor Live Camera Feeds and Flight Telemetry (GUI):** Maintain constant visual and data awareness. You must continuously process multiple streams of information simultaneously, keeping your eyes locked on both the real time, downward-facing video feed from the HABCAM and the graphical user interface (GUI) of the winch flight software. This allows you to react to both visual terrain cues and telemetry data, such as cable tension, vehicle pitch, and exact depth.
* **Scan Forward-Looking Sonar for Obstacle Avoidance:** Anticipate and evade underwater hazards before they become a threat. Because visibility is limited underwater, you will continuously read and interpret the forward-looking sonar display to detect upcoming obstacles. Such as steep drop-offs, large boulders, shipwrecks, or abandoned fishing gear; well before they enter the camera's field of view, allowing you to proactively haul in the winch and avoid a collision.

<br>

### CO-PILOT {#spec-copilot}

As the Co-Pilot, you act as the essential second pair of eyes and primary technical support for the active Pilot. While the Pilot focuses entirely on the physical maneuvering of the vehicle, you are responsible for comprehensive situational awareness, system optimization, and hazard detection to ensure both the safety of the HABCAM and the quality of the scientific data.

Your responsibilities include:

* **Execute Rotational Shifts (30 to 60 Minutes):** Maintain vigilance as part of a synchronized team. Just like the Pilot, you will rotate into the Co-Pilot station for short, focused intervals of 30 minutes to one hour. This frequent rotation prevents screen fatigue and ensures you remain sharply attuned to subtle changes in sensor data and visual feeds.
* **Monitor Dual Camera Feeds and Sensor Telemetry:** Oversee the vehicle's diagnostic health. You are tasked with continuously watching the live video streams from multiple cameras to ensure clear visibility and proper illumination. Simultaneously, you must verify that all onboard environmental sensors (such as temperature, depth, and altimeters) are actively logging and transmitting accurate, uninterrupted data back to the ship.
* **Analyze Sonar for Obstacles and Topographical Shifts:** Serve as the early warning system for navigational hazards. You will actively interpret the sonar displays to map out the terrain ahead. This includes not only spotting immediate, dangerous obstacles (like boulders or wrecks) but also identifying complex seafloor topography, such as rolling sand waves, which require the Pilot to make continuous, rhythmic depth adjustments.
* **Communicate Critical Concerns to the Pilot:** Facilitate seamless, high-stress teamwork. You must maintain clear, constant, and concise verbal communication with the Pilot. If you detect an upcoming obstacle on the sonar or notice a sudden drop in sensor performance, you are responsible for immediately alerting the Pilot so they have the maximum possible time to react and adjust the winch.
* **Optimize Hardware and Software Settings in Real-Time:** Manage the configuration of the HABCAM's instruments. As environmental conditions change, you will actively fine tune the system's parameters. This includes adjusting sonar ranges for better resolution, modifying camera frame rates to match the vehicle's speed and altitude, and tweaking settings within the winch flight software to ensure smooth data capture.
* **Troubleshoot and Mitigate Station Software Issues:** Act as the immediate first line of defense for control station stability. If the pilot/co-pilot software freezes, an application crashes, or a localized networking glitch occurs, you must diagnose and resolve the issue on the fly. Your mitigation prevents operational downtime and ensures the Pilot does not lose control or visibility of the vehicle.

<br>

### ANNOTATOR {#spec-annotator}

As an Annotator, you are the frontline data processor of the scientific survey. Your primary responsibility is to translate the raw visual imagery captured by the underwater HABCAM into quantifiable, actionable scientific records. Because this requires sharp visual acuity and rapid decision making, you operate within a fast paced, collaborative workflow.

Your responsibilities include:

* **Execute Rotational Shifts (30 to 60 Minutes):** Maintain visual sharpness and combat screen fatigue. Accurately identifying camouflaged marine life and complex benthic habitats requires continuous concentration. To ensure the highest data quality, you will rotate through the annotation station in 30- to 60-minute intervals. You will frequently work concurrently alongside several other annotators to divide the workload and maintain a steady processing speed.
* **Process Primary and Secondary Image Assignments:** Analyze a rapid, continuous stream of visual data. You are tasked with reviewing batches of newly captured seafloor images, which are automatically pushed to your workstation every 10 minutes. You must swiftly and accurately log specific targets according to your assigned priorities; this typically involves identifying and counting primary species of interest (such as specific fish or scallops) while also recording secondary environmental details, like substrate types and other invertebrate life.
* **Complete Mandatory Identification and Protocol Training:** Guarantee standardized data collection and scientific validity. Before taking on active shifts, you must complete a specialized training program, conducted either prior to departure or while the vessel is under sail to the survey site. This essential onboarding ensures your identification skills are calibrated with the rest of the scientific party, and that you are fully proficient in utilizing the survey's specific annotation software and classification guidelines.

<br>

### QA/QC LEAD {#spec-qaqc-lead}

As the QA/QC lead, you are the primary guardian of data integrity for the survey. Your main objective is to ensure that all visual data processed by the scientific team is highly accurate, consistent, and scientifically sound. You act as both an educator and auditor for the annotation team.

Your responsibilities include:

* **Host the Comprehensive Pre-Cruise Training Overview:** Organize and lead the foundational orientation for the scientific party. Before the vessel departs or active data collection begins, you will host a mandatory, large-scale training session. This overview sets the baseline expectations for data quality, distributes visual reference guides, and aligns the entire team on the specific biological and ecological targets of the upcoming survey.
* **Train Annotators on Standardized Protocols:** Serve as the primary, ongoing educator for the data processing team. You are responsible for thoroughly instructing all annotators on the exact, standardized protocols required for the mission. This includes teaching precise species identification criteria, benthic habitat classification, and the correct, efficient operation of the customized annotation software to ensure absolute consistency across all shifts.
* **Audit and Confirm Baseline Annotation Accuracy:** Conduct targeted quality control checks on individual performance. For every annotator on the team, you will review, grade, and verify a sample set of approximately 30 assigned images. This initial audit allows you to catch individual misidentifications early, provide constructive, one-on-one feedback, and officially certify that each annotator is fully calibrated and ready to process large volumes of data independently.

<br>

### POPULATION DYNAMICS {#spec-population-dynamics}

As the Population Dynamics specialist, you are the lead quantitative scientist for the survey. Your primary role is to ensure that the data collected is statistically robust and biologically meaningful for stock assessments and ecological modeling. You bridge the gap between active field operations and high level data analysis.

Your responsibilities include:

* **Assist in Strategic Trackline Planning and Dynamic Routing:** Collaborate directly with the Chief Scientist to design mathematically sound survey routes. You provide input based on statistical requirements, historical population distributions, and depth stratifications. During the cruise, you actively participate in real-time decision-making, recalculating and updating tracklines on the fly when the team faces severe weather, time constraints, or unexpected biological discoveries.
* **Actively Participate in the Operational Cycle:** Maintain a hands-on connection to the raw data collection process. Rather than solely working on backend analysis, you are expected to fully integrate into the rotating shift schedule. You will take regular turns functioning as a HABCAM Pilot, Co-Pilot, and Annotator alongside the rest of the scientific party, ensuring you intimately understand the operational conditions and visual complexities of the data you will later analyze.
* **Execute System Calibrations and Altimeter Verification:** Guarantee the spatial accuracy of the survey's visual data. You will oversee camera calibration procedures and analyze the resulting calibration annotation data. You must calculate the statistical confidence of the altimeter's positioning to ensure that the exact scale of the images is known, which allows for precise measurements of organism density and total seafloor area swept. You will leverage these metrics to continually assist cruise planners in developing efficient tracklines for each leg of the journey.
* **Analyze Data, Identify Gaps, and Synthesize Results:** Serve as the central hub for data synthesis. You are responsible for aggregating and mathematically analyzing the massive volume of biological and habitat annotations generated by the shift teams. This requires meticulously auditing the dataset to identify any spatial or temporal gaps in coverage, summarizing population trends, and formally presenting these preliminary statistical results to leadership for ongoing survey adjustments and future stock assessments.
