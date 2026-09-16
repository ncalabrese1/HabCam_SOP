# Cable Harness Specifications & Wiring Schematics

### 1. System Overview
This slide set contains the electrical schematics, pinout diagrams, cable harness routing plans, and interconnect specifications for the Habitat Mapping Camera System (HabCam)[cite: 8].

As a continuously towed underwater imaging vehicle operating near the seabed, the HabCam relies on oceanographic sensors, imaging systems, and acoustic tools[cite: 8]. The cable harnesses described herein provide the link between the centralized vehicle telemetry housing, power distribution manifolds, and individual payload sensors[cite: 8].

### 2. Cable Harness Design Standards
All HabCam cable assemblies are engineered to withstand prolonged immersion in seawater under hydrostatic pressure, high tension, and continuous vibration[cite: 8]. Design criteria include[cite: 8]:
* **Wet-Pluggable Connectors:** Utilize marine-grade wet-mate circular connectors (e.g., SubConn, Impulse, Glenair) rated for deep-water hydrostatic pressures[cite: 8].
* **Mechanical Protection:** Cables feature heavy-duty polyurethane or neoprene outer jackets with embedded water-blocking compounds and Kevlar strain-relief strength members[cite: 8].
* **Noise Mitigation:** High-speed data pairs and sensitive optical feedback lines utilize individual foil wrapping, tinned-copper braided shielding, and isolated analog/digital ground returns to eliminate EMI and crosstalk from power lines[cite: 8].
* **Color-Coded Conductor Wiring:** Standardized color coding (following marine instrumentation standards) is maintained across all sub-assemblies to facilitate rapid deck repairs[cite: 8].

### 3. Maintenance, Deck Handling & Quality Assurance
To ensure system reliability during sea trials and survey operations, technicians must adhere to the following servicing guidelines[cite: 8]:

**Connector Care & Lubrication:**
* Inspect rubber faces and O-rings for grit, salt crystals, or hair prior to deployment[cite: 8].
* Apply a light coating of Dow Corning 111 silicone grease to neoprene connector faces[cite: 8].
* Never use petroleum-based lubricants, as they degrade neoprene seals[cite: 8].

**Bend Radius & Mechanical Anchoring:**
* Maintain a minimum static bend radius of 6x the cable diameter, and a dynamic bend radius of 10x the cable diameter[cite: 8].
* Secure all cables along the 304 Stainless Steel frame using rubber-lined P-clamps and heavy-duty UV-resistant cable ties[cite: 8].

**Dummy Plug Usage:**
* Always cap un-mated bulkhead connectors with protective dummy plugs immediately upon disconnect on deck to protect pin contacts from salt spray[cite: 8].

<br>
<hr>
<br>

### Cable Harness Master Reference

| Schematic Reference | Connector Model (Vehicle &rarr; Device Side) | Pin Count | Primary Protocol / Signal | Operating Voltage |
| :--- | :--- | :--- | :--- | :--- |
| **HabCamV4 - Chanos Cable** | 13-Pin Circular &rarr; 13-Pin Circular | 13 &rarr; 13 | Biogeochemical Data + Dual Power Rails | +12 VDC |
| **HabCamV4 Wiring - Camera Power Ethernet Cable** | 13-Pin Circular &rarr; 13-Pin Rectangular | 13 &rarr; 13 | Ethernet Data + Camera Power + Strobe Sync | System Power / Strobe Voltage |
| **Cable Wiring - A-Sphere** | SubConn MCIL4F &rarr; SubConn MCIL6F | 4 &rarr; 6 | RS232 Serial Data (Moxa Interface) + Power | +24 VDC |
| **Microstrain 3DM-GX3-25 AHRS** | SubConn MCIL6F &rarr; SubConn MCIL4F | 6 &rarr; 4 | RS232 Serial Data (Moxa Interface) + Power | +12 VDC |
| **HabCamV4 - BlueView Cable** | SubConn DIL13M &rarr; Teledyne Impulse Titan | 13 &rarr; 10 | Sonar TX/RX Differential + Power | 12-48 VDC |
| **Cable Wiring - Benthos PSA916 Sonar Altimeter** | SubConn MCIL6F &rarr; Impulse RMG-6FS | 6 &rarr; 6 | RS-232 Serial Data (Moxa Interface) + Power | +12 VDC (+6–24V Range) |
| **Cable Wiring - HabCam V4 Eco-Triplet** | SubConn MCIL6F &rarr; SubConn MCIL6F | 6 &rarr; 6 | RS232 Serial Data (Moxa Interface) + Power | +12 VDC |

<br>
<hr>
<br>

## Individual Cable Specifications & Wiring Diagrams

### Chanos Cable

<div align="center">
<img width="1265" height="892" alt="Chanos" src="https://github.com/user-attachments/assets/861b8031-917e-4d75-b12a-1a85c9511a82" />
</div>

<br>

**Schematic Reference:** HabCamV4 - Chanos Cable[cite: 8]  
**Primary Function:** Connects the Chanos in-situ biogeochemical analyzer to the HabCamV4 system for ocean chemistry data collection and sensor power[cite: 8].

**Key Specifications:**
* **Connector Configuration:** 13-pin circular connector on the vehicle hub end (P1) to a 13-pin circular connector on the Chanos sensor end (P2)[cite: 8].
* **Power Conductors:** Dual +12 VDC power rails using 18 AWG conductors (#18 WHT and #18 RED) paired with dual 18 AWG ground returns (#18 BLK and #18 GRN)[cite: 8].
* **Data & Signal Lines:** 24 AWG color-coded twisted pairs for differential communications and control lines[cite: 8].
* **Cable Shielding:** Pin 2 on both ends is dedicated to the cable screen/shield grounding[cite: 8].

### Camera Power Ethernet Cable

<div align="center">
 <img width="1265" height="892" alt="Camera_Power" src="https://github.com/user-attachments/assets/1adccfc7-2298-4c57-984e-4bfab114408a" />
</div>

<br>

**Schematic Reference:** HabCamV4 Wiring - Camera Power Ethernet Cable[cite: 8]  
**Primary Function:** Delivers primary system power, strobe synchronization signals, and high-speed Ethernet data between the central telemetry hub and the main camera system[cite: 8].

**Key Specifications:**
* **Connector Configuration:** 13-pin circular connector on the hub end (P1) to a 13-pin rectangular connector on the camera housing end (P2)[cite: 8].
* **Power & Strobe Conductors:** Heavy-gauge 18 AWG conductors dedicated to camera power delivery and strobe pulse timing (#18 RED/BLK for power, #18 WHT/GRN for strobe)[cite: 8].
* **Ethernet Data Lines:** 8 color-coded 24 AWG conductors forming four twisted pairs for high-speed Ethernet telemetry[cite: 8].

### A-Sphere Cable Wiring

<div align="center">
<img width="1249" height="878" alt="A-Sphere" src="https://github.com/user-attachments/assets/7b16fff8-3262-47b5-923d-b643877b3de8" />
</div>

<br>

**Schematic Reference:** Cable Wiring - A-Sphere[cite: 8]  
**Primary Function:** Connects the A-Sphere instrument to the HabCam system to supply system power (+24V DC) and handle RS232 serial data communication[cite: 8].

### Microstrain Cable

<div align="center">
<img width="1243" height="872" alt="Microstrain" src="https://github.com/user-attachments/assets/c90159af-3fc6-4f7c-897f-2826acea4ef9" />
</div>

<br>

**Schematic Reference:** Cable Wiring - Microstrain 3DM-GX3-25 AHRS[cite: 8]  
**Primary Function:** Connects the Microstrain 3DM-GX3-25 AHRS bottle to the HabCam telemetry bottle for real-time orientation tracking via an internal Moxa serial server[cite: 8].

### BlueView Cable

<div align="center">
<img width="995" height="700" alt="Blueview" src="https://github.com/user-attachments/assets/a90c4bdc-8003-4ed6-a2f9-6bcc87025911" />
</div>

<br>

**Schematic Reference:** HabCamV4 - BlueView Cable[cite: 8]  
**Primary Function:** Connects the BlueView Mk2 multibeam acoustic imaging sonar to the HabCam central telemetry hub for forward obstacle avoidance[cite: 8].

### Sonar Altimeter Cable

<div align="center">
<img width="1245" height="881" alt="Altimeter" src="https://github.com/user-attachments/assets/a46ecd7c-a77a-49b4-9b27-b9b9f1c37974" />
</div>

<br>

**Schematic Reference:** Cable Wiring - Benthos PSA916 Sonar Altimeter[cite: 8]  
**Primary Function:** Connects the Teledyne Benthos PSA-916 Sonar Altimeter directly to the electronics bottle to deliver height-above-seabed measurements[cite: 8].

### Eco-Triplet Cable

<div align="center">
<img width="1232" height="867" alt="Eco-Triplet" src="https://github.com/user-attachments/assets/6b8aa09c-f0d6-455f-8388-0fbc7dcf5e35" />
</div>

<br>

**Schematic Reference:** Cable Wiring - HabCamV4 Eco-Triplet[cite: 8]  
**Primary Function:** Connects the Sea-Bird / WET Labs ECO Triplet fluorometer bulkhead directly to the HabCam electronics bottle[cite: 8].