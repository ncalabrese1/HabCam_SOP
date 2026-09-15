<div align="center">

# HabCam Hardware, Schematics & Mounting Specifications

<div align="center">

<table>
  <tr>
    <td><a href="README.md">Home</a></td>
    <td><a href="01-overview-and-species.md"><b>01 Overview</b></a></td>
    <td><a href="02-hardware-and-schematics.md">02 Hardware</a></td>
    <td><a href="03-software-and-data.md">03 Software</a></td>
    <td><a href="04-staging-and-surveys.md">04 Staging</a></td>
    <td><a href="05-data-processing-and-analysis.md">05 Data & Analysis</a></td>
    <td><a href="06-maintenance-and-troubleshooting.md">06 Maintenance</a></td>
  </tr>
</table>

</div>
</table>

</div>

<br>

## Component Reference Table

| Attachment | Label | Description |
| :--- | :---: | :--- |
| **Frame** | A | Durable, protective and stable platform designed to carry imaging and sampling equipment close to the seafloor. |
| **Tail** | B | Supports the rudder, the elevator (vehicle lift) and the side scan sonar. |
| **Blue View** | C | An advanced multibeam imaging or scanning sonar system. It functions like an underwater acoustic camera, using high-frequency sound waves rather than light to generate real-time video-like imagery and 3D point clouds in zero-visibility conditions. |
| **CTD** | D | It is the primary instrument package used to measure the essential physical properties of seawater such as Conductivity, Temperature, and depth. |
| **EcoTriplet** | E | A multi-parameter optical sensor used to measure light scattering and fluorescence in natural waters. |
| **Main Electronics Bottle** | F | A heavy-duty, waterproof cylinder that protects an underwater vehicle’s delicate computers, navigation systems, and sensors from the crushing pressure of the ocean. |
| **Expansion Bottle** | G | A reservoir that maintains the internal pressure of a fluid-filled system slightly above the surrounding sea pressure. It allows internal oils to expand and contract as temperatures change, while preventing seawater from leaking into sensitive electronics or motors. |
| **SideScan Sonar** | H | An acoustic imaging system mounted on an underwater vehicle. It emits fan-shaped sound waves to the left and right, mapping the seafloor to create highly detailed, photo-like 2D images of the seabed, shipwrecks, and debris. |
| **Cable Tubes** | I | Hold the cables going to the sensors, reducing cable drag/chaffing. |
| **Cameras** | J | Downward facing stereo cameras which capture images of the seafloor, synchronized with the strobes. |
| **4 - Strobes** | K | High-intensity, flashing lights used to aid in vehicle recovery, mark worksites, and provide synchronized illumination for high-resolution imaging. |
| **Altimeter** | L | An acoustic instrument that measures the exact vertical distance between the vehicle and the seabed. It sends down sound waves and times how long the pulse takes to bounce back from the ocean floor. |
| **Attitude Sensor** | M | Measures its 3D orientation in the water, specifically tracking its pitch (nose up or down), roll (side-to-side tilt), and yaw/heading (compass direction). |
| **Pinger** | N | A device that emits repeatable acoustic sound pulses. They are used for tracking a vehicle's position, guiding it to specific subsea targets, or enabling emergency recovery if the vehicle is lost. |
| **Doors** | O | To keep the vehicle straight while towing, two doors are attached to HABCAM (act as a rudder). |
| **Lead Weights** | P | They allow the craft to achieve neutral buoyancy, fine-tune its center of gravity, and offset buoyant forces. |
| **Weak Link** | Q | An engineered mechanical failure point. It is designed to break intentionally when subjected to a predetermined threshold of force (e.g., getting snagged on rocks or debris) to prevent catastrophic damage to the rest of the vehicle or its tether. |


<br>
<hr>

## Frame Schematics & Physical Envelope

### Structural Core & Design Principles
* **Primary Frame Architecture:** Built from 304 Stainless Steel welded tubular/pipe roll-cage construction for high tensile strength, impact toughness, and chassis rigidity[cite: 2].
* **Corrosion Mitigation:** Exposed stainless steel structures utilize sacrificial zinc/aluminum anodes and marine-grade anti-corrosion coatings to combat pitting and galvanic action[cite: 2].
* **Fasteners & Hardware:** Passivated 316/304 Stainless Steel hardware with anti-seize provisions prevents thread galling during deck maintenance[cite: 2].
* **Hydrodynamic Tow Envelope:** Engineered to minimize roll and drag at 5–7 knot tow speeds approximately 2 meters above the seabed[cite: 2].

<br>

### Physical Specifications

| PARAMETER | SPECIFICATION | NOTES/DETAILS |
| :--- | :--- | :--- |
| **Frame Material** | 304 Stainless Steel | Welded tubular roll-cage assembly |
| **Dry Weight (In Air)** | Insert weight | Fully loaded with primary payload |
| **Wet Weight (In Water)** | Insert weight | Positive/negative buoyancy metrics |
| **Overall Dimensions (Without Tailside)** | 108.0in. x 62.0in. x 41.0in. | Max clearance envelope |
| **Overall Dimensions (With Tailside)** | 155.52in. x 62.0in. x | |
| **Max Depth Rating** | 110 to 113 meters (360 to 370 feet) | Frame & housing operational limit |
| **Operational Tow speed** | 5 - 7 knots | Optimal hydrodynamic stability |

<br>
<h2>HabCam Frame Schematics</h2>

<h3>1. System Overview</h3>
<p>This slide contains the structural schematics and technical drawings for the frame of the Habitat Mapping Camera System (HabCam). The HabCam is an advanced, continuously towed underwater imaging vehicle utilized for high-resolution benthic habitat and marine population surveys. The frame serves as the foundational chassis, providing structural integrity and spatial orientation for a multi-million-dollar suite of oceanographic sensors.</p>

<h3>2. Core Design</h3>
<p>Because the HabCam operates just meters above the seafloor in challenging marine environments, its frame is engineered to meet strict operational tolerances. The core design prioritizes three major factors:</p>
<ul>
  <li><b>Hydrodynamic Stability:</b> The geometry of the frame is designed to minimize drag and roll, ensuring a smooth, predictable flight path while being towed via the ship’s winch.</li>
  <li><b>Durability and Impact Resistance:</b> Constructed from marine grade, corrosion resistant alloys, the frame features a robust roll-cage architecture. This protects sensitive internal housings from catastrophic damage in the event of an accidental seafloor strike or boulder impact.</li>
  <li><b>Modularity and Accessibility:</b> The frame must allow for rapid on deck maintenance. The open architecture design ensures that technical teams (such as the HabCam Lead) can easily access fiber optic terminations, adjust wiring if necessary, and calibrate sensors between deployments.</li>
</ul>

<h3>3. Payload Integration</h3>
<p>These schematics detail the mounting points, brackets, and load-bearing structures required to securely integrate the vehicle's primary payload. When reviewing the drawings, note the specific integration zones for:</p>
<ul>
  <li>Primary and secondary high-resolution camera housings.</li>
  <li>Illumination strobes and associated power manifolds.</li>
  <li>Forward-looking obstacle avoidance sonar and altimeters.</li>
  <li>The primary tow-point assembly and fiber optic telemetry housing.</li>
</ul>

<h3>4. Navigating The Schematics</h3>
<p>The slide begins with complete, fully assembled isometric views, followed by detailed top, side, and front elevations. Subsequent sections break down individual sub-assemblies (e.g., the tow-arm mechanism, sensor brackets) and conclude with a comprehensive Bill of Materials (BOM) specifying required alloys, fasteners, and torque tolerances.</p>

<h3>5. Materials</h3>
<p>To maintain structural integrity during tow operations and cushion mechanical impact, the HabCam chassis and mounting components use the following specifications:</p>
<ul>
  <li><b>Primary Structural Frame:</b> 304 Stainless Steel tubular/pipe construction, selected for its high tensile strength, impact toughness, and weldability in structural roll-cage configurations.</li>
  <li><b>Corrosion Mitigation:</b> Exposed 304 stainless steel components are equipped with sacrificial zinc/aluminum anodes or marine-grade anti-corrosion coatings to protect against pitting and galvanic action in prolonged saltwater immersion.</li>
  <li><b>Fasteners and Brackets:</b> Passivated 316 / 304 Stainless Steel hardware with anti-seize provisions to prevent galling during on-deck servicing, or storage.</li>
  <li><b>Pressure Housings:</b> Hard-anodized aluminum or specialized pressure-rated housings for sensitive cameras, strobes, and oceanographic sensors.</li>
</ul>
---
<div align="center">

<h3>Frame Body Schematics</h3>


<img width="822" height="633" alt="Frame_1" src="https://github.com/user-attachments/assets/038bf5c3-27d2-4678-a678-dbfe66920244" />
<p><b>Frame Body 1</b></p>

<br>


<img width="864" height="668" alt="Frame_2" src="https://github.com/user-attachments/assets/5a0bbe8b-fefe-4fb1-aa54-fc83ea8066f4" />
<p><b>Frame Body 2</b></p>

<br>


<img width="864" height="668" alt="Frame_3" src="https://github.com/user-attachments/assets/15ccbcaa-6f22-42e5-8f58-ea3f4d336b77" />
<p><b>Frame Body 3</b></p>

<br>


<img width="864" height="668" alt="Frame_4" src="https://github.com/user-attachments/assets/d606768b-abba-4867-8b2a-76894ed717aa" />
<p><b>Frame Body 4</b></p>

<br>
<hr>
<br>

<h3>Tail Schematics</h3>


<img width="864" height="668" alt="Tail_1" src="https://github.com/user-attachments/assets/4534ddc4-1e33-4648-af17-b9180c6e0f16" />
<p><b>Tail 1</b></p>

<br>

<img width="864" height="668" alt="Tail_2" src="https://github.com/user-attachments/assets/ef7ecaf9-17cf-4710-96a1-41d5fe9d4c01" />
<p><b>Tail 2</b></p>

</div>
<br>

<h2>HabCam Cable Harness Specifications</h2>

<h3>1. System Overview</h3>
<p>This slide set contains the electrical schematics, pinout diagrams, cable harness routing plans, and interconnect specifications for the Habitat Mapping Camera System (HabCam).</p>
<p>As a continuously towed underwater imaging vehicle operating near the seabed, the HabCam relies on oceanographic sensors, imaging systems, and acoustic tools. The cable harnesses described herein provide the link between the centralized vehicle telemetry housing, power distribution manifolds, and individual payload sensors.</p>

<h3>2. Cable Harness Design Standards</h3>
<p>All HabCam cable assemblies are engineered to withstand prolonged immersion in seawater under hydrostatic pressure, high tension, and continuous vibration. Design criteria include:</p>
<ul>
  <li><b>Wet-Pluggable Connectors:</b> Utilize marine-grade wet-mate circular connectors (e.g., SubConn, Impulse, Glenair) rated for deep-water hydrostatic pressures.</li>
  <li><b>Mechanical Protection:</b> Cables feature heavy-duty polyurethane or neoprene outer jackets with embedded water-blocking compounds and Kevlar strain-relief strength members.</li>
  <li><b>Noise Mitigation:</b> High-speed data pairs and sensitive optical feedback lines utilize individual foil wrapping, tinned-copper braided shielding, and isolated analog/digital ground returns to eliminate EMI and crosstalk from power lines.</li>
  <li><b>Color-Coded Conductor Wiring:</b> Standardized color coding (following marine instrumentation standards) is maintained across all sub-assemblies to facilitate rapid deck repairs.</li>
</ul>

<h3>3. Maintenance, Deck Handling & Quality Assurance</h3>
<p>To ensure system reliability during sea trials and survey operations, technicians must adhere to the following servicing guidelines:</p>

<p><b>Connector Care & Lubrication:</b></p>
<ul>
  <li>Inspect rubber faces and O-rings for grit, salt crystals, or hair prior to deployment.</li>
  <li>Apply a light coating of Dow Corning 111 silicone grease to neoprene connector faces.</li>
  <li>Never use petroleum-based lubricants, as they degrade neoprene seals.</li>
</ul>

<p><b>Bend Radius & Mechanical Anchoring:</b></p>
<ul>
  <li>Maintain a minimum static bend radius of 6x the cable diameter, and a dynamic bend radius of 10x the cable diameter.</li>
  <li>Secure all cables along the 304 Stainless Steel frame using rubber-lined P-clamps and heavy-duty UV-resistant cable ties.</li>
</ul>

<p><b>Dummy Plug Usage:</b></p>
<ul>
  <li>Always cap un-mated bulkhead connectors with protective dummy plugs immediately upon disconnect on deck to protect pin contacts from salt spray.</li>
</ul>

<br>
<h2>HabCam Cable Schematics</h2>

<h3>1. System Overview</h3>
<p>This slide set contains the electrical schematics, pinout diagrams, cable harness routing plans, and interconnect specifications for the Habitat Mapping Camera System (HabCam).</p>
<p>As a continuously towed underwater imaging vehicle operating near the seabed, the HabCam relies on oceanographic sensors, imaging systems, and acoustic tools. The cable harnesses described herein provide the link between the centralized vehicle telemetry housing, power distribution manifolds, and individual payload sensors.</p>

<h3>2. Cable Harness Design Standards</h3>
<p>All HabCam cable assemblies are engineered to withstand prolonged immersion in seawater under hydrostatic pressure, high tension, and continuous vibration. Design criteria include:</p>
<ul>
  <li><b>Wet-Pluggable Connectors:</b> Utilize marine-grade wet-mate circular connectors (e.g., SubConn, Impulse, Glenair) rated for deep-water hydrostatic pressures.</li>
  <li><b>Mechanical Protection:</b> Cables feature heavy-duty polyurethane or neoprene outer jackets with embedded water-blocking compounds and Kevlar strain-relief strength members.</li>
  <li><b>Noise Mitigation:</b> High-speed data pairs and sensitive optical feedback lines utilize individual foil wrapping, tinned-copper braided shielding, and isolated analog/digital ground returns to eliminate EMI and crosstalk from power lines.</li>
  <li><b>Color-Coded Conductor Wiring:</b> Standardized color coding (following marine instrumentation standards) is maintained across all sub-assemblies to facilitate rapid deck repairs.</li>
</ul>

<h3>3. Maintenance, Deck Handling & Quality Assurance</h3>
<p>To ensure system reliability during sea trials and survey operations, technicians must adhere to the following servicing guidelines:</p>

<p><b>Connector Care & Lubrication:</b></p>
<ul>
  <li>Inspect rubber faces and O-rings for grit, salt crystals, or hair prior to deployment.</li>
  <li>Apply a light coating of Dow Corning 111 silicone grease to neoprene connector faces.</li>
  <li>Never use petroleum-based lubricants, as they degrade neoprene seals.</li>
</ul>

<p><b>Bend Radius & Mechanical Anchoring:</b></p>
<ul>
  <li>Maintain a minimum static bend radius of 6x the cable diameter, and a dynamic bend radius of 10x the cable diameter.</li>
  <li>Secure all cables along the 304 Stainless Steel frame using rubber-lined P-clamps and heavy-duty UV-resistant cable ties.</li>
</ul>

<p><b>Dummy Plug Usage:</b></p>
<ul>
  <li>Always cap un-mated bulkhead connectors with protective dummy plugs immediately upon disconnect on deck to protect pin contacts from salt spray.</li>
</ul>

<br>
<hr>
<br>

<h3>Cable Harness Master Reference</h3>

<table>
  <thead>
    <tr>
      <th align="left">Schematic Reference</th>
      <th align="left">Connector Model (Vehicle &rarr; Device Side)</th>
      <th align="left">Pin Count</th>
      <th align="left">Primary Protocol / Signal</th>
      <th align="left">Operating Voltage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="#chanos-cable"><b>HabCamV4 - Chanos Cable</b></a></td>
      <td>13-Pin Circular &rarr; 13-Pin Circular</td>
      <td>13 &rarr; 13</td>
      <td>Biogeochemical Data + Dual Power Rails</td>
      <td>+12 VDC</td>
    </tr>
    <tr>
      <td><a href="#camera-power-ethernet-cable"><b>HabCamV4 Wiring - Camera Power Ethernet Cable</b></a></td>
      <td>13-Pin Circular &rarr; 13-Pin Rectangular</td>
      <td>13 &rarr; 13</td>
      <td>Ethernet Data + Camera Power + Strobe Sync</td>
      <td>System Power / Strobe Voltage</td>
    </tr>
    <tr>
      <td><a href="#a-sphere-cable-wiring"><b>Cable Wiring - A-Sphere</b></a></td>
      <td>SubConn MCIL4F &rarr; SubConn MCIL6F</td>
      <td>4 &rarr; 6</td>
      <td>RS232 Serial Data (Moxa Interface) + Power</td>
      <td>+24 VDC</td>
    </tr>
    <tr>
      <td><a href="#microstrain-cable"><b>Microstrain 3DM-GX3-25 AHRS</b></a></td>
      <td>SubConn MCIL6F &rarr; SubConn MCIL4F</td>
      <td>6 &rarr; 4</td>
      <td>RS232 Serial Data (Moxa Interface) + Power</td>
      <td>+12 VDC</td>
    </tr>
    <tr>
      <td><a href="#blueview-cable"><b>HabCamV4 - BlueView Cable</b></a></td>
      <td>SubConn DIL13M &rarr; Teledyne Impulse Titan</td>
      <td>13 &rarr; 10</td>
      <td>Sonar TX/RX Differential + Power</td>
      <td>12-48 VDC</td>
    </tr>
    <tr>
      <td><a href="#sonar-altimeter-cable"><b>Cable Wiring - Benthos PSA916 Sonar Altimeter</b></a></td>
      <td>SubConn MCIL6F &rarr; Impulse RMG-6FS</td>
      <td>6 &rarr; 6</td>
      <td>RS-232 Serial Data (Moxa Interface) + Power</td>
      <td>+12 VDC (+6–24V Range)</td>
    </tr>
    <tr>
      <td><a href="#eco-triplet-cable"><b>Cable Wiring - HabCam V4 Eco-Triplet</b></a></td>
      <td>SubConn MCIL6F &rarr; SubConn MCIL6F</td>
      <td>6 &rarr; 6</td>
      <td>RS232 Serial Data (Moxa Interface) + Power</td>
      <td>+12 VDC</td>
    </tr>
  </tbody>
</table>

<br>
<hr>
<br>

<h2>Individual Cable Specifications & Wiring Diagrams</h2>
<h3 id="chanos-cable">Chanos Cable</h3>

<div align="center">
<img width="1265" height="892" alt="Chanos" src="https://github.com/user-attachments/assets/861b8031-917e-4d75-b12a-1a85c9511a82" />
</div>

<br>

<p><b>Schematic Reference:</b> HabCamV4 - Chanos Cable</p>
<p><b>Primary Function:</b> Connects the Chanos in-situ biogeochemical analyzer to the HabCamV4 system for ocean chemistry data collection and sensor power.</p>

<p><b>Key Specifications:</b></p>
<ul>
  <li><b>Connector Configuration:</b> 13-pin circular connector on the vehicle hub end (P1) to a 13-pin circular connector on the Chanos sensor end (P2).</li>
  <li><b>Power Conductors:</b> Dual +12 VDC power rails using 18 AWG conductors (#18 WHT and #18 RED) paired with dual 18 AWG ground returns (#18 BLK and #18 GRN).</li>
  <li><b>Data & Signal Lines:</b> 24 AWG color-coded twisted pairs for differential communications and control lines.</li>
  <li><b>Cable Shielding:</b> Pin 2 on both ends is dedicated to the cable screen/shield grounding.</li>
</ul>

<p><b>Pin Allocation Callouts:</b></p>
<ul>
  <li><b>Power Supply (+12V DC):</b> P1 Pins 3 & 12 (#18 WHT & #18 RED) &rarr; P2 Pins 3 & 12</li>
  <li><b>Power Ground (GND):</b> P1 Pins 1 & 13 (#18 BLK & #18 GRN) &rarr; P2 Pins 1 & 13</li>
  <li><b>Screen / Cable Shield:</b> P1 Pin 2 &rarr; P2 Pin 2</li>
  <li><b>Signal Lines (24 AWG):</b>
    <ul>
      <li>P1 Pin 4 (#24 BRN) &rarr; P2 Pin 4</li>
      <li>P1 Pin 5 (#24 BRN/WHT) &rarr; P2 Pin 5</li>
      <li>P1 Pin 6 (#24 BLU) &rarr; P2 Pin 7</li>
      <li>P1 Pin 7 (#24 BLU/WHT) &rarr; P2 Pin 6</li>
      <li>P1 Pin 8 (#24 ORN) &rarr; P2 Pin 8</li>
      <li>P1 Pin 9 (#24 ORN/WHT) &rarr; P2 Pin 9</li>
      <li>P1 Pin 10 (#24 GRN) &rarr; P2 Pin 10</li>
      <li>P1 Pin 11 (#24 GRN/WHT) &rarr; P2 Pin 11</li>
    </ul>
  </li>
</ul>

<br>
<hr>
<br>
<h3 id="camera-power-ethernet-cable">Camera Power Ethernet Cable</h3>

<div align="center">
 <img width="1265" height="892" alt="Camera_Power" src="https://github.com/user-attachments/assets/1adccfc7-2298-4c57-984e-4bfab114408a" />
</div>

<br>

<p><b>Schematic Reference:</b> HabCamV4 Wiring - Camera Power Ethernet Cable</p>
<p><b>Primary Function:</b> Delivers primary system power, strobe synchronization signals, and high-speed Ethernet data between the central telemetry hub and the main camera system.</p>

<p><b>Key Specifications:</b></p>
<ul>
  <li><b>Connector Configuration:</b> 13-pin circular connector on the hub end (P1) to a 13-pin rectangular connector on the camera housing end (P2).</li>
  <li><b>Power & Strobe Conductors:</b> Heavy-gauge 18 AWG conductors dedicated to camera power delivery and strobe pulse timing:
    <ul>
      <li>Camera Power: #18 RED (Camera Power) paired with #18 BLK (Camera Ret)</li>
      <li>Strobe Control: #18 WHT (Strobe Signal) paired with #18 GRN (Strobe Ret)</li>
    </ul>
  </li>
  <li><b>Ethernet Data Lines:</b> 8 color-coded 24 AWG conductors forming four twisted pairs for high-speed Ethernet telemetry.</li>
  <li><b>Cable Shielding:</b> Pin 2 on both connectors connects directly to the cable screen/shield for noise suppression.</li>
</ul>

<p><b>Pin Allocation Callouts:</b></p>
<ul>
  <li><b>Camera Return (GND):</b> P1 Pin 1 (#18 BLK) &rarr; P2 Pin 1</li>
  <li><b>Screen / Cable Shield:</b> P1 Pin 2 &rarr; P2 Pin 2</li>
  <li><b>Strobe Signal:</b> P1 Pin 3 (#18 WHT) &rarr; P2 Pin 3</li>
  <li><b>Ethernet Data Lines (24 AWG):</b>
    <ul>
      <li>P1 Pin 4 (#24 BRN/WHT) &rarr; P2 Pin 4</li>
      <li>P1 Pin 5 (#24 BRN) &rarr; P2 Pin 5</li>
      <li>P1 Pin 6 (#24 BLU) &rarr; P2 Pin 6</li>
      <li>P1 Pin 7 (#24 BLU/WHT) &rarr; P2 Pin 7</li>
      <li>P1 Pin 8 (#24 ORN/WHT) &rarr; P2 Pin 8</li>
      <li>P1 Pin 9 (#24 ORN) &rarr; P2 Pin 9</li>
      <li>P1 Pin 10 (#24 GRN) &rarr; P2 Pin 10</li>
      <li>P1 Pin 11 (#24 GRN/WHT) &rarr; P2 Pin 11</li>
    </ul>
  </li>
  <li><b>Camera Power:</b> P1 Pin 12 (#18 RED) &rarr; P2 Pin 12</li>
  <li><b>Strobe Return:</b> P1 Pin 13 (#18 GRN) &rarr; P2 Pin 13</li>
</ul>

<br>
<hr>
<br>
<h3 id="a-sphere-cable-wiring">A-Sphere Cable Wiring</h3>

<div align="center">
<img width="1249" height="878" alt="A-Sphere" src="https://github.com/user-attachments/assets/7b16fff8-3262-47b5-923d-b643877b3de8" />
</div>

<br>

<p><b>Schematic Reference:</b> Cable Wiring - A-Sphere</p>
<p><b>Primary Function:</b> Connects the A-Sphere instrument to the HabCam system to supply system power (+24V DC) and handle RS232 serial data communication.</p>

<p><b>Key Specifications:</b></p>
<ul>
  <li><b>Connector Configuration:</b> SubConn 4-pin inline female connector (MCIL4F) with lock collar and snap ring (MCDLS-M / MCDLS Snap Ring) on the HabCam side (P1) to a SubConn 6-pin inline female connector (MCIL6F) on the A-Sphere instrument side (P2).</li>
  <li><b>Power Lines (P1 - HabCam Side):</b> Dual 18 AWG conductors for +24V DC power (#18 RED & #18 GRN) and dual 18 AWG conductors for Power Ground (#18 BLK & #18 WHT).</li>
  <li><b>Serial Communication (P2 - Instrument Side):</b> 20 AWG color-coded conductors providing RS232 transmit, receive, and signal ground connections between the instrument and the internal Moxa serial server.</li>
</ul>

<p><b>Pin Allocation Callouts:</b></p>
<ul>
  <li><b>P1 (HabCam Side - Power):</b>
    <ul>
      <li>Pins 1 & 2 (#18 BLK & #18 WHT): Power Ground</li>
      <li>Pins 3 & 4 (#18 RED & #18 GRN): +24V DC</li>
    </ul>
  </li>
  <li><b>P2 (A-Sphere Side - RS232 Serial Data):</b>
    <ul>
      <li>Pin 1 (BLK #20): RS232 RX (Instrument)</li>
      <li>Pin 2 (WHT #20): RS232 TX (Instrument)</li>
      <li>Pin 3 (GRN #20): RS232 TX (Moxa)</li>
      <li>Pin 4 (ORN #20): RS232 RX (Moxa)</li>
      <li>Pin 5 (BLU #20): RS232 Signal Ground</li>
    </ul>
  </li>
</ul>

<br>
<hr>
<br>
<h3 id="microstrain-cable">Microstrain Cable</h3>

<div align="center">
<img width="1243" height="872" alt="Microstrain" src="https://github.com/user-attachments/assets/c90159af-3fc6-4f7c-897f-2826acea4ef9" />
</div>

<br>

<p><b>Schematic Reference:</b> Cable Wiring - Microstrain 3DM-GX3-25 AHRS</p>
<p><b>Primary Function:</b> Connects the Microstrain 3DM-GX3-25 AHRS (Attitude and Heading Reference System) bottle to the HabCam telemetry bottle for real-time roll, pitch, and orientation tracking via an internal Moxa serial server.</p>

<p><b>Key Specifications:</b></p>
<ul>
  <li><b>Connector Configuration:</b> SubConn 4-pin inline female connector (MCIL4F) on the AHRS Bottle side (P1) to a SubConn 6-pin inline female connector (MCIL6F) on the HabCam Bottle side (P2). Both connectors utilize locking collars and snap rings (MCDLS-M / MCDLS Snap Ring).</li>
  <li><b>Power Supply:</b> +12 VDC power rail and dedicated power ground bridging the two bottles.</li>
  <li><b>Serial Communication:</b> RS232 serial telemetry links the AHRS instrument transmit/receive lines directly to the Moxa serial port interface.</li>
</ul>

<p><b>Pin Allocation Callouts:</b></p>
<ul>
  <li><b>P1 (AHRS Bottle Side):</b>
    <ul>
      <li>Pin 1 (#18 BLK): Power Ground</li>
      <li>Pin 2 (#18 WHT): +12V DC</li>
      <li>Pin 3 (#18 RED): Instrument RS232 TX (signals to Moxa RX)</li>
      <li>Pin 4 (#18 GRN): Instrument RS232 RX (signals from Moxa TX)</li>
    </ul>
  </li>
  <li><b>P2 (Electronics Bottle Side):</b>
    <ul>
      <li>Pin 1 (BLK #20): Power Ground</li>
      <li>Pin 2: Unused / No Connection (NC)</li>
      <li>Pin 3 (RED #20): +12V DC</li>
      <li>Pin 4 (GRN #20): Moxa RS232 RX</li>
      <li>Pin 5 (ORN #20): Moxa RS232 TX</li>
      <li>Pin 6 (BLU #20): Moxa RS232 GND</li>
    </ul>
  </li>
</ul>

<br>
<hr>
<br>
<h3 id="blueview-cable">BlueView Cable</h3>

<div align="center">
<img width="995" height="700" alt="Blueview" src="https://github.com/user-attachments/assets/a90c4bdc-8003-4ed6-a2f9-6bcc87025911" />
</div>

<br>

<p><b>Schematic Reference:</b> HabCamV4 - BlueView Cable</p>
<p><b>Primary Function:</b> Connects the BlueView Mk2 multibeam acoustic imaging sonar to the HabCam central telemetry hub for real-time forward obstacle avoidance and seabed monitoring.</p>

<p><b>Key Specifications:</b></p>
<ul>
  <li><b>Connector Configuration:</b> SubConn 13-pin circular male connector (DIL13M) with a locking sleeve collar (DLSA-M / DLSA-Snap Ring) on the vehicle hub end (P1) to a Teledyne Impulse Titan Series 10-pin right-angle connector (MKS(W)-10-CCP-RA) on the sonar end (P2).</li>
  <li><b>Cable Stock:</b> Underwater ethernet-rated cable (D-P4TP24#SW or equivalent).</li>
  <li><b>Signal Protocol:</b> Differential Sonar TX/RX data communications using 24 AWG color-coded conductors.</li>
  <li><b>Operating Voltage:</b> Wide-range input (12–48 VDC) utilizing 18 AWG primary power conductors feeding split 24 AWG pin terminations at the sonar connector.</li>
</ul>

<p><b>Pin Allocation Callouts:</b></p>
<ul>
  <li><b>Power Ground:</b> P1 Pin 1 (#18 BLK) &rarr; P2 Pins 7 & 8 (#24 YEL/WHT & YEL)</li>
  <li><b>Power Supply (12–48 VDC):</b> P1 Pins 2 & 3 (#18 WHT) &rarr; P2 Pins 4 & 5 (#24 BLU/WHT & BLU)</li>
  <li><b>Sonar RX+ / RX-:</b> P1 Pin 8 (#24 ORN) & Pin 9 (#24 ORN/WHT) &rarr; P2 Pin 1 & Pin 2</li>
  <li><b>Sonar TX+ / TX-:</b> P1 Pin 11 (#24 GRN/WHT) & Pin 10 (#24 GRN) &rarr; P2 Pin 3 & Pin 6</li>
  <li><b>Unused Terminations:</b> P1 Pins 4, 5, 6, 7, 12, 13; P2 Pins 9, 10</li>
</ul>

<br>
<hr>
<br>
<h3 id="sonar-altimeter-cable">Sonar Altimeter Cable</h3>

<div align="center">
<img width="1245" height="881" alt="Altimeter" src="https://github.com/user-attachments/assets/a46ecd7c-a77a-49b4-9b27-b9b9f1c37974" />
</div>

<br>

<p><b>Schematic Reference:</b> Cable Wiring - Benthos PSA916 Sonar Altimeter</p>
<p><b>Primary Function:</b> Connects the Teledyne Benthos PSA-916 Sonar Altimeter directly to the electronics bottle to deliver height-above-seabed measurements to an internal Moxa serial interface.</p>

<p><b>Key Specifications:</b></p>
<ul>
  <li><b>Connector Configuration:</b> Impulse 6-pin female connector with locking sleeve (RMG-6FS -w/ Sleeve) on the altimeter end (P1) to a SubConn 6-pin inline female connector (MCIL6F) with snap ring and locking collar (MCDLS Snap Ring / MCDLS-F) on the electronics bottle end (P2).</li>
  <li><b>Power Supply:</b> Accepts wide input range (+6 to 24V) at the altimeter, powered via a +12V DC rail and external power ground line from the electronics bottle.</li>
  <li><b>Serial Communication:</b> RS-232 input/output lines route directly to the Moxa serial port interface (Rx, Tx, and RS-232 GND).</li>
</ul>

<p><b>Pin Allocation Callouts:</b></p>
<ul>
  <li><b>P1 (Altimeter Side - Impulse RMG-6FS):</b>
    <ul>
      <li>Pin 1: RS-232 Input / External Key Input</li>
      <li>Pin 2: External Power GND</li>
      <li>Pin 4: RS-232 Output / Error Output</li>
      <li>Pin 5: External Power (+6–24V)</li>
      <li>Pins 3 & 6: Unused / No Connection (NC)</li>
    </ul>
  </li>
  <li><b>P2 (Electronics Bottle Side - SubConn MCIL6F):</b>
    <ul>
      <li>Pin 1: Power GND</li>
      <li>Pin 2: Unused / No Connection (NC)</li>
      <li>Pin 3: +12V DC</li>
      <li>Pin 4: Moxa RS-232 Tx</li>
      <li>Pin 5: Moxa RS-232 Rx</li>
      <li>Pin 6: RS-232 GND</li>
    </ul>
  </li>
</ul>

<br>
<hr>
<br>
<h3 id="eco-triplet-cable">Eco-Triplet Cable</h3>

<div align="center">
<img width="1232" height="867" alt="Eco-Triplet" src="https://github.com/user-attachments/assets/6b8aa09c-f0d6-455f-8388-0fbc7dcf5e35" />
</div>

<br>

<p><b>Schematic Reference:</b> Cable Wiring - HabCamV4 Eco-Triplet</p>
<p><b>Primary Function:</b> Connects the Sea-Bird / WET Labs ECO Triplet fluorometer bulkhead directly to the HabCam electronics bottle for environmental optical sampling and data transmission.</p>

<p><b>Key Specifications:</b></p>
<ul>
  <li><b>Connector Configuration:</b> SubConn 6-pin inline female connector (MCIL6F) on the ECO Triplet bulkhead side (P1) to a matching SubConn 6-pin inline female connector (MCIL6F) on the electronics bottle side (P2). Both ends are secured with locking collars and snap rings (MCDLS-M / MCDLS Snap Ring).</li>
  <li><b>Power Supply:</b> Delivered over a +12 VDC power line with a shared power ground return using 20 AWG conductors.</li>
  <li><b>Serial Communication:</b> RS232 serial interface routing instrument transmit and receive lines to the internal Moxa serial server.</li>
</ul>

<p><b>Pin Allocation Callouts:</b></p>
<ul>
  <li><b>P1 (ECO Triplet Bulkhead Side):</b>
    <ul>
      <li>Pin 1 (#20 BLK): Power Ground</li>
      <li>Pin 2 (#20 WHT): Instrument RS232 RX (connects to Moxa TX)</li>
      <li>Pin 3: Unused / No Connection (NC)</li>
      <li>Pin 4 (#20 GRN): +12V DC</li>
      <li>Pin 5 (#20 ORN): Instrument RS232 TX (connects to Moxa RX)</li>
      <li>Pin 6: Unused / No Connection (NC)</li>
    </ul>
  </li>
  <li><b>P2 (Electronics Bottle Side):</b>
    <ul>
      <li>Pin 1 (BLK #20): Power Ground</li>
      <li>Pin 2: Unused / No Connection (NC)</li>
      <li>Pin 3 (RED #20): +12V DC</li>
      <li>Pin 4 (GRN #20): Moxa RS232 TX</li>
      <li>Pin 5 (ORN #20): Moxa RS232 RX</li>
      <li>Pin 6 (BLU #20): Moxa RS232 GND</li>
    </ul>
  </li>
</ul>

<br>

---

<br>
<div align="center">

# HabCam Electrical Schematics & Network Architecture

</div>

<br>

<h2>Master Table of Contents</h2>

<table>
  <thead>
    <tr>
      <th align="left">Section</th>
      <th align="left">Description</th>
      <th align="left">Primary Components / Schematics</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="#network-connectivity"><b>1. Network Connectivity & CWDM</b></a></td>
      <td>Copper-to-fiber multiplexing and subsea telemetry pipeline.</td>
      <td>Mako Cameras, BlueView Sonar, SFP Media Converters, OptiLink</td>
    </tr>
    <tr>
      <td><a href="#ethernet-schematics"><b>2. Ethernet Electrical Routing</b></a></td>
      <td>Dual switch architecture inside the Electronics Bottle.</td>
      <td>Ubiquiti Switches, SubConn DBH13M Data Breakouts, Test Ports</td>
    </tr>
    <tr>
      <td><a href="#bulkhead-specs"><b>3. Bulkhead Specifications</b></a></td>
      <td>Pinouts, O-rings, and thread specs for Electronics Bottle bulkheads.</td>
      <td>SubConn MCBH3M, MCBH4M, MCBH6M, DBH13M, OptiLink A-04-BCR</td>
    </tr>
    <tr>
      <td><a href="#fiber-cabling"><b>4. Internal Fiber Cabling</b></a></td>
      <td>Media conversion, SFP transceivers, and CWDM channels.</td>
      <td>IMC IE-ModeConverter, AFL CWDM Mux, L-Com ST Barrels</td>
    </tr>
    <tr>
      <td><a href="#endcap-placements"><b>5. Bottle Endcap Layouts</b></a></td>
      <td>External port assignments for Electronics & Expansion bottles.</td>
      <td>Front/Back Endcaps (J1–J22, J50–J52), Expansion Bottle (J1–J11)</td>
    </tr>
    <tr>
      <td><a href="#serial-ports"><b>6. Serial Port Arrays (INST 1–12)</b></a></td>
      <td>Moxa N-Port servers and regulated DC power buses.</td>
      <td>Moxa 5650-8-DT, Terminal Blocks T5–T16, SubConn MCBH6M</td>
    </tr>
    <tr>
      <td><a href="#ac-power-strobes"><b>7. AC Power & Strobe Control</b></a></td>
      <td>AC distribution, DC rail rectifiers, and strobe timing bus.</td>
      <td>Astrodyne PS1–PS4, Sealevel CC320, MVS 5000 Strobes</td>
    </tr>
    <tr>
      <td><a href="#subsystem-housings"><b>8. Sensor Bottles & Housings</b></a></td>
      <td>Wiring schematics for individual pressure housings.</td>
      <td>Strobe Bottle, Attitude Bottle, Prosilica & Mako Camera Housings</td>
    </tr>
    <tr>
      <td><a href="#sensor-cables"><b>9. CTD & Environmental Cables</b></a></td>
      <td>Dedicated cable assemblies for oceanographic sampling.</td>
      <td>Sea-Bird SBE 37/49 CTD, ECO-Triplet Fluorometer Cable</td>
    </tr>
  </tbody>
</table>

<br>
<hr>
<br>

<a name="network-connectivity"></a>
<h2>1. HabCam Network Connectivity & Telemetry Architecture</h2>

<p>The HabCam network architecture details the end-to-end data conversion and multiplexing pipeline. High-resolution subsea imaging, acoustic sonar, and serial instrument telemetry convert from copper electrical signals into Coarse Wavelength Division Multiplexing (CWDM) optical signals for long-distance transmission across the primary tow cable umbilical.</p>

<div align="center">
<img width="1268" height="823" alt="Network Connectivity" src="https://github.com/user-attachments/assets/b6d04387-a717-4559-a1af-26f3b52abf03" />
  <p><i>Figure 1.1: HabCam Subsea Network Connectivity & CWDM Conversion Schematic.</i></p>
</div>

<br>

<h3>CWDM Wavelength Allocation & Subsystem Routing</h3>

<table>
  <thead>
    <tr>
      <th align="left">Subsystem / Device</th>
      <th align="left">Data Output Type</th>
      <th align="left">Wavelength Allocation (Tx / Rx)</th>
      <th align="left">Intermediate Conversion</th>
      <th align="left">Primary Optical Link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Allied Vision Mako G-234C (Cam 1)</b></td>
      <td>Copper Gigabit Ethernet</td>
      <td>Tx 1470 nm / Rx 1490 nm</td>
      <td>SFP Media Converter</td>
      <td>CWDM Multiplexer &rarr; OptiLink J2</td>
    </tr>
    <tr>
      <td><b>Allied Vision Mako G-234C (Cam 2)</b></td>
      <td>Copper Gigabit Ethernet</td>
      <td>Tx 1510 nm / Rx 1530 nm</td>
      <td>SFP Media Converter</td>
      <td>CWDM Multiplexer &rarr; OptiLink J2</td>
    </tr>
    <tr>
      <td><b>Sonar / Data Switch Bus</b></td>
      <td>RS-232 / Copper Ethernet</td>
      <td>Tx 1590 nm / Rx 1610 nm</td>
      <td>Moxa Server &rarr; SFP Converter</td>
      <td>CWDM Multiplexer &rarr; OptiLink J2</td>
    </tr>
  </tbody>
</table>

<br>
<hr>
<br>

<a name="ethernet-schematics"></a>
<h2>2. Ethernet Electrical Schematic & Internal Switch Routing</h2>

<p>Routing across dual Ethernet switches inside the Electronics Bottle handles internal data switching, diagnostic test ports, and subsea 13-pin connector breakouts (Data1Net and Data2Net).</p>

<div align="center">
<img width="1276" height="841" alt="Ethernet Pinout" src="https://github.com/user-attachments/assets/511180be-6801-4f53-931a-c948b1439548" />
  <p><i>Figure 2.1: Dual Switch Ethernet Architecture & Subsea Pinout Breakout.</i></p>
</div>

<br>

<h3>Switch Port Assignment Matrix</h3>

<table>
  <thead>
    <tr>
      <th align="left">Switch Unit</th>
      <th align="left">Port</th>
      <th align="left">Target Network Line</th>
      <th align="left">Destination / Assigned Function</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Ethernet Switch #1</b><br>(Ubiquiti 60-105-ProSafe)</td>
      <td>Eth1<br>Eth2<br>Eth3<br>Eth4<br>Eth5</td>
      <td>Moxa1 Net<br>Moxa2 Net<br>Timing Net<br>Unused<br>Inter Net</td>
      <td>Moxa Serial Server Interface #1<br>Moxa Serial Server Interface #2<br>Precision Timing / Sync Network<br>Terminated / Spare<br>Inter-switch trunk line to Switch #2 (Eth1)</td>
    </tr>
    <tr>
      <td><b>Ethernet Switch #2</b><br>(Ubiquiti 60-105-ProSafe)</td>
      <td>Eth1<br>Eth2<br>Eth3<br>Eth4<br>Eth5</td>
      <td>Inter Net<br>Data1 Net<br>Data2 Net<br>Test Net<br>Data Net</td>
      <td>Trunk link from Switch #1 (Eth5)<br>SubConn 13-pin Connector (Data1Net)<br>SubConn 13-pin Connector (Data2Net)<br>Internal L-com RJ45 Test Jack (ECF504-8SA)<br>Central Data Bus</td>
    </tr>
  </tbody>
</table>

<br>
<hr>
<br>

<a name="bulkhead-specs"></a>
<h2>3. Bulkhead Connector Specifications & Pinout Reference</h2>

<p>Master technical specifications for all SubConn bulkhead connectors installed on the Electronics Bottle endcaps.</p>

<div align="center">
<img width="1270" height="829" alt="Bulkhead Pinouts" src="https://github.com/user-attachments/assets/6d8d0149-95b8-44a0-a048-a19b268fa883" />
  <p><i>Figure 3.1: SubConn Bulkhead Face Views and Hardware Specifications.</i></p>
</div>

<br>

<h3>Bulkhead Hardware & Pinout Specifications</h3>

<ul>
  <li><b>3-Pin AC Input Bulkhead (J1):</b>
    <ul>
      <li><b>Hardware Spec:</b> SubConn MCBH3M-SS | <b>Thread:</b> 7/16-20 UNF-2A | <b>O-Ring:</b> 2-014</li>
      <li><b>Pinout:</b> Pin 1: Ground Return | Pin 2: AC (Hot) | Pin 3: AC (Neutral)</li>
    </ul>
  </li>
  <li><b>4-Pin Strobe Bulkheads (J5–J8):</b>
    <ul>
      <li><b>Hardware Spec:</b> SubConn MCBH4M-SS | <b>Thread:</b> 7/16-20 UNF-2A | <b>O-Ring:</b> 2-014</li>
      <li><b>Pinout:</b> Pin 1: Strobe Signal Return | Pin 2: Strobe Signal | Pin 3: AC (Hot) | Pin 4: AC (Neutral)</li>
      <li><b>Power Rating:</b> MVS-5002 Strobe (12V @ 4.5A) & fan (12V @ 0.5A) via Astrodyne LPR75-12 (75W total).</li>
    </ul>
  </li>
  <li><b>6-Pin Serial Bulkheads (J11–J22):</b>
    <ul>
      <li><b>Hardware Spec:</b> SubConn MCBH6M-SS | <b>Thread:</b> 7/16-20 UNF-2A | <b>O-Ring:</b> 2-014</li>
      <li><b>Pinout:</b> Pin 1: Power Return | Pin 2: Power Output #1 | Pin 3: Power Output #2 | Pin 4: Instrument Rx (Tx by Moxa) | Pin 5: Instrument Tx (Rx by Moxa) | Pin 6: Comms Return</li>
      <li><b>Power Limits (Per Port):</b> 100W @ 48V (2A), 75W @ 24V (3A), 35W @ 12V (3A), 15W @ 5V (3A).</li>
      <li><b>Total Serial Bus Power Available:</b> 100W (48V), 90W (24V), 100W (12V), 70W (5V).</li>
    </ul>
  </li>
  <li><b>13-Pin Ethernet / Camera Bulkheads (J3, J4, J9, J10):</b>
    <ul>
      <li><b>Hardware Spec:</b> SubConn DBH13M-SS | <b>Thread:</b> 1/2-20 UNF-2A | <b>O-Ring:</b> 2-015</li>
      <li><b>Camera Pinout (J3, J4):</b> Pin 1: Camera Return | Pin 3: Strobe Signal | Pins 4–11: Ethernet Color Pairs | Pin 12: Camera Power | Pin 13: Strobe Return</li>
      <li><b>Ethernet Pinout (J9, J10):</b> Pins 1–3: Power Conductors (#18 BLK, #18 ORN, #18 WHT) | Pins 4–11: Cat6 Ethernet Pairs | Pins 12–13: Main Power Rails (#18 RED, #18 GRN)</li>
    </ul>
  </li>
  <li><b>SubConn OptiLink Fiber Bulkhead (J2):</b>
    <ul>
      <li><b>Hardware Spec:</b> SubConn OptiLink A-04-BCR | <b>Thread:</b> 7/8-14 | <b>O-Rings:</b> 2-019 & 2-022</li>
      <li><b>Capacity:</b> 4 Single-Mode (SM) Optical Fiber channels.</li>
    </ul>
  </li>
</ul>

<br>
<hr>
<br>

<a name="fiber-cabling"></a>
<h2>4. Electronics Bottle Internal Fiber Cabling</h2>

<p>Details internal optical media conversion, CWDM wavelength multiplexing, and fiber pass-through routing inside the Electronics Bottle to bridge copper Ethernet devices to the SubConn OptiLink subsea bulkhead.</p>

<div align="center">
<img width="1280" height="880" alt="Bottle Fiber Cabling" src="https://github.com/user-attachments/assets/5123f9c5-6b91-48be-9f4a-656a459024e3" />
  <p><i>Figure 4.1: Internal Optical Media Conversion & CWDM Routing.</i></p>
</div>

<br>

<h3>Fiber Channel Routing Map</h3>

<table>
  <thead>
    <tr>
      <th align="left">Channel Source</th>
      <th align="left">Input Protocol</th>
      <th align="left">Optical Transceiver</th>
      <th align="left">CWDM LC Port Wavelengths</th>
      <th align="left">Barrel Coupling</th>
      <th align="left">SubConn OptiLink Pin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Camera 1 Ethernet</b></td>
      <td>RJ45 Copper</td>
      <td>Aaxeon SFP-C 1490</td>
      <td>Tx 1470 nm / Rx 1490 nm</td>
      <td>ST-to-ST Barrel 1 (FOA-011A)</td>
      <td>Fiber 1</td>
    </tr>
    <tr>
      <td><b>Camera 2 Ethernet</b></td>
      <td>RJ45 Copper</td>
      <td>Aaxeon SFP-C 1490</td>
      <td>Tx 1510 nm / Rx 1530 nm</td>
      <td>ST-to-ST Barrel 2 (FOA-011A)</td>
      <td>Fiber 2</td>
    </tr>
    <tr>
      <td><b>Sonar Ethernet</b></td>
      <td>RJ45 Copper</td>
      <td>Aaxeon SFP-C 1490</td>
      <td>Tx 1570 nm / Rx 1550 nm</td>
      <td>ST-to-ST Barrel 3 (FOA-011A)</td>
      <td>Fiber 3</td>
    </tr>
    <tr>
      <td><b>Data Net Ethernet</b></td>
      <td>RJ45 Copper</td>
      <td>Aaxeon SFP-C 1490</td>
      <td>Tx 1610 nm / Rx 1590 nm</td>
      <td>ST-to-ST Barrel 4 (FOA-011A)</td>
      <td>Fiber 4</td>
    </tr>
  </tbody>
</table>

<br>
<hr>
<br>

<a name="endcap-placements"></a>
<h2>5. Bottle Endcap Connector Placements & Designation Maps</h2>

<p>External bulkhead connector placements, designations, part numbers, and gender specifications for both the Electronics Bottle and Expansion Bottle.</p>

<div align="center">
<img width="1258" height="819" alt="Endcap Connector Placement" src="https://github.com/user-attachments/assets/100949ed-dd02-4bee-9d20-c77d0e01dbc9" />
  <p><i>Figure 5.1: Electronics Bottle Front and Back Endcap Bulkhead Layouts.</i></p>
</div>

<br>

<h3>Electronics Bottle Bulkhead Assignments</h3>

<table>
  <thead>
    <tr>
      <th align="left">Port Designation</th>
      <th align="left">Assigned Function</th>
      <th align="left">Endcap Location</th>
      <th align="left">SubConn Bulkhead Part</th>
      <th align="left">Mating Cable Plug</th>
      <th align="left">Pin / Fiber Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>J1</b></td>
      <td>AC Power Input</td>
      <td>Front Endcap</td>
      <td>MCBH3M-SS</td>
      <td>MCIL3F</td>
      <td>3 Pins</td>
    </tr>
    <tr>
      <td><b>J2</b></td>
      <td>Main Fiber Input</td>
      <td>Front Endcap</td>
      <td>OptiLink A-04-BCR</td>
      <td>OptiLink Plug</td>
      <td>4 SM Fibers</td>
    </tr>
    <tr>
      <td><b>J3, J4</b></td>
      <td>Camera #1, Camera #2</td>
      <td>Front Endcap</td>
      <td>DBH13M-SS</td>
      <td>DIL13F</td>
      <td>13 Pins</td>
    </tr>
    <tr>
      <td><b>J5–J8</b></td>
      <td>Strobe #1 through #4</td>
      <td>Front Endcap</td>
      <td>MCBH4M-SS</td>
      <td>MCIL4F</td>
      <td>4 Pins</td>
    </tr>
    <tr>
      <td><b>J9, J10</b></td>
      <td>Ethernet #1, Ethernet #2</td>
      <td>Back Endcap</td>
      <td>DBH13M-SS</td>
      <td>DIL13F</td>
      <td>13 Pins</td>
    </tr>
    <tr>
      <td><b>J11–J22</b></td>
      <td>Serial Ports #1 through #12</td>
      <td>Back Endcap</td>
      <td>MCBH6M-SS</td>
      <td>MCIL6F</td>
      <td>6 Pins</td>
    </tr>
    <tr>
      <td><b>J50–J52</b></td>
      <td>Direct Optical ST Ports</td>
      <td>Front Endcap</td>
      <td>Lancer 500-BST-S1-B02-000</td>
      <td>ST-Dry Penetrator</td>
      <td>Single ST Fiber</td>
    </tr>
  </tbody>
</table>

<br>

<div align="center">
<img width="1248" height="818" alt="Expansion Connector Placement" src="https://github.com/user-attachments/assets/88d9ceb8-bf1a-4be6-ab0d-6c3839617479" />
  <p><i>Figure 5.2: Expansion Bottle Endcap Bulkhead Layout.</i></p>
</div>

<br>

<h3>Expansion Bottle Bulkhead Assignments</h3>

<table>
  <thead>
    <tr>
      <th align="left">Port Designation</th>
      <th align="left">Assigned Subsystem</th>
      <th align="left">SubConn Bulkhead Part</th>
      <th align="left">Mating Cable Plug</th>
      <th align="left">Pin Count & Gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>J1</b></td>
      <td>AC Power In</td>
      <td>MCBH3F-SS</td>
      <td>MCIL3M</td>
      <td>3 Pins (Female Bulkhead)</td>
    </tr>
    <tr>
      <td><b>J2</b></td>
      <td>Data Net In</td>
      <td>DBBH13F-SS</td>
      <td>DIL13M</td>
      <td>13 Pins (Female Bulkhead)</td>
    </tr>
    <tr>
      <td><b>J3</b></td>
      <td>Ethernet #2</td>
      <td>DBBH13M-SS</td>
      <td>DIL13F</td>
      <td>13 Pins (Male Bulkhead)</td>
    </tr>
    <tr>
      <td><b>J4</b></td>
      <td>BlueView Sonar</td>
      <td>DBBH13M-SS</td>
      <td>DIL13F</td>
      <td>13 Pins (Male Bulkhead)</td>
    </tr>
    <tr>
      <td><b>J5</b></td>
      <td>Ethernet #3</td>
      <td>DBBH13M-SS</td>
      <td>DIL13F</td>
      <td>13 Pins (Male Bulkhead)</td>
    </tr>
    <tr>
      <td><b>J6</b></td>
      <td>Unused / Spare Port</td>
      <td>DBBH13M-SS</td>
      <td>DIL13F</td>
      <td>13 Pins (Male Bulkhead)</td>
    </tr>
    <tr>
      <td><b>J7–J11</b></td>
      <td>Serial #1 through #5</td>
      <td>MCBH8F-SS</td>
      <td>MCIL8M</td>
      <td>8 Pins (Female Bulkhead)</td>
    </tr>
  </tbody>
</table>

<br>
<hr>
<br>

<a name="serial-ports"></a>
<h2>6. Serial Instrumentation Port Arrays (INST 1–12)</h2>

<p>Internal power distribution buses, Moxa N-Port serial server interfaces, and pin routings for auxiliary instrumentation ports INST 1 through INST 12 (J11–J22) inside the Electronics Bottle.</p>

<div align="center">
<img width="1258" height="845" alt="Serial Ports 1-6" src="https://github.com/user-attachments/assets/bb949343-5088-4895-a99a-dc1299498ed3" />
  <p><i>Figure 6.1: Electrical Schematic for Serial Ports 1 through 6 (J11–J16).</i></p>
</div>

<br>

<div align="center">
<img width="1256" height="822" alt="Serial Ports 7-12" src="https://github.com/user-attachments/assets/c347ac8f-e320-4614-9705-0043876eb87d" />
  <p><i>Figure 6.2: Electrical Schematic for Serial Ports 7 through 12 (J17–J22).</i></p>
</div>

<br>

<h3>Serial Port Wiring & Terminal Block Matrix</h3>

<table>
  <thead>
    <tr>
      <th align="left">Instrument Port</th>
      <th align="left">Back Endcap Port</th>
      <th align="left">Moxa Server & DB9 Connector</th>
      <th align="left">Power Bus Terminal Blocks</th>
      <th align="left">SubConn MCBH6M Pin Allocation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>INST 1</b></td>
      <td>J11</td>
      <td>Moxa Server #1 (Port 1 / J38)</td>
      <td>Terminal Block T5</td>
      <td>Pin 1: Power Return (BLK #22)<br>Pin 2: Power Output #1 (WHT #22)<br>Pin 3: Power Output #2 (RED #22)<br>Pin 4: Instrument Rx / Moxa Tx (GRN #22)<br>Pin 5: Instrument Tx / Moxa Rx (ORG #22)<br>Pin 6: Comms Return (BLU #22)</td>
    </tr>
    <tr>
      <td><b>INST 2–6</b></td>
      <td>J12–J16</td>
      <td>Moxa Server #1 (Ports 2–6 / J39–J43)</td>
      <td>Terminal Blocks T6–T10</td>
      <td>Identical 6-pin wiring structure to INST 1</td>
    </tr>
    <tr>
      <td><b>INST 7</b></td>
      <td>J17</td>
      <td>Moxa Server #2 (Port 1 / J44)</td>
      <td>Terminal Block T11</td>
      <td>Identical 6-pin wiring structure to INST 1</td>
    </tr>
    <tr>
      <td><b>INST 8–12</b></td>
      <td>J18–J22</td>
      <td>Moxa Server #2 (Ports 2–6 / J45–J49)</td>
      <td>Terminal Blocks T12–T16</td>
      <td>Identical 6-pin wiring structure to INST 1</td>
    </tr>
  </tbody>
</table>

<br>
<hr>
<br>

<a name="ac-power-strobes"></a>
<h2>7. AC Power Distribution & MVS 5000 Strobe Controls</h2>

<p>Governs high-voltage AC input distribution, internal DC power generation (5V, 12V, 24V, 48V), system cooling fans, camera power control, and flash pulse triggers for four MVS 5000 strobe units.</p>

<div align="center">
<img width="1254" height="834" alt="AC Power" src="https://github.com/user-attachments/assets/c943e173-9c90-4b22-b80e-8f91a35f3040" />
  <p><i>Figure 7.1: AC Power Distribution, Rectifiers, and Strobe Control Schematic.</i></p>
</div>

<br>

<h3>Internal Rectifiers & Interface Allocation</h3>

<ul>
  <li><b>AC Main Input (J1):</b> High-voltage AC enters via SubConn MCBH3M-SS with a 4A slow-blow fuse (F1: Littelfuse 03540821ZXBL) guarding the main AC rails.</li>
  <li><b>Internal DC Regulators:</b>
    <ul>
      <li><b>PS1 (Astrodyne RS150-48):</b> Generates +48V DC (Fused via F2 @ 1A Fast) &rarr; Terminal Strip T1.</li>
      <li><b>PS2 (Astrodyne RS150-24):</b> Generates +24V DC (Fused via F3 @ 1A Fast) &rarr; Terminal Strip T2.</li>
      <li><b>PS3 (Astrodyne RS150-12):</b> Generates +12V DC (Fused via F2-3 @ 8A Fast) &rarr; Terminal Strip T3.</li>
      <li><b>PS4 (Astrodyne RS100-5):</b> Generates +5V DC (Fused via F4-5 @ 8A Fast) &rarr; Terminal Strip T4.</li>
    </ul>
  </li>
  <li><b>System Cooling:</b> Dual Mechatronics GDA6025-12BB 12V cooling fans equipped with tachometer feedback lines.</li>
  <li><b>Timing Unit (U1):</b> Sealevel CC320 timing interface on the Timing Net with optical trigger outputs (Out1–Out8) pulled up via 1.2k&Omega; resistors.</li>
</ul>

<br>

<h3>Strobe & Camera Bulkhead Connections</h3>

<table>
  <thead>
    <tr>
      <th align="left">Port Name</th>
      <th align="left">Endcap Port</th>
      <th align="left">SubConn Model</th>
      <th align="left">Assigned Function</th>
      <th align="left">Pin Allocation Callouts</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>STR-1</b></td>
      <td>J5</td>
      <td>MCBH4M-SS</td>
      <td>Strobe Unit #1 Power & Trigger</td>
      <td>Pin 1: Strobe Return (#20 BLK)<br>Pin 2: Strobe Signal (#20 WHT)<br>Pin 3: AC Hot (#20 RED)<br>Pin 4: AC Neutral (#20 GRN)</td>
    </tr>
    <tr>
      <td><b>STR-2, 3, 4</b></td>
      <td>J6, J7, J8</td>
      <td>MCBH4M-SS</td>
      <td>Strobe Units #2, #3, #4 Power & Trigger</td>
      <td>Identical 4-pin mapping to STR-1</td>
    </tr>
    <tr>
      <td><b>CAM-1</b></td>
      <td>J3</td>
      <td>DBH13M-SS</td>
      <td>Main Camera #1 Interface</td>
      <td>Pin 1: Camera Return (#18 BLK)<br>Pin 3: Strobe Signal (#18 WHT)<br>Pins 5–11: Cam1 Ethernet (#24 Pairs)<br>Pin 12: Camera Power (#18 RED)<br>Pin 13: Strobe Return (#18 GRN)</td>
    </tr>
    <tr>
      <td><b>CAM-2</b></td>
      <td>J4</td>
      <td>DBH13M-SS</td>
      <td>Main Camera #2 Interface</td>
      <td>Identical 13-pin mapping to CAM-1</td>
    </tr>
  </tbody>
</table>

<br>
<hr>
<br>

<a name="subsystem-housings"></a>
<h2>8. Sensor Bottles, Strobe Units & Camera Housings</h2>

<h3>8.1 Strobe Bottle Internal Schematic</h3>

<div align="center">
<img width="1234" height="838" alt="Strobe Bottle" src="https://github.com/user-attachments/assets/16c26846-5ed4-4318-ac23-aa0c5d430d06" />
  <p><i>Figure 8.1: WHOI Strobe Bottle Internal Electrical Schematic.</i></p>
</div>

<br>

<p>Details AC power conversion, thermal regulation, opto-isolated trigger pulse amplification, and driving circuit connections for the Perkin-Elmer MVS-5002 strobe unit:</p>
<ul>
  <li><b>Internal Power Converter (PS1):</b> Astrodyne LPR75-12 converting high-voltage AC into regulated +12V DC.</li>
  <li><b>Trigger Conditioning:</b> Dual NPN transistors (Q1, Q2 2N3904) driving a Perkin-Elmer MVS-5002 optocoupler stage with a 150&Omega; current-limiting resistor. Nominal trigger: 5V @ 20mA (4.5V @ 18mA minimum).</li>
  <li><b>Internal Cooling:</b> Sunon KDE1206PHV2 12V fan drawing air out through housing side vents.</li>
</ul>

<br>

<h3>8.2 Attitude Bottle Internal Schematic</h3>

<div align="center">
<img width="1226" height="827" alt="Attitude Bottle" src="https://github.com/user-attachments/assets/eac244c8-2b77-4025-a97c-7e7b2bc27c7c" />
  <p><i>Figure 8.2: WHOI Attitude Bottle (Microstrain 3DM-GX3-25 IMU) Schematic.</i></p>
</div>

<br>

<table>
  <thead>
    <tr>
      <th align="left">Bulkhead Pin (SubConn MCBH4M-SS J1)</th>
      <th align="left">Assigned Signal</th>
      <th align="left">Wire Specification</th>
      <th align="left">Sensor Connector (P2) & Function (U1)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Pin 1</b></td>
      <td>Power Return</td>
      <td>20 AWG Violet</td>
      <td>Pin 9 / Pin 6 (Power Ground)</td>
    </tr>
    <tr>
      <td><b>Pin 2</b></td>
      <td>+12V Power Input</td>
      <td>20 AWG Green</td>
      <td>Pin 8 (+5–16V Power Input)</td>
    </tr>
    <tr>
      <td><b>Pin 3</b></td>
      <td>RS232 Out From Housing</td>
      <td>20 AWG Yellow</td>
      <td>Pin 4 (RS232 Transmit - Tx)</td>
    </tr>
    <tr>
      <td><b>Pin 4</b></td>
      <td>RS232 In To Housing</td>
      <td>20 AWG Orange</td>
      <td>Pin 5 (RS232 Receive - Rx)</td>
    </tr>
  </tbody>
</table>

<br>

<h3>8.3 Camera Synchronization Bus Circuit Analysis</h3>

<div align="center">
<img width="1206" height="804" alt="Camera Trigger" src="https://github.com/user-attachments/assets/8be62985-f4e8-4581-846c-8b9f9c71552a" />
  <p><i>Figure 8.3: Optically Isolated Shared Camera / Strobe Synchronization Bus.</i></p>
</div>

<br>

<ul>
  <li><b>Bus Bias:</b> Single 2050&Omega; (0.5W) pull-up resistor to +24V DC in the Electronics Bottle.</li>
  <li><b>Active Low State (Trigger Pulled Low):</b> Line near 0V; 11.7mA through pull-up resistor; 0mA through camera LEDs; 0.3mA through each strobe; total collector sinking current = 12.9mA.</li>
  <li><b>Inactive High State (Floating High):</b> Line at 3.4V; 10.1mA through pull-up resistor; 5.3mA through each camera input LED (exceeds drive threshold).</li>
  <li><b>Worst-Case Single Camera Load:</b> Single-camera / 4-strobe line rises to 5.0V, delivering 9.5mA to the camera LED.</li>
</ul>

<br>

<h3>8.4 Allied Vision Mako G-234C Camera Housing Wiring</h3>

<div align="center">
<img width="1195" height="883" alt="Camera Wiring" src="https://github.com/user-attachments/assets/1d0c551d-283e-417a-8295-8503d2ee9ade" />
  <p><i>Figure 8.4: Allied Vision Mako G-234C Camera Housing Electrical Wiring Diagram.</i></p>
</div>

<br>

<table>
  <thead>
    <tr>
      <th align="left">Vehicle Bulkhead Port (SubConn DBH13MSS J1)</th>
      <th align="left">Wire Color / Spec</th>
      <th align="left">Internal Target / Power PCB (1A1)</th>
      <th align="left">Camera Receptacle (Hirose HR25-7TR-8PA)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Pin 1</b></td>
      <td>Black (#18)</td>
      <td>Power PCB 1A1P1 Pin 1 (GND)</td>
      <td>Hirose Pin 4 (SyncIn 1 Gnd) & Pin 5 (Sync Gnd)</td>
    </tr>
    <tr>
      <td><b>Pin 12</b></td>
      <td>Red (#18)</td>
      <td>Power PCB 1A1P1 Pin 2 (+12V DC)</td>
      <td>Hirose Pin 7 (+12V Power)</td>
    </tr>
    <tr>
      <td><b>Pin 3</b></td>
      <td>White (#18)</td>
      <td>Power PCB 1A1P1 Pin 4 (SYNC IN)</td>
      <td>Optical Trigger Input Line</td>
    </tr>
    <tr>
      <td><b>Pin 13</b></td>
      <td>Green (#18)</td>
      <td>Power PCB 1A1P1 Pin 3 (SYNC GND)</td>
      <td>Optical Trigger Return Line</td>
    </tr>
    <tr>
      <td><b>Pins 4–11</b></td>
      <td>Cat6 Ethernet Pairs</td>
      <td>Aaxeon FCU3002A Media Converter</td>
      <td>Gigabit Ethernet Port (PoE Capable)</td>
    </tr>
    <tr>
      <td><b>Optical Output (J2)</b></td>
      <td>ST-Dry Penetrator</td>
      <td>Lancer 500-BST-S1-B02</td>
      <td>Aaxeon SFP Module (Tx 1550 nm / Rx 1310 nm)</td>
    </tr>
  </tbody>
</table>

<br>
<hr>
<br>

<a name="sensor-cables"></a>
<h2>9. CTD & Environmental Sensor Cable Harnesses</h2>
<img width="1234" height="881" alt="CTD Wiring" src="https://github.com/user-attachments/assets/e79fb571-f2c0-4c4f-bfd4-d1134a0c35e7" />
<h3>9.1 Sea-Bird SBE 37 / SBE 49 CTD Cable Assembly</h3>

<div align="center">

  <p><i>Figure 9.1: Sea-Bird SBE 37/49 CTD Sensor Cable Schematic.</i></p>
</div>

<br>

<table>
  <thead>
    <tr>
      <th align="left">SubConn MCIL4F Pin (SBE CTD Side)</th>
      <th align="left">Wire Color</th>
      <th align="left">Signal Function</th>
      <th align="left">SubConn MCIL6F Pin (HabCam Side)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Pin 1</b></td>
      <td>Black</td>
      <td>Power Ground</td>
      <td>Pin 1 & Pin 6 (Ground)</td>
    </tr>
    <tr>
      <td><b>Pin 2</b></td>
      <td>White</td>
      <td>RS-232 Rx (Connects to HabCam Tx)</td>
      <td>Pin 5 (Orange Wire - RS-232 Tx)</td>
    </tr>
    <tr>
      <td><b>Pin 3</b></td>
      <td>Red</td>
      <td>RS-232 Tx (Connects to HabCam Rx)</td>
      <td>Pin 4 (Green Wire - RS-232 Rx)</td>
    </tr>
    <tr>
      <td><b>Pin 4</b></td>
      <td>Green</td>
      <td>9–24V DC Operating Power</td>
      <td>Pin 2 (White Wire - 9–24V DC)</td>
    </tr>
  </tbody>
</table>

<br>

<h3>9.2 ECO-Triplet Fluorometer Cable Assembly</h3>

<div align="center">
<img width="1234" height="881" alt="Eco-Triplet Wiring" src="https://github.com/user-attachments/assets/b112bbf6-75a1-43c8-b4a5-00ff100705ca" />

  <p><i>Figure 9.2: Sea-Bird / WET Labs ECO-Triplet Cable Schematic.</i></p>
</div>

<br>

<table>
  <thead>
    <tr>
      <th align="left">SubConn MCIL6F Pin (ECO-Triplet Side)</th>
      <th align="left">Wire Color</th>
      <th align="left">Signal Function</th>
      <th align="left">SubConn MCIL6F Pin (Bottle / INST 4 Side)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Pin 1</b></td>
      <td>Black</td>
      <td>Power Ground</td>
      <td>Pin 1 (Black Wire - Ground)</td>
    </tr>
    <tr>
      <td><b>Pin 2</b></td>
      <td>White</td>
      <td>RS-232 Rx</td>
      <td>Pin 4 (Green Wire - RS-232 XMT)</td>
    </tr>
    <tr>
      <td><b>Pin 3</b></td>
      <td>Red</td>
      <td>Not Used (N/U)</td>
      <td>Pin 2 (White Wire - Open / N/U)</td>
    </tr>
    <tr>
      <td><b>Pin 4</b></td>
      <td>Green</td>
      <td>+12V DC Operating Power</td>
      <td>Pin 3 (Red Wire - +12V DC)</td>
    </tr>
    <tr>
      <td><b>Pin 5</b></td>
      <td>Orange</td>
      <td>RS-232 Tx</td>
      <td>Pin 5 (Orange Wire - RS-232 Rx)</td>
    </tr>
    <tr>
      <td><b>Pin 6</b></td>
      <td>Blue</td>
      <td>Analog #1 (N/U)</td>
      <td>Pin 6 (Blue Wire - RS-232 Rx)</td>
    </tr>
  </tbody>
</table>

<br>
<hr>

</div>

<div align="center">

# HabCam Vehicle Sensor Preparation & Assembly Protocols

<img width="369" height="491" alt="Habcam in Tank" src="https://github.com/user-attachments/assets/bfd3aa9e-db54-4ff7-903f-41e80b910eb6" />
<p><i>HabCam Vehicle Submerged in Sundance Tank for Camera Calibration</i></p>

</div>

<br>

<h2>Master Subsystem & Mounting Summary</h2>

<table>
  <thead>
    <tr>
      <th align="left">Subsystem</th>
      <th align="left">Mounting Location</th>
      <th align="left">Required Hardware & Fasteners</th>
      <th align="left">Required Tools</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="#electronics-bottle"><b>Electronics Bottle</b> *(1x)*</a></td>
      <td>Aft Vehicle Frame</td>
      <td>• (4x) Black Aluminum Brackets<br>• (4x) Barrier Rubber Pieces (Pliobond 35 glued)<br>• (8x) 9/16"-12 (3 ½") Partial Thread Bolts<br>• (8x) 9/16"-12 (2 ¼") Partial Thread Bolts<br>• (4x) 32" 11mm Fully Threaded Rods<br>• (6x) Plastic Washers, (10x) Steel Washers<br>• (8x) Steel Lock Nuts, (8x) Hex Nuts</td>
      <td>• 9/16" Socket & Wrench<br>• 7/16" Wrench<br>• 14mm Wrench</td>
    </tr>
    <tr>
      <td><a href="#blueview-sonar"><b>BlueView Sonar</b> *(1x)*</a></td>
      <td>Forward Vehicle Frame</td>
      <td>• (4x) Steel Brackets<br>• (4x) Barrier Rubber Pieces<br>• (6x) 9/16"-12 (3 ½") Steel Partial Thread Bolts<br>• (4x) 9/16"-12 (2 ¼") Steel Partial Thread Bolts<br>• (20x) 3/16" Steel Washers<br>• (10x) Steel Lock Nuts, (10x) Hex Nuts</td>
      <td>• 9/16" Socket & Wrench<br>• 14mm Wrench<br>• Aqua Shield Grease</td>
    </tr>
    <tr>
      <td><a href="#ctd-39-dissolved-oxygen"><b>CTD 39 Oxygen</b> *(1x)*</a></td>
      <td>Starboard Forward Rail</td>
      <td>• (2x) UHMW Brackets, (2x) Plastic Brackets<br>• (4x) Barrier Rubber Pieces<br>• (4x) 7/16"-14 (4 ¾") Steel Partial Thread Bolts<br>• (2x) 7/16"-14 (1") Steel Full Thread Bolts<br>• (3x) 3/16" (1") Socket Head Screws<br>• (10x) Steel Washers, (6x) Lock Nuts, (2x) Hex Nuts</td>
      <td>• 7/16" Socket & Wrench<br>• 11mm Wrench<br>• Hex Key Set (1/4"–1/16")</td>
    </tr>
    <tr>
      <td><a href="#ctd-49-sound-speed"><b>CTD 49 Sound Speed</b> *(1x)*</a></td>
      <td>Port Forward Rail</td>
      <td>• (6x) Plastic Brackets (Sensor, Center, Frame)<br>• (8x) Barrier Rubber Pieces<br>• (8x) 9/16"-12 (2 ¾") Steel Partial Thread Bolts<br>• (16x) Steel Washers<br>• (8x) Steel Lock Nuts, (8x) Hex Nuts</td>
      <td>• 9/16" Socket & Wrench<br>• 14mm Wrench</td>
    </tr>
    <tr>
      <td><a href="#eco-triplet-puck"><b>Eco-Triplet Puck</b> *(1x)*</a></td>
      <td>Center Forward Expansion Rail</td>
      <td>• (2x) Steel Brackets (Top & Bottom)<br>• (2x) Barrier Rubber Pieces<br>• (2x) 9/16"-12 (2 ½") Steel Partial Thread Bolts<br>• (2x) 9/16"-12 (2") Steel Partial Thread Bolts<br>• (6x) Steel Washers, (4x) Lock Nuts, (2x) Hex Nuts</td>
      <td>• 9/16" Socket & Wrench<br>• 14mm Wrench</td>
    </tr>
    <tr>
      <td><a href="#habitat-cameras"><b>Habitat Cameras</b> *(2x)*</a></td>
      <td>Center Frame Plate</td>
      <td>• (1x) Steel Mounting Plate (16 in x 16 in)<br>• (6x) Metal Brackets<br>• (4x) M7-1.0 x 45mm Threaded Bolts<br>• (4x) 1/4"-20 (2") Socket Head Screws<br>• (8x) 1/4"-20 (1") Socket Head Screws<br>• (6x) Steel Washers, (6x) Steel Lock Nuts</td>
      <td>• Hex Key Set (1/4"–1/16")<br>• M7 / 3/16" Allen Keys</td>
    </tr>
    <tr>
      <td><a href="#strobe-lights"><b>Strobe Lights</b> *(4x)*</a></td>
      <td>Forward, Aft, Port, Starboard</td>
      <td>• (8x) Steel Brackets<br>• (8x) Barrier Rubber Pieces<br>• (8x) 9/16"-12 (3 ½") Steel Partial Thread Bolts<br>• (8x) 7/16"-14 (1 ¾") Steel Partial Thread Bolts<br>• (32x) Plastic Washers, (32x) Steel Washers<br>• (16x) Steel Lock Nuts, (16x) Hex Nuts</td>
      <td>• 9/16" Socket & Wrench<br>• 7/16" Socket & Wrench<br>• 14mm / 11mm Wrenches</td>
    </tr>
    <tr>
      <td><a href="#attitude-sensor"><b>Attitude Sensor</b> *(1x)*</a></td>
      <td>Internal Housing Chassis</td>
      <td>• Housing Mounting Brackets & Isolation Collars<br>• Stainless Steel Attachment Fasteners</td>
      <td>• Standard Wrench & Socket Set</td>
    </tr>
    <tr>
      <td><a href="#altimeter"><b>Sonar Altimeter</b> *(1x)*</a></td>
      <td>Center Camera Plate</td>
      <td>• (2x) Plastic Brackets<br>• (4x) Barrier Rubber Pieces<br>• (4x) 9/16"-12 (6 ½") Steel Partial Thread Bolts<br>• (8x) Steel Washers<br>• (4x) Steel Lock Nuts, (4x) Hex Nuts</td>
      <td>• 9/16" Socket & Wrench<br>• 14mm Wrench</td>
    </tr>
  </tbody>
</table>

<br>
<hr>
<br>

<h2>Detailed Subsystem Preparation, Mounting & Technical Specifications</h2>

<a name="blueview-sonar"></a>
<h3>BlueView Forward Looking Sonar (1x)</h3>

<div align="center">
  <img width="530" height="705" alt="BlueView" src="https://github.com/user-attachments/assets/992d102a-c524-457e-b3f7-2bba977efd09" />
  <br><br>
<img width="367" height="335" alt="BlueView" src="https://github.com/user-attachments/assets/2a63bea3-015d-4956-b9bb-948f54804023" />
</div>

<br>

<p><b>Hardware Inventory:</b></p>
<ul>
  <li>(4x) Steel Brackets</li>
  <li>(4x) Barrier Rubber Pieces</li>
  <li>(6x) 9/16”-12 (3 ½”) Steel Partial Thread Hex Bolts</li>
  <li>(4x) 9/16”-12 (2 ¼”) Steel Partial Thread Hex Bolts</li>
  <li>(20x) 3/16" Steel Washers</li>
  <li>(10x) Steel Lock Nuts</li>
  <li>(10x) 9/16”-12 Steel Hex Nuts</li>
</ul>

<p><b>Tools Needed:</b></p>
<ul>
  <li>9/16" Socket Wrench</li>
  <li>9/16" Combination Wrench</li>
  <li>14mm Combination Wrench (Optional)</li>
  <li>Aqua Shield Grease</li>
</ul>

<p><b>System Overview:</b> A forward-facing sonar (forward-looking sonar or forward imaging sonar) is designed to provide high-resolution imaging of the underwater environment in front of a vessel or vehicle. Unlike traditional sonar systems that measure depth directly below or capture data in a single direction, forward-facing sonar scans the area ahead to detect obstacles, submerged structures, and features during poor visibility, night operations, or turbid water surveys. Widely used in navigation, underwater inspections, search-and-rescue, and operations in complex marine environments.</p>

<p><b>Sonar Preparation & Mounting Steps:</b></p>
<ol>
  <li>Prior to attaching BlueView to the front of the vehicle, ensure the bracket has rubber gaskets glued to them (brackets should already be attached to the HabCam vehicle).</li>
  <li>Attach BlueView to the bracket, with the Impulse connector facing towards the back of the vehicle.</li>
  <li>Thread four stainless steel screws through the bracket.</li>
  <li>Prior to adding the stainless steel washer, lock washer, and nut, apply Aqua Shield over all of the threads (there should be 4 screws).</li>
  <li>Add the stainless steel washer, lock washer, and nut to all four screws (washer on inside, lock washer in middle, nut on outside).</li>
  <li>Use 9/16" ratcheting wrenches to tighten the nuts.</li>
</ol>

<br>

<h4>Teledyne Marine BlueView M450 Mk2 System Specifications</h4>

<table>
  <thead>
    <tr>
      <th align="left">Parameter</th>
      <th align="left">Specification</th>
      <th align="left">Parameter</th>
      <th align="left">Specification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Operating Frequency</b></td>
      <td>450 kHz</td>
      <td><b>Supply Voltage</b></td>
      <td>12–28 VDC</td>
    </tr>
    <tr>
      <td><b>Field of View</b></td>
      <td>130&deg;</td>
      <td><b>Max Power Consumption</b></td>
      <td>24 W</td>
    </tr>
    <tr>
      <td><b>Max Range</b></td>
      <td>300 m (984 ft)</td>
      <td><b>Connectivity</b></td>
      <td>Ethernet</td>
    </tr>
    <tr>
      <td><b>Optimum Range</b></td>
      <td>2–150 m (6.5–197 ft)</td>
      <td><b>Connector</b></td>
      <td>Impulse MKS(W) Splash-mate (standard); Impulse MKS, Burton (optional)</td>
    </tr>
    <tr>
      <td><b>Beam Width (Horizontal / Vertical)</b></td>
      <td>1&deg; / 10&deg;</td>
      <td><b>Range Resolution</b></td>
      <td>50.8 mm (2.0 in)</td>
    </tr>
    <tr>
      <td><b>Number of Beams (Maximum)</b></td>
      <td>768 (0.18&deg; beam spacing)</td>
      <td><b>Update Rate</b></td>
      <td>Up to 20 Hz</td>
    </tr>
  </tbody>
</table>

<br>

<h4>BlueView Mechanical Options</h4>

<table>
  <thead>
    <tr>
      <th align="left">Version</th>
      <th align="left">Depth Rating</th>
      <th align="left">Dimensions (L &times; W)</th>
      <th align="left">Can Diameter</th>
      <th align="left">Weight (Air / Water)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>BlueView M450 S Mk2</b></td>
      <td>1,000 m</td>
      <td>203.4 mm (8.0 in) &times; 195.6 mm (7.7 in)</td>
      <td>&Oslash;101.6 mm (4.0 in)</td>
      <td>3.5 kg / 1.6 kg</td>
    </tr>
    <tr>
      <td><b>BlueView M450 D6 Mk2</b></td>
      <td>6,000 m</td>
      <td>253.7 mm (10.0 in) &times; 195.6 mm (7.7 in)</td>
      <td>&Oslash;127.0 mm (5.0 in)</td>
      <td>8.5 kg / 5.5 kg</td>
    </tr>
  </tbody>
</table>

<br>
<hr>
<br>

<a name="ctd-39-dissolved-oxygen"></a>
<h3>CTD-39 Dissolved Oxygen Sensor (Optional) (1x)</h3>

<div align="center">
  <img width="530" height="708" alt="CTD-39" src="https://github.com/user-attachments/assets/2b06c7c3-7110-4aab-bc1d-03d5f765ab2b" />
  <br><br>
<img width="255" height="418" alt="CTD-39" src="https://github.com/user-attachments/assets/001241a7-8ec2-4cf6-b888-7d988b748afb" />
</div>

<br>

<p><b>Hardware Inventory:</b></p>
<ul>
  <li>(2x) UHMW Brackets</li>
  <li>(2x) Plastic Brackets</li>
  <li>(4x) Barrier Rubber Pieces</li>
  <li>(4x) 7/16”-14 (4 ¾”) Steel Partial Thread Hex Bolts</li>
  <li>(2x) 7/16”-14 (1”) Steel Full Thread Hex Bolts</li>
  <li>(3x) 3/16” (1”) Steel Socket Head Screws Full Thread</li>
  <li>(10x) Steel Washers</li>
  <li>(6x) Steel Lock Nuts</li>
  <li>(2x) 7/16”-14 Steel Hex Nuts</li>
</ul>

<p><b>Tools Needed:</b></p>
<ul>
  <li>7/16" Socket Wrench</li>
  <li>7/16" Combination Wrench</li>
  <li>11mm Combination Wrench (Optional)</li>
  <li>Hex Key Set (1/4"–1/16")</li>
</ul>

<p><b>System Overview:</b> The SBE 39plus is a high-accuracy, fast-sampling temperature (pressure optional) recorder with USB interface, internal batteries, and onboard memory. Designed for moorings or long-duration fixed-site deployments, as well as nets, towed vehicles, or ROVs. Memory capacity exceeds 9.5 million samples excluding pressure data, or 5.5 million samples including pressure. Sampling every 0.5 sec yields approximately 55 days of data without pressure or 32 days with pressure (battery endurance exceeds memory capacity).</p>

<p><b>CTD Preparation Steps:</b></p>
<ol>
  <li>Prior to attaching Seabird 39 CTD to the Starboard forward vertical frame rail, ensure bracket has rubber gaskets glued to them (brackets should already be attached to HabCam vehicle).</li>
  <li>Attach Seabird 39 CTD to the bracket, with the bulkhead connector facing down by threading screw through bracket.</li>
  <li>Prior to adding stainless steel washer, lock washer, and nut, apply Aqua Shield over all of the threads (there should be 4 screws).</li>
  <li>Add the stainless steel washer, lock washer, and nut to all four screws (washer on inside, lock washer in middle, nut on outside).</li>
  <li>Use 7/16" ratcheting wrenches to tighten the nuts.</li>
</ol>

<br>

<h4>Sea-Bird Scientific SBE 39plus System Specifications</h4>

<table>
  <thead>
    <tr>
      <th align="left">Parameter</th>
      <th align="left">Specification</th>
      <th align="left">Parameter</th>
      <th align="left">Specification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Communication Options</b></td>
      <td>RS-232</td>
      <td><b>Sampling Rate</b></td>
      <td>Up to 2 Hz (2 samples/sec)</td>
    </tr>
    <tr>
      <td><b>Depth Rating</b></td>
      <td>600 m</td>
      <td><b>Memory Capacity</b></td>
      <td>9.5 million samples T; 5.5 million samples TD</td>
    </tr>
    <tr>
      <td><b>Power Source</b></td>
      <td>Internal, External</td>
      <td><b>Power Consumption</b></td>
      <td>Lithium battery pack (4 AA Saft LS 14500): > 11,000,000 samples TD</td>
    </tr>
    <tr>
      <td><b>Housing Material Options</b></td>
      <td>Plastic, Titanium</td>
      <td><b>Accuracy</b></td>
      <td>Temperature: &plusmn;0.002 &deg;C (-5 to +35 &deg;C); &plusmn;0.01 &deg;C (+35 to +45 &deg;C)<br>Optional Pressure: &plusmn;0.1% of full scale range</td>
    </tr>
    <tr>
      <td><b>Onboard Memory</b></td>
      <td>Yes</td>
      <td><b>Resolution</b></td>
      <td>Temperature: 0.0001 &deg;C<br>Optional Pressure: 0.002% of full scale range</td>
    </tr>
    <tr>
      <td><b>Connector</b></td>
      <td>MCBH</td>
      <td><b>Software / Biofouling</b></td>
      <td>Seasoft V2 | Biofouling Protection: No</td>
    </tr>
  </tbody>
</table>

<p><b>Documentation Links:</b></p>
<ul>
  <li><a href="https://www.seabird.com/hubfs/Product%20Assets/SBE%2039plus/SBE%2039plus%20Datasheets.zip?hsLang=en" target="_blank">SBE 39plus DataSheet Zip</a></li>
  <li><a href="https://www.seabird.com/hubfs/Product%20Assets/SBE%2039plus/Manuals/39plusrevB.pdf?hsLang=en" target="_blank">SBE 39plus Manual (Rev B)</a></li>
  <li><a href="https://www.seabird.com/hubfs/Product%20Assets/SBE%2039plus/Methods-Procedures/SBE%2039%20Methods-Procedures.zip?hsLang=en" target="_blank">SBE 39 Methods and Procedures Zip</a></li>
  <li><a href="https://www.seabird.com/hubfs/Product%20Assets/SBE%2039plus/Configurations/SBE%2039plus%20Configurations%20Overview.pdf?hsLang=en" target="_blank">SBE 39plus Configurations Overview</a></li>
</ul>

<br>
<hr>
<br>

<a name="ctd-49-sound-speed"></a>
<h3>CTD-49 Sound Speed Sensor (1x)</h3>

<div align="center">
  <img width="537" height="715" alt="CTD-49" src="https://github.com/user-attachments/assets/acfb146e-98b2-4127-ae30-f809362fa6a9" />
  <br><br>
<img width="286" height="431" alt="CTD-49" src="https://github.com/user-attachments/assets/1e25bb83-d045-4f3b-a1d8-018db19d76be" />
</div>

<br>

<p><b>Hardware Inventory:</b></p>
<ul>
  <li>(6x) Plastic Brackets</li>
  <li>(8x) Barrier Rubber Pieces</li>
  <li>(8x) 9/16”-12 (2 ¾”) Steel Partial Thread Hex Bolts</li>
  <li>(16x) Steel Washers</li>
  <li>(8x) Steel Lock Nuts</li>
  <li>(8x) 9/16”-12 Steel Hex Nuts</li>
</ul>

<p><b>Tools Needed:</b></p>
<ul>
  <li>9/16" Socket Wrench</li>
  <li>9/16" Combination Wrench</li>
  <li>14mm Combination Wrench (Optional)</li>
</ul>

<p><b>System Overview:</b> The SBE 49 FastCAT is an integrated CTD sensor intended for use as a modular component in towed vehicles, ROVs, AUVs, or other autonomous platforms that supply DC power and acquire serial data. It is an easy-to-use, light, and compact instrument suited to small vehicle payloads. FastCAT must be externally powered, and its RS-232C data saved or telemetered by the vehicle. It does not support auxiliary sensors directly. FastCAT's pump-controlled, TC-ducted flow feature minimizes salinity spiking, and its 16 Hz sampling provides very high spatial resolution of oceanographic structures and gradients. Measured data and derived variables of salinity and sound velocity are output in real-time in engineering units or raw HEX.</p>

<p><b>CTD Preparation Steps:</b></p>
<ol>
  <li>Prior to attaching Seabird 49 CTD to Port forward vertical frame rail, ensure bracket has rubber gaskets glued to them (brackets should already be attached to HabCam vehicle).</li>
  <li>Attach Seabird 49 CTD to the bracket, with the pump facing down by threading screw through bracket.</li>
  <li>Prior to adding stainless steel washer, lock washer, and nut, apply Aqua Shield over all of the threads (there should be 4 screws).</li>
  <li>Add the stainless-steel washer, lock washer, and nut to all four screws (washer on inside, lock washer in middle, nut on outside).</li>
  <li>Use 9/16" ratcheting wrenches to tighten the nuts.</li>
</ol>

<br>

<h4>Sea-Bird Scientific SBE 49 FastCAT CTD System Specifications</h4>

<table>
  <thead>
    <tr>
      <th align="left">Parameter</th>
      <th align="left">Specification</th>
      <th align="left">Parameter</th>
      <th align="left">Specification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Communication Options</b></td>
      <td>RS-232C</td>
      <td><b>Sampling Rate</b></td>
      <td>16 Hz (16 samples/sec)</td>
    </tr>
    <tr>
      <td><b>Depth Rating</b></td>
      <td>350 m</td>
      <td><b>Power Consumption</b></td>
      <td>Input: 0.75 A @ 9–24 VDC<br>Turn-on transient: 750 mA<br>Sampling/transmitting (with pump): 350 mA @ 9V, 285 mA @ 12V, 180 mA @ 19V</td>
    </tr>
    <tr>
      <td><b>Power Source</b></td>
      <td>External</td>
      <td><b>Accuracy</b></td>
      <td>Conductivity: &plusmn;0.0003 S/m<br>Temperature: &plusmn;0.002 &deg;C<br>Pressure: &plusmn;0.1% of full scale range</td>
    </tr>
    <tr>
      <td><b>Housing Material Options</b></td>
      <td>Plastic, Titanium</td>
      <td><b>Resolution</b></td>
      <td>Conductivity: 0.00005 S/m (0.4 ppm salinity)<br>Temperature: 0.0001 &deg;C<br>Pressure: 0.002% of full scale range</td>
    </tr>
    <tr>
      <td><b>Connector</b></td>
      <td>MCBH</td>
      <td><b>Software / Biofouling</b></td>
      <td>Seasoft V2 | Biofouling Protection: Yes</td>
    </tr>
  </tbody>
</table>

<p><b>Documentation Links:</b></p>
<ul>
  <li><a href="https://www.seabird.com/hubfs/Product%20Assets/SBE%2049/Datasheets/SBE%2049DS53May25.pdf?hsLang=en" target="_blank">SBE 49 DataSheet PDF</a></li>
  <li><a href="https://www.seabird.com/hubfs/Product%20Assets/SBE%2049/Manuals/SBE%2049%20Manuals.zip?hsLang=en" target="_blank">SBE 49 Manuals Zip</a></li>
  <li><a href="https://www.seabird.com/hubfs/Product%20Assets/SBE%2049/Methods-Procedures/SBE%2049%20Methods-Procedures.zip?hsLang=en" target="_blank">SBE 49 Methods and Procedures Zip</a></li>
</ul>

<br>
<hr>
<br>

<a name="eco-triplet-puck"></a>
<h3>Eco-Triplet Puck - Fluorometer (1x)</h3>

<div align="center">
  <img width="546" height="727" alt="Eco-Triplet" src="https://github.com/user-attachments/assets/55354b6d-fcf0-46a6-9249-841b3b7e2f9f" />
  <br><br>
  <img width="377" height="283" alt="Eco-Triplet" src="https://github.com/user-attachments/assets/99503384-5829-41c4-948e-aae78b8727f1" />
</div>

<br>

<p><b>Hardware Inventory:</b></p>
<ul>
  <li>(2x) Steel Brackets</li>
  <li>(2x) Barrier Rubber Pieces</li>
  <li>(2x) 9/16”-12 (2 ½”) Steel Partial Thread Hex Bolts</li>
  <li>(2x) 9/16”-12 (2”) Steel Partial Thread Hex Bolts</li>
  <li>(6x) Steel Washers</li>
  <li>(4x) Steel Lock Nuts</li>
  <li>(2x) 9/16”-12 Steel Hex Nuts</li>
</ul>

<p><b>Tools Needed:</b></p>
<ul>
  <li>9/16" Socket Wrench</li>
  <li>9/16" Combination Wrench</li>
  <li>14mm Combination Wrench (Optional)</li>
</ul>

<p><b>System Overview:</b> The next generation of optical monitoring with Sea-Bird Scientific's cutting-edge ECO V2 Series. Offers dynamic range transitioning from deep blue ocean to coastal waters. Delivers 16-bit resolution and enhanced signal-to-noise ratios across up to four channels. Ideal for biological monitoring and dye trace studies. Robust potted optics block ensures long-term sensor stability. Optional anti-biofouling technology enables extended field measurements.</p>

<p><b>Fluorometer Preparation Steps:</b></p>
<ol>
  <li>Prior to attaching Eco-Triplet Puck to Center Forward Horizontal expansion bottle rails, ensure the bracket has rubber gaskets glued to them (brackets should already be attached to HabCam vehicle).</li>
  <li>Attach Eco-Triplet to the bracket, with the bulkhead connector facing towards the center of HabCam and resting above the crossbar, by threading screw through bracket.</li>
  <li>Prior to adding the stainless-steel washer, lock washer and nut, apply Aqua Shield over all of the threads (there should be 2 screws).</li>
  <li>Add the stainless-steel washer, lock washer, and nut to both screws (washer on inside, lock washer in middle, nut on outside).</li>
  <li>Use 9/16" ratcheting wrenches to tighten the nuts.</li>
</ol>

<br>

<h4>HabCam Sensor Configuration (Model BBFL2, Serial Number: 627)</h4>
<p><i>Configured via joint agreement between Population Dynamics Branch and Oceanography Branch.</i></p>

<table>
  <thead>
    <tr>
      <th align="left">Channel</th>
      <th align="left">Measurement Parameter</th>
      <th align="left">Wavelength</th>
      <th align="left">Sensitivity</th>
      <th align="left">Typical Range</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Channel 1</b></td>
      <td>Scattering (NTU)</td>
      <td>650 nm</td>
      <td>~0.003 m<sup>-1</sup></td>
      <td>0–5 m<sup>-1</sup></td>
    </tr>
    <tr>
      <td><b>Channel 2</b></td>
      <td>Chlorophyll (EX/EM)</td>
      <td>695 nm</td>
      <td>0.025 &mu;g/l</td>
      <td>0–50 &mu;g/l</td>
    </tr>
    <tr>
      <td><b>Channel 3</b></td>
      <td>fDOM</td>
      <td>460 nm</td>
      <td>0.28 ppb/count</td>
      <td>0–375 ppb</td>
    </tr>
  </tbody>
</table>

<br>

<h4>Sea-Bird Scientific ECO V2 Optical Sensor System Specifications</h4>

<table>
  <thead>
    <tr>
      <th align="left">Parameter</th>
      <th align="left">Specification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Communication Options</b></td>
      <td>RS-232, Analog</td>
    </tr>
    <tr>
      <td><b>Depth Rating</b></td>
      <td>600 m, 2,000 m, 6,000 m</td>
    </tr>
    <tr>
      <td><b>Power Source</b></td>
      <td>Internal, External</td>
    </tr>
    <tr>
      <td><b>Housing Material Options</b></td>
      <td>Aluminum, Titanium, ABS, Acetal, Copolymer</td>
    </tr>
    <tr>
      <td><b>Connector</b></td>
      <td>MCBH-6M</td>
    </tr>
    <tr>
      <td><b>Sampling Rate</b></td>
      <td>User-selectable to 8 Hz</td>
    </tr>
    <tr>
      <td><b>Memory Capacity</b></td>
      <td>1 Ch: 1,048,000 samples | 2 Ch: 762,000 | 3 Ch: 599,000 | 4 Ch: 493,000</td>
    </tr>
    <tr>
      <td><b>Software / Biofouling</b></td>
      <td>UCI | Biofouling Protection: Yes</td>
    </tr>
  </tbody>
</table>

<p><b>Documentation Links:</b></p>
<ul>
  <li><a href="https://www.seabird.com/hubfs/Product%20Assets/ECO%20V2/Datasheets/ECO%20V2%20Single%20Channel.DS.53.Feb26%202.zip?hsLang=en" target="_blank">ECO V2 Single Channel DataSheet Zip</a></li>
  <li><a href="https://www.seabird.com/hubfs/Product%20Assets/ECO%20V2/Manuals/ECO%20V2%20Manuals.zip?hsLang=en" target="_blank">ECO V2 Manuals Zip</a></li>
</ul>

<br>
<hr>
<br>

<a name="electronics-bottle"></a>
<h3>Main Electronics Bottle - WHOI Engineered (1x)</h3>

<div align="center">
  <img width="530" height="705" alt="Bottle" src="https://github.com/user-attachments/assets/becf982a-6b5f-41b3-9888-0379a8ec98e3" />
  <br><br>
  <!-- Secondary Installed Photo Space -->
  [DROP ELECTRONICS BOTTLE MOUNTED / EXTRA PHOTO HERE]
</div>

<br>

<p><b>Hardware Inventory:</b></p>
<ul>
  <li>(4x) Black Aluminum Brackets</li>
  <li>(4x) Barrier Rubber Pieces</li>
  <li>(8x) 9/16”-12 (3 ½”) Steel Partial Thread Hex Bolts</li>
  <li>(8x) 9/16”-12 (2 ¼”) Steel Partial Thread Hex Bolts</li>
  <li>(4x) 32" 11mm Fully Threaded Rods</li>
  <li>(6x) Plastic Washers</li>
  <li>(10x) 3/16" Steel Washers</li>
  <li>(8x) Steel Lock Nuts</li>
  <li>(8x) 9/16”-12 Steel Hex Nuts</li>
</ul>

<p><b>Tools Needed:</b></p>
<ul>
  <li>9/16" Socket Wrench</li>
  <li>9/16" Combination Wrench</li>
  <li>7/16" Socket Wrench</li>
  <li>14mm Combination Wrench (Optional)</li>
  <li>3/16" Hex Wrench</li>
  <li>Small Phillips Screwdriver</li>
  <li>Rubber Mallet</li>
  <li>Multimeter</li>
  <li>Molykote 55 Grease & Dielectric Grease</li>
  <li>Pliobond 35 Rubber Adhesive</li>
  <li>Aqua Shield Grease</li>
  <li>Vacuum Pump Fixture</li>
</ul>

<p><b>Main Electronics Bottle Removal, Disassembly, Maintenance & Reassembly Procedure:</b></p>

<ol>
  <li>Before removing the main electronics bottle from HabCam, ensure it is powered off.</li>
  <li>Disconnect all cables from bulkhead connectors on both sides of the main electronics bottle.</li>
  <li>Remove main bottle top clamps with 9/16" ratcheting wrench.</li>
  <li>Place the main bottle cradle on the table.</li>
  <li>Two people are needed to gently remove the main bottle from HabCam. One person climbs on top of the vehicle and gently slides the main bottle out of the back of the vehicle. The second person holds the weight in the back. Then both carry the bottle to the cradle.</li>
<div align="center">
  <img width="294" height="386" alt="Bottle on Vehicle" src="https://github.com/user-attachments/assets/37a206ef-fe0c-4f86-9049-5bb45f1032bb" />
</div>
  <li>
        Check the condition of top and bottom clamps on HabCam. If replacement is needed due to wear/damage, remove brackets from HabCam using 9/16" ratcheting wrenches.
  </li>
  <li>If replacing the main electronics bottle clamp, ensure rubber is applied to the inside of the clamp before reattaching to HabCam. Rubber can be attached to clamps using Pliobond 35.</li>
<div align="center">
  <img width="437" height="327" alt="Bottle on Stand" src="https://github.com/user-attachments/assets/c61f26e2-d5b0-4072-8585-55aafc8ec513" />
</div>
  <li>
    To open the main electronics bottle, remove threaded rods along the outside of the main bottle using 7/16" ratcheting wrenches (there should be 4 of them).
  </li>
  <div align="center">
  <img width="380" height="285" alt="Pressure Portjpg" src="https://github.com/user-attachments/assets/a7c11ff6-0d0d-4f92-89c1-5e08a0ffdd6d" /> 
  </div>
    <li>
     Use a 3/16" hex wrench to pop-out the vacuum purge plug on the back of the main bottle. You should hear air escape upon loosening if it has not been opened since coming back from the field.
  </li>
  <li>Remove the end cap on the forward end cap (opposite side of the purge plug). There should be a label that says "open this end first". This end is opened first as it is NOT connected to the electronics chassis.</li>
<div align="center">
<img width="210" height="345" alt="Bottle Stood Up" src="https://github.com/user-attachments/assets/0d90fe47-1f67-49d7-9f84-21594386fce9" />
<img width="465" height="357" alt="Inside Removed" src="https://github.com/user-attachments/assets/f829341b-0336-4250-bdca-83b2eb8ef16a" /> 
</div>  
  <li>Use a rubber mallet to lightly bang on the back end of the cap's lip to loosen it.</li>
  <li>To remove the forward end cap, unplug ethernet cables, two mini amp-style and the 3 large amp-style connectors. Now take the cap completely out; when setting it down avoid bending the bulkheads as much as feasibly possible.</li>
  </li>
    Use a mallet on the opposite cap's rim to loosen it from housing. Once loose, set on a soft pad on the floor upright with that cap facing upward, remove it with the electronic housing, and place it on the cradle.
  </li>
 <div align="center">
<img width="340" height="255" alt="Prototype Board Removal 1" src="https://github.com/user-attachments/assets/27a6a393-9064-48cc-886a-dad14a4b6a94" />
<img width="359" height="255" alt="Prototype Board Removal 2" src="https://github.com/user-attachments/assets/3e755bea-2450-4c32-85ac-5ac57245c2a7" />
</div> 
  <li>
      On the underside of the main bottle, there is a removable prototype board, attached with screws. Using a small Phillips screwdriver, remove the screws from the standoffs. Take the plate off and replace the desiccant packs with fresh ones (4 large packs).
  </li>
 <div align="center">
  <img width="348" height="463" alt="Fuses" src="https://github.com/user-attachments/assets/5d447f9f-20b8-4905-891b-a75f1440743f" /> 
  </div>
  <li>
    Check the suite of fuses to ensure they are properly connected with a multimeter. Set multimeter to continuity mode; you should hear a beep if connected properly.
  </li>
  <li>Turn on the vehicle by plugging in 3-pin power cable and fiber optic bulkhead (currently using Port 3). On the step-up transformer, turn on input, then output (in that order).</li>
  <li>Check that you can connect to both Moxas, both Guardasofts, and whatever sensors are plugged into the bottle (i.e. attitude sensor).</li>
  <li>If working, turn off main bottle by turning off output, then input on step-up transformer. Unplug 3-pin power cable and fiber optic bulkhead.</li>
  <li>Add a cap to the fiberoptic bulkhead on the main bottle to protect it from scratches.</li>
  <li>Check if desiccant needs replaced. Attach 4 packets to underside of prototype board using painter's tape. Recommended replacement is once a year.</li>
  <li>Reattach prototype board to standoffs.</li>
  <li>Prior to reattaching housing, slip off O-rings on back end cap, wipe off excess grease, apply isopropyl alcohol to paper towel and quickly wipe down O-rings. Do not over apply alcohol as it eats through rubber.</li>
  <li>Gently check O-rings for nicks or cuts, and apply an even coat of Molykote 55.</li>
  <li>Apply an even coat of Molykote 55 to inside edge of housing that meets back end cap O-rings when assembled.</li>
  <li>To reassemble main electronics bottle, gently invert inside of main bottle and hover over housing, ensuring nothing is pinched as you close. Requires substantial pressure to snap closed.</li>
  <li>On front end cap, remove O-rings, wipe off excess grease, apply isopropyl alcohol to paper towel and quickly wipe down O-rings.</li>
  <li>Flip electronics bottle and apply even coat of Molykote 55 to inside edge of housing meeting front end cap O-rings.</li>
  <li>Before attaching front end cap, plug in ethernet cables, two mini amp-style and 3 large amp-style into respective ports.</li>
  <li>Hover end cap over housing, ensuring nothing is pinched as you close. Align handles and rod holes as close as possible; press firmly until snapped closed.</li>
  <li>Turn on vehicle by plugging in 3-pin power cable and fiber optic bulkhead (Port 3). On step-up transformer, turn on input, then output. Listen for beep (if purge plug is out). Verify link light and attitude output on Engineering GUI.</li>
  <li>If reporting well, power down by turning off output, then input on step-up transformer. Unplug 3-pin power cable and fiber optic bulkhead.</li>
  <li>Before pulling a vacuum, ensure rod holes are aligned.</li>
  <li>To pull a vacuum, attach vacuum plug to purge plug port. Attach hose to pump and turn pump on. Shut off valve at 16 inHg of mercury, then shut off pump.</li>
  <li>Wait 24 hours, and confirm that pressure is still held at 16 inHg.</li>
  <li>Check handle integrity, replace if necessary.</li>
  <li>To secure main electronics bottle clamps, thread a 2.5" partially threaded screw through plastic insert. Apply Aqua Shield over all threads prior to adding stainless washer, lock washer, and nut.</li>
  <li>Apply dielectric grease to female end of connector faces of camera cable and strobe. Listen for cracking sound as you align male and female connectors. Hand-tighten locking collars across all front/back connectors.</li>
  <li>Ensure all desired sensors work by turning on vehicle (3-pin power and fiber optic bulkhead Port 3; step-up transformer input then output).</li>
</ol>

<br>
<hr>
<br>

<a name="habitat-cameras"></a>
<h3>Allied Vision Mako G-234 - Cameras (2x)</h3>

<div align="center">
  <img width="549" height="732" alt="Camera" src="https://github.com/user-attachments/assets/d41133ad-3292-487d-b2d3-f8a05d4d4eb6" />
  <br><br>
<table>
  <tr>
    <td align="center">
    <img width="268" height="357" alt="Cameras" src="https://github.com/user-attachments/assets/15046f46-832a-4a6c-8822-df73dc632499" />
      <br>
      <b>Camera Housings & Frame Mount</b>
    </td>
    <td align="center">
     <img width="272" height="363" alt="Cameras2" src="https://github.com/user-attachments/assets/4891c4b5-c245-49cb-945a-9c27ddfc3d75" />
      <br>
      <b>Down-Looking Stereo Optical Ports</b>
    </td>
  </tr>
</table>

</div>
</div>

<br>

<p><b>Hardware Inventory:</b></p>
<ul>
  <li>(1x) Steel Mounting Plate (16 in &times; 16 in)</li>
  <li>(6x) Steel Brackets</li>
  <li>(4x) 1/4”-20 (2”) Steel Socket Head Screws Partial Thread</li>
  <li>(8x) 1/4”-20 (1”) Steel Socket Head Screws Full Thread</li>
  <li>(6x) Steel Washers</li>
  <li>(6x) Steel Lock Nuts</li>
</ul>

<p><b>Tools Needed:</b></p>
<ul>
  <li>Hex Key Set (1/4"–1/16")</li>
</ul>

<p><b>System Overview:</b> Mako G-234 is a 2.35 megapixel GigE machine vision camera incorporating a high quality Type 1/1.2 (13.4 mm diagonal) Sony IMX249 CMOS sensor. At full resolution, this camera runs 41.5 frames per second (10-bit sensor readout). Higher frame rates are possible with a smaller region of interest (ROI).</p>

<br>

<h4>Allied Vision Mako G-234 System Specifications</h4>

<table>
  <thead>
    <tr>
      <th align="left">Parameter</th>
      <th align="left">Specification</th>
      <th align="left">Parameter</th>
      <th align="left">Specification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Resolution</b></td>
      <td>1,936 &times; 1,216 (2.40 MP)</td>
      <td><b>Sensor Size</b></td>
      <td>11.34 mm &times; 7.13 mm (13.4 mm, Type 1/1.2)</td>
    </tr>
    <tr>
      <td><b>Framerate</b></td>
      <td>41 fps</td>
      <td><b>Pixel Size</b></td>
      <td>5.86 &mu;m &times; 5.86 &mu;m</td>
    </tr>
    <tr>
      <td><b>Digital Interface</b></td>
      <td>IEEE 802.3 1000BASE-T, IEEE 802.3af (PoE)</td>
      <td><b>Exposure Time</b></td>
      <td>16 &mu;s to 85 s</td>
    </tr>
    <tr>
      <td><b>Sensor Type / Arch</b></td>
      <td>Area Scan | CMOS</td>
      <td><b>Image Buffer (RAM)</b></td>
      <td>64 MByte</td>
    </tr>
    <tr>
      <td><b>Sensor Model / Shutter</b></td>
      <td>Sony IMX249 | Global Shutter (GS)</td>
      <td><b>Power Supply</b></td>
      <td>10.8 to 26.4 VDC AUX or 802.3at Type 1 PoE</td>
    </tr>
  </tbody>
</table>

<p><b>Documentation Link:</b> <a href="https://www.alliedvision.com/pdf/datasheet/1080?locale=en_US" target="_blank">Allied Vision Mako G-234 DataSheet PDF</a></p>

<br>
<hr>
<br>

<a name="strobe-lights"></a>
<h3>Arctic Rays (INKFISH) Dragonfish - Mini LED Strobe Lights (4x)</h3>

<div align="center">
  <img width="550" height="734" alt="Strobes" src="https://github.com/user-attachments/assets/4cb76693-0378-47cd-b581-d94f0644c457" />
  <br><br>
 <table>
  <tr>
    <td align="center">
       <img width="248" height="331" alt="Strobes" src="https://github.com/user-attachments/assets/00d58e56-ecb2-4a5e-9865-89c963b7a129" />
      <br>
      <b>Rear Bracket Mount & Cable Harness</b>
    </td>
    <td align="center">
      <img width="248" height="331" alt="Strobes2" src="https://github.com/user-attachments/assets/9b5cff3d-c6b1-4bf9-8485-b99f6a23bfc9" />
      <br>
      <b>Front LED Array & Housing Assembly</b>
    </td>
  </tr>
</table>
</div>

<br>

<p><b>Hardware Inventory:</b></p>
<ul>
  <li>(8x) Steel Brackets</li>
  <li>(8x) Barrier Rubber Pieces</li>
  <li>(8x) 9/16”-12 (3 ½”) Steel Partial Thread Hex Bolts</li>
  <li>(8x) 7/16”-14 (1 ¾”) Steel Partial Thread Hex Bolts</li>
  <li>(32x) Plastic Washers</li>
  <li>(32x) Steel Washers</li>
  <li>(16x) Steel Lock Nuts</li>
  <li>(16x) 9/16”-12 Steel Hex Nuts</li>
</ul>

<p><b>Tools Needed:</b></p>
<ul>
  <li>9/16" Socket Wrench</li>
  <li>9/16" Combination Wrench</li>
  <li>7/16" Socket Wrench</li>
  <li>7/16" Combination Wrench</li>
  <li>14mm Combination Wrench (Optional)</li>
  <li>11mm Combination Wrench (Optional)</li>
</ul>

<p><b>System Overview:</b> High-output, 30,000-lumen compact LED strobe light rated down to 6,000 meters for HOV/ROV/AUV digital still photography or wherever high-output compact strobes are required.</p>

<p><b>Patented Driver Technology Features:</b></p>
<ul>
  <li>Extremely compact package with integral driver electronics</li>
  <li>Wide-flood or focused-beam options</li>
  <li>Simple trigger-controlled pulse length</li>
  <li>Fast repetition rate</li>
  <li>Optional independent secondary quench line</li>
  <li>Customizable color temperature, pulse intensity, rep rate, and max pulse duration</li>
</ul>

<br>

<h4>Dragonfish Mini Technical Specifications</h4>

<table>
  <thead>
    <tr>
      <th align="left">Category</th>
      <th align="left">Parameter</th>
      <th align="left">Specification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Optical</b></td>
      <td>Operating Mode<br>Color Channels<br>Luminous Output<br>Color Temperature<br>CRI<br>Beam Angle (FWHM)</td>
      <td>Pulsed Strobe<br>One<br>30,000 Lm @ 5,700K<br>2700K, 3000K, 3500K, 4000K, 5700K standard, 6500K<br>70 min. Standard (optional 80 min, 90 min)<br>100&deg; standard (65&deg; optional)</td>
    </tr>
    <tr>
      <td><b>Electrical</b></td>
      <td>Voltage<br>Power<br>Max Input Current<br>Pulse Duration<br>Pulse Rep Rate</td>
      <td>9–35 VDC standard (other ranges optional)<br>16 W pulsed max<br>650 mA @ 24V during recharge<br>0.1–5 ms standard<br>2 Hz standard (10 Hz optional)</td>
    </tr>
    <tr>
      <td><b>Interface</b></td>
      <td>Connector<br>Control Signal</td>
      <td>SubConn MCBH4M<br>Logic Trigger, 5V TTL, active-low</td>
    </tr>
    <tr>
      <td><b>Mechanical & Env.</b></td>
      <td>Weight<br>Materials<br>Depth Rating<br>Temperatures</td>
      <td>In Air: 350g | In Water: 175g<br>6061-T6 Aluminum Housing, Acrylic Window<br>300 m (984 ft)<br>-10 &deg;C to 40 &deg;C operating | -25 &deg;C to 85 &deg;C storage</td>
    </tr>
  </tbody>
</table>

<p><b>Documentation Link:</b> <a href="https://www.arcticrays.com/hubfs/SpecSheets/SS_DragonFish-Mini-Strobe.pdf?hsLang=en" target="_blank">Dragonfish-Mini Strobe Spec Sheet PDF</a></p>

<br>
<hr>
<br>

<a name="attitude-sensor"></a>
<h3>Microstrain AHRS Sensor (3DM-GX5-25-HRS) - Attitude Sensor (1x)</h3>

<div align="center">
  <!-- Secondary Installed Photo Space -->
  [DROP ATTITUDE SENSOR MOUNTED / EXTRA PHOTO HERE]
</div>

<br>

<p><b>Hardware Inventory:</b></p>
<ul>
  <li>Housing Mounting Brackets & Isolation Collars</li>
  <li>Stainless Steel Attachment Fasteners</li>
</ul>

<p><b>Tools Needed:</b></p>
<ul>
  <li>Standard Wrench & Socket Set</li>
</ul>

<p><b>System Overview:</b> Industrial-grade Attitude and Heading Reference System (AHRS). Relies on internal barometric pressure sensing alongside triaxial accelerometers, gyroscopes, and magnetometers processed through an onboard Auto-Adaptive Extended Kalman Filter (EKF) to achieve high-accuracy orientation estimates (pitch, roll, yaw).</p>

<br>

<h4>Microstrain 3DM-GX5-25-HRS Specifications</h4>

<table>
  <thead>
    <tr>
      <th align="left">Parameter</th>
      <th align="left">Specification</th>
      <th align="left">Parameter</th>
      <th align="left">Specification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Mounting Style</b></td>
      <td>Chassis Mount</td>
      <td><b>Supply Voltage Min / Max</b></td>
      <td>4.25 V / 36 V</td>
    </tr>
    <tr>
      <td><b>Sensor Type</b></td>
      <td>9-axis IMU / AHRS</td>
      <td><b>Sensing Axis</b></td>
      <td>X, Y, Z</td>
    </tr>
    <tr>
      <td><b>Interface Type</b></td>
      <td>RS-232, USB</td>
      <td><b>Part Aliases</b></td>
      <td>6253-4220</td>
    </tr>
    <tr>
      <td><b>Output Type</b></td>
      <td>Digital</td>
      <td><b>Product Type</b></td>
      <td>IMUs - Inertial Measurement Units</td>
    </tr>
    <tr>
      <td><b>Resolution</b></td>
      <td>0.02 mg</td>
      <td><b>Trade Name</b></td>
      <td>MicroStrain</td>
    </tr>
    <tr>
      <td><b>Operating Temp Range</b></td>
      <td>-40 &deg;C to +85 &deg;C</td>
      <td><b>Manufacturer</b></td>
      <td>HBK / Hottinger Brüel & Kjær</td>
    </tr>
  </tbody>
</table>

<p><b>Documentation Links:</b></p>
<ul>
  <li><a href="https://www.mouser.com/datasheet/3/3764/1/3dm-gx5-25_datasheet_8400-0093_rev_o.pdf" target="_blank">Microstrain 3DM-GX5-25 DataSheet PDF</a></li>
  <li><a href="https://www.mouser.com/catalog/additional/Parker_LORD_3DM_GX5_UK_Declaration_Conformity_Rev.pdf" target="_blank">UK Declaration of Conformity Certificate</a></li>
  <li><a href="https://www.microstrain.com/sites/default/files/applications/files/3dm-gx5-25_user_manual_8500-0012_rev_d.pdf" target="_blank">3DM-GX5-25 User Manual PDF</a></li>
</ul>

<br>
<hr>
<br>

<a name="altimeter"></a>
<h3>Teledyne Benthos PSA 916 - Sonar Altimeter (1x)</h3>

<div align="center">
  <img width="557" height="743" alt="Altimeter" src="https://github.com/user-attachments/assets/968aa9ce-5334-483f-b910-758af423c30d" />
  <br><br>
<img width="289" height="385" alt="Altimeter" src="https://github.com/user-attachments/assets/535e2b61-3fd6-45ed-ab29-ec48b559df85" />
</div>

<br>

<p><b>Hardware Inventory:</b></p>
<ul>
  <li>(2x) Plastic Brackets</li>
  <li>(4x) Barrier Rubber Pieces</li>
  <li>(4x) 9/16”-12 (6 ½”) Steel Partial Thread Hex Bolts</li>
  <li>(8x) Steel Washers</li>
  <li>(4x) Steel Lock Nuts</li>
  <li>(4x) 9/16”-12 Steel Hex Nuts</li>
</ul>

<p><b>Tools Needed:</b></p>
<ul>
  <li>9/16" Socket Wrench</li>
  <li>9/16" Combination Wrench</li>
  <li>14mm Combination Wrench (Optional)</li>
</ul>

<p><b>System Overview:</b> The Teledyne PSA-916 Programmable Sonar Altimeter is a lightweight altimeter designed for marine applications. Transmits a narrow-beam acoustic signal then measures round trip travel time for sound pulses reflecting off the seabed. Knowing the nominal speed of sound in water (1,500 m/s), travel time calculates precise distance to the ocean floor. Constructed from hard anodized, marine-grade aluminum housing and electronically isolated to eliminate signal interference with host sensors. The 200 kHz operating frequency achieves accurate measurements down to 6,000 meter depths. Applications include wave height measurement, obstacle avoidance, shallow water surveys, ice thickness, sediment transport, and scour studies.</p>

<br>

<h4>Teledyne Benthos PSA 916 System Specifications</h4>

<table>
  <thead>
    <tr>
      <th align="left">Parameter</th>
      <th align="left">Specification</th>
      <th align="left">Parameter</th>
      <th align="left">Specification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Operating Frequency</b></td>
      <td>200 kHz</td>
      <td><b>Range Outputs</b></td>
      <td>Analog: 0–5 VDC | Digital: RS-232</td>
    </tr>
    <tr>
      <td><b>Beam Width</b></td>
      <td>14&deg; conical typical</td>
      <td><b>Operating Depth</b></td>
      <td>6,000 m</td>
    </tr>
    <tr>
      <td><b>Pulse Length</b></td>
      <td>250 &mu;s standard</td>
      <td><b>Power Required</b></td>
      <td>7 to 24 VDC</td>
    </tr>
    <tr>
      <td><b>Repetition Rates</b></td>
      <td>5 pps or external</td>
      <td><b>Power Consumption</b></td>
      <td>60 mA @ 15 VDC</td>
    </tr>
    <tr>
      <td><b>Range</b></td>
      <td>100 m full scale</td>
      <td><b>Size</b></td>
      <td>2.25 in. diameter &times; 9.75 in. long</td>
    </tr>
    <tr>
      <td><b>Resolution</b></td>
      <td>RS-232: 1 cm | Analog: 2.5 cm</td>
      <td><b>Weight</b></td>
      <td>In Air: 0.63 kg (1.4 lbs) | In Water: 0.36 kg (0.8 lbs)</td>
    </tr>
    <tr>
      <td><b>Required Topside Unit</b></td>
      <td>UDB-9000 Universal Deck Box</td>
      <td><b>Housing Material</b></td>
      <td>Hard Anodized Marine-Grade Aluminum</td>
    </tr>
  </tbody>
</table>

<p><b>Documentation Links:</b></p>
<ul>
  <li><a href="https://coriolix.sikuliaq.alaska.edu/media/uploads/benthos_psa-916_manual.pdf" target="_blank">Teledyne Benthos PSA-916 Manual PDF</a></li>
  <li><a href="https://cdn.prod.website-files.com/64f5b41c95d2817bbfee10e3/6516ca9e3e360549609249fe_Teledyne%20PSA916%20Altimeter.pdf" target="_blank">Teledyne PSA 916 DataSheet PDF</a></li>
</ul>

<a name="weak-link"></a>
<h2>1. Assembling the Weak Link</h2>

<p>The mechanical weak link protects the primary tow cable and ship winch from catastrophic over-tension during seafloor snags. It is installed between the towing bridle and the mechanical cable clevis[cite: 6, 8].</p>

<div align="center">
  <!-- Placeholders for Weak Link Assembly Diagrams -->
  <table>
    <tr>
      <td align="center">
        [DROP WEAK LINK EXPLODED VIEW PHOTO HERE]
        <br>
        <b>Weak Link Housing & Shear Pin Alignment</b>
      </td>
      <td align="center">
        [DROP WEAK LINK ASSEMBLED PHOTO HERE]
        <br>
        <b>Assembled Weak Link Attached to Tow Bridle</b>
      </td>
    </tr>
  </table>
</div>

<br>

<p><b>Assembly Procedure:</b></p>
<ol>
  <li>Align the large holes on the outer housing with the large holes on the padeye inner housing (bridle), positioning set screws facing upwards. Each side of the bridle and outer shell features one large hole and one small hole.</li>
  <li>Slightly lift the bridle to slip the outer shell over the inner housing.</li>
  <li>Rotate components until all matching holes align perfectly.</li>
  <li>Insert the shear pin, wiggling the bridle and outer shell until the pin slides fully into position.</li>
  <li>Ensure the shear pin is centered inside the body and sits completely flush on both sides.</li>
  <li>Using a 3mm hex bit, tighten the set screws to <b>7.8 Nm</b> to lock the pin flush. (Note: Set torque on torque wrench prior to tightening).</li>
  <li>Attach the mechanical clevis to the weak link using the primary termination bolts. Ensure the set screws remain secured and protected by a hose clamp.</li>
</ol>

<br>
<hr>
<br>

<h2>Fiber Optic Termination</h2>

<h3>Purpose</h3>

<p>Underwater fiber optic cables are used in environments where standard communication cables cannot provide the required durability, data capacity, or long-term reliability. The underwater sensors, subsea equipment, and HabCam need a cable that can handle water exposure, pulling force, bending, abrasion, pressure, and repeated deployment.</p>

<p>On the Henry B. Bigelow specifically the fiber optic cable (Run through the winch cable) is cut yearly, so a new fiber optic termination is required every time before deployment for a new survey.</p>

<h3>Hardware</h3>

<h4>Part 1: Inserting the Fiber Optic into the Clevis</h4>

<ol>
  <li>Mark and cut about 10m (33ft) off of the ship’s fiber optic cable with a grinder and cutting wheel; this process disposes of any wire that was exposed to additional stress by going up and around the hanging block. Prior to cutting, put a hose clamp just after the 33ft mark (down the wire) to ensure that the cable does not start to unwrap.</li>
  <li>After cutting the wire, leave the hose clamp on the open end and pay out enough wire length to reach into the starboard side of the ship’s CTD lab and onto a table, where the fiber optic connectors will be applied.</li>
  <li>Measure and mark 24ft from the open end. Install another hose clamp on this end.</li>
  <li>Down at the 24 ft mark, take a dremel and score the outermost shield wire. (Note: There are 3 layers of shielding).</li>
  <li>Starting from the open end, start peeling back the outer shield wire until you have reached the scored mark. Once you reach that mark, the shield wire should break off.</li>
  <li>Repeat step 5 for the remaining shield wires until the black plastic shield is exposed.</li>
  <li>Starting at the 24 ft mark, measure 12 inches up the wire and make a mark with a sharpie. (Note: This is 25 ft from open end of the cable).</li>
  <li>Remove hose clamps and insert wire through the narrow end of sandblasted clevis and pull through until the 12 inch mark is visible on the wider end of the clevis.</li>
  <li>Refasten hose clamp only at the 12 inch mark.</li>
</ol>

<br>

<h4>Part 2: Creating the Broom</h4>

<div align="center">
<img width="265" height="412" alt="Wire and Clevis" src="https://github.com/user-attachments/assets/9d3dd535-e7cc-4893-97c4-c803a8005698" />
  <p><i>Steel Armor Wire Broom Formed and Seated inside Clevis Well</i></p>
</div>

<ol>
  <li>Starting at the 24 ft mark, start peeling the strands of shield wire (all three layers) until you reach the hose clamp (12 inches up the wire).</li>
  <li>Bend each wire at a 90 degree angle against the hose clamp. Try to evenly space the wires around the cable. (All the wires will form a “broom”).</li>
  <li>The black rubber part of the cable should now be visible up to this mark.</li>
  <li>Remove the hose clamp at the 25ft mark and move it right after the smaller opening of the clevis. (This prevents the shield wires from unwinding/bird-caging up the cable).</li>
  <li>Walk the clevis out to the back deck.</li>
  <li>Install two screw eyes in the deck, 6 feet from each other.</li>
  <li>Take a 2 ft strap. Then feed a 1in diameter pin through the two holes at the opening of the clevis. Make sure one end of the strap is fed through the pin.</li>
  <li>Attach the other side of the strap to the screw eye on deck with a 5/8th shackle.</li>
  <li>Attach a Yale Grip rope line down the cable just after the clevis using several half hitches.</li>
  <li>Put a 5/8th shackle on the rope end that is going away from the open end of the cable. This shackle will attach to the ship’s manual come-along winch and pull the broom into the clevis’ well.</li>
  <li>Secure the come-along winch and place the shackle that is on the half-hitched rope (holding the cable) into the come-along wench hook. Make sure the come along, rope, and cables are arranged in a straight line.</li>
  <li>Attach the shackle to the other screw eye.</li>
  <li>Use the come along to pull down the broom into the clevis well. Try to get about 4-6 inches of broom inside the well; it is important, as we do not want the termination slipping during deployment, even with epoxy.</li>
  <li>Once the broom is fully seated in the clevis. Move and tighten the hoseclap to the cable, at the base of the clevis (end with small opening).</li>
</ol>

<h4>Part 3: Epoxy</h4>

<ol>
  <li>Hang the termination by the clevis bolt holes so that the broom is facing up.</li>
  <li>Take 15ft of Tygon tubing and slide it over the black wire. Attach the tubing to the black rubber wire, and move it so that one end of the tubing is inserted down into the epoxy well. This tubing protects the black rubber wire from trimmed metal ends, which will occur later.</li>
  <li>Try to bend the broom ends away from the Tygon tubing as much as possible, so that they will not poke into it. Note: bend the black cable at a 45 degree angle. You do not want to block the pathway of the load pin.</li>
  <li>Using splicing tape, followed by electrical tape, create a reservoir around 2-3 in high around the openings of the clevis, where the broom becomes exposed.</li>
  <li>At this time, place newspaper or cardboard underneath where the clevis is hanging to prevent any epoxy mixture from spilling onto the ship’s floors.</li>
  <li>You will need gloves, Socketfast resin and its catalyst, a zip tie, and a long wooden mixing stick. Put on your gloves, take your catalyst and pour it into the Socketfast resin. Immediately take a wooden mixing stick and mix epoxy thoroughly for at least 2 minutes; The resin container should feel warm.</li>
  <li>Then, carefully pour epoxy into the clevis well until the mixture comes up to the top of the duct tape reservoir. Use a funnel if there is one available. A zip tie can be used to guide the flow and pop bubbles as the epoxy is poured. Tip: take a hammer and lightly tap the clevis as the resin is being poured. This allows the bubbles to rise to the surface.</li>
  <li>While the epoxy is wet, now is the time to bend back any remaining broom strand ends away from the Tygon tubing.</li>
  <li>Let the epoxy stand for a minimum of 1-2 hour before trimming back the broom strands to be as flush as possible with the hardened epoxy. <i>*Important: If left to harden at room temperature, the epoxy should set for at least 24 hours until deploying into water. *If time is of the essence, you may uniformly heat the clevis at 180-200° F with two heat guns for about 30 minutes; it will be fully cured and ready for deployment.</i></li>
  <li>Before attaching the clevis to the HabCam towing bridle, perform a pull test with the ship's winch and the towing block to ensure that the epoxy will hold under tension. Aim for a tension of 8000Ibs.</li>
</ol>

<br>

<h4>Part 4: The Boot</h4>

<ol>
  <li>The boot uses 6 rolls of 2in self-vulcanizing tape and 2-3 layers (not rolls!) of 2in electrical tape.</li>
  <li>Be sure when applying the tape that you pull tightly to ensure that the tape stretches and adheres to itself properly.</li>
  <li>Taper self-vulcanizing tape so that the area closest to the clevis is thickest.</li>
  <li>Entire boot length will be about 2.5ft or just under, if you measure from where the grooves in the clevis are.</li>
</ol>

<h4>Part 5: Fairing on Cable</h4>

<div align="center">
  <img width="577" height="432" alt="Fairing Cable On Deck" src="https://github.com/user-attachments/assets/75f5d219-02a1-4d7a-92dc-227e6c8e4b90" />
  <p><i>Applying Zip Tie Fairing along Tow Cable on Deck</i></p>
</div>

<ol>
  <li>Use the wide, 18" zip ties.[cite: 4]</li>
  <li>Starting from where the boot ends, apply zip ties along the wire for about 15-20 feet until 8-10 bags of 100 zip ties are consumed.[cite: 4]</li>
  <li>Fairing wrap could be used as a substitute, if handy.[cite: 4] Just secure the wrap with electrical tape.[cite: 4]</li>
</ol>

<h3>Fiber Optics Power Terminals</h3>

<h4>Part 1: Posing Power and Fiber Optic Wires</h4>

<ol>
  <li>From the open end of the fiber optic wire, measure 2 feet down, and make a mark. Then, VERY CAREFULLY, take a razor knife and score the black rubber down the length of the wire to that mark; you do not need to cut all the way through the rubber in order to remove it. Then, use a hefty pair of pliers to help peel back the stiff rubber before finally cutting it off at the 2-foot mark.
    <br><i>Tip: Try squeezing the end of the wire with the pliers; it can help split the rubber and get you started.</i>
  </li>
  <li>After the 2 feet of black rubber has been removed, carefully separate the now-exposed wires. You should have 3 power wires (2 brown, 1 green), 3 fiber optic wires (1 red, 1 gray, 1 black), some flexible rubber spacing material, and a thin, white-gray spacer strand.</li>
  <li>Remove the flexible rubber spacing material. You can also cut the very thin white-gray spacer strand.</li>
  <li>Finally, snip about an inch off the fiber and power wires to get rid of any broken regions that might have occurred from cutting the wire when it had all three metal layers attached.</li>
</ol>

<br>

<h4>Part 2: Inserting the Fiber Optic Wire into the J-Box</h4>

<ol>
  <li>Take the J-box that you are going to use. Two metal connectors on the side of the J-Box should already be utilized and have wire coming out of them. However, a third connector should be empty. Unscrew the threaded cap of that connector, and remove the metal ring collar and rubber gasket.
    <br><br>
    <div align="center">
    <img width="780" height="440" alt="J box Open" src="https://github.com/user-attachments/assets/6bf402c1-2d1e-4602-810a-7f7eb4a10bcd" />
    <p><i>Figure 2.1: Open J-Box Interior showing Empty Connector Port and Terminal Block</i></p>
    </div>
  </li>
  <li>Guide the power and fiber optic wires through the threaded cap; the threads of the cap should face the open end. Next, put on the metal ring collar, and then put on the rubber gasket so that the flattest part of the gasket is facing the open end of the wire. <b>*DO NOT MISS THIS STEP!</b></li>
  <li>Guide the power and fiber optic wires through the open connector on the side of the J-Box until about half an inch of black rubber is visible inside the J-box. Secure a hose clamp around the black rubber so that it is almost flush against the J-box wall; this technique ensures that the wire will not slip out through the connector hole.
    <br><br>
    <div align="center">
      <table>
        <tr>
          <td align="center">
            <img width="780" height="430" alt="Wire through J Box Gasket" src="https://github.com/user-attachments/assets/7ba85171-61a9-46b4-be90-f9621a9a49f4" />
            <br>
            <b>Threading Cap, Collar & Rubber Gasket onto Wire</b>
          </td>
          <td align="center">
            <img width="750" height="540" alt="Wire Secured via Hose Clamp" src="https://github.com/user-attachments/assets/167a8cba-641f-4396-b7ca-dbefbd1dd73e" />
            <br>
            <b>Internal Hose Clamp Secured Flush to Inner Wall</b>
          </td>
        </tr>
      </table>
    </div>
  </li>
  <li>Secure the gasket, metal ring collar, and threaded cap to the J-box. You might have to push in the rubber gasket with a padded item (e.g. a screwdriver with a rag around the end). Tighten the cap with a pipe wrench so that it is snug, but be careful not to turn the connector, as well.
    <br><br>
    <div align="center">
      <table>
        <tr>
          <td align="center">
           <img width="760" height="553" alt="Outside Gasket" src="https://github.com/user-attachments/assets/ca22fdb2-9ff7-40cc-93fa-4ad2481d2a71" />
            <br>
            <b>Seating Rubber Gasket & Metal Collar into Connector</b>
          </td>
          <td align="center">
          <img width="780" height="590" alt="Tightening Gasket" src="https://github.com/user-attachments/assets/dd89971c-2aa5-4ad6-8ff9-2539052325bc" />
            <br>
            <b>Tightening Threaded Cap with Pipe Wrench</b>
          </td>
        </tr>
      </table>
    </div>
  </li>
</ol>

<h4>Part 3: Connecting Ring Terminals to the Power Wires</h4>

<ol>
  <li>Find the 2 thick brown wires and 1 thick green wire. These are your power wires. The green wire is the one that actually sends the power, while the brown ones are neutral/ground. Start with your green wire.</li>
  <li>Select a 12-10 AWG ring terminal end and a gauged wire stripper/crimping tool.
    <br><br>
    <div align="center">
           <img width="725" height="223" alt="Ring Terminal and Crimper" src="https://github.com/user-attachments/assets/35e1c42f-873a-4caa-b1cb-a1c9d4fcdde8" />
            <br>
            <p><i>12-10 AWG Ring Terminal and Gauged Wire Stripper/Crimping Tool</i></p>
    </div>
    <br>
    Then, take your green wire. Using the stripping/crimping tool, find the size 12 hole and place just the tip of the green wire in it. Strip off little bits of the green coating (less than ½"), which will reveal copper wire, until you can place the wide end of the terminal over the copper and only a small amount (1 or 2/16ths of an inch) pokes through the tapered end (where the ring is).
  </li>
  <li>Place the ring terminal over your green wire.</li>
  <li>Then, using the crimping part of the tool, aim for the upper half of the terminal's yellow jacket and squeeze down very, very hard to crimp the terminal end to the exposed copper of the green wire. Tug on the terminal with your fingers to make sure it is secure.
    <br><br>
    <div align="center">
      <img width="670" height="501" alt="Crimped Ring Terminal" src="https://github.com/user-attachments/assets/32982909-3da0-4d99-82e0-59e8e5483f35" />
      <p><i>Crimped 12-10 AWG Yellow Ring Terminal</i></p>
    </div>
  </li>
  <li>Repeat Steps 2-3 for the two brown wires. All power wires should now have a ring terminal at the end of them.</li>
</ol>

<br>

<h4>Part 4: Connecting the Power Wires to the J-Box</h4>

<ol>
  <li>Locate the green power wire. Then, look into your J-box at the black power terminal attached to the yellow plastic; it should have screws and three wires with red ring terminals attached to it. Across from the middle wire is where the green one will screw in. You will have to gently bend the green wire in a loop around the inside of the J-box to get it to fit and attach to the power terminal. Just be careful not to make any sharp angles (i.e. 90°) with the wire.
    <br><br>
    <div align="center">
     <img width="654" height="490" alt="Wiring1" src="https://github.com/user-attachments/assets/c6ec133c-605b-4007-85ea-8ead22c8bd19" />
     <p><i>Green Power Wire Connected to Center Terminal Screw</i></p>
    </div>
  </li>
  <li>Finally, attach the brown wires to either side of the green one; it doesn’t matter which brown wire goes where, just that they are across from their red terminal counterparts.
    <br><br>
    <div align="center">
      <img width="618" height="456" alt="Wiring2" src="https://github.com/user-attachments/assets/d3780aff-f7cf-48a9-b80e-de5f22f7a9a8" />
      <p><i>Green and Brown Conductors Connected to J-Box Terminal Strip</i></p>
    </div>
  </li>
</ol>

<h3>Fiber Optic ST Connectors</h3>

<h4>Part 1: Safety, Cleanliness, and Pre-Heating Your Oven</h4>

<ol>
  <li>You will be working with small shards of metal and glass. Wear safety glasses <b>AT ALL TIMES</b> when working with the fiber optic wire ends.</li>
  <li>A majority of scratches, breaks, and mishaps come from improperly cleaned equipment—dirt is not your friend. Therefore, clean and wipe down the area you will be working in as best you can and give yourself plenty of space. Always wipe down all your tools with alcohol and a lint-free wipe before stripping fiber optic buffers or polishing. And finally, always clean the ST ferrule with alcohol and a low-lint wipe before looking into the viewing scope.</li>
  <li>Take your 3M Hot Melt kit and find your oven. Set up, plug in, and turn on your oven within easy reach; it needs at least six minutes to uniformly heat up.</li>
</ol>

<br>

<h4>Part 2: Exposing the Protective Jacketing</h4>

<ol start="4">
  <li>Find the gray, black, and red fiber optic wires. These wires need ST connectors attached to them in order to function properly. Start with your gray wire.</li>
  <li>Open up a 3M Hot Melt Connector Singlemode ST Yellow Boot connector packet. Inside, you will find a metal connector with a cap, a yellow boot, and a thin tube of plastic. You may discard the plastic tube; it's for a different kind of fiber than the one that we will be using.
    <br><br>
    <div align="center">
      <img width="780" height="285" alt="Connector Boot and Packet" src="https://github.com/user-attachments/assets/547e0749-b6b4-4503-8bf7-aad44b340efd" />
      <p><i>3M ST Yellow Boot Packet & Disassembled Component Parts</i></p>
    </div>
  </li>
  <li>*Place the yellow boot narrow-opening first onto the grey wire. <b>*if you forget this step, you can slice open the side of the boot and ease it onto the wire from the side.</b>
    <br><br>
    <div align="center">
     <img width="780" height="418" alt="Connector Sleeve" src="https://github.com/user-attachments/assets/df0d2df6-0e60-443c-9992-d0c73afa25c2" />
      <p><i>Yellow Boot Slid onto Gray Fiber Wire</i></p>
    </div>
  </li>
  <li>Then, find your 3M oven's hotplate. On the plate, should be a to-scale guide for the lengths to cut your ST wire. Line up your gray wire with the hot plate picture and make a mark right where the lines that form a crude 'V' on the plate's ST picture end.
    <br><br>
    <div align="center">
      <img width="780" height="548" alt="Connector Cut Back" src="https://github.com/user-attachments/assets/c5bce662-2192-47cb-a5b0-ee2987ba1c65" />
      <p><i>Measuring Cut Lengths on 3M Hotplate Scale Guide</i></p>
    </div>
  </li>
</ol>

<br>

<h4>Part 3: Trimming Metal Strands</h4>

<ol>
  <li>Gently and evenly fan out the metal jacketing so that no strands are overlapping. <b>BE CAREFUL</b>, as there is a buffered piece of glass in the middle of those metal jacketing strands. <b>DO NOT BEND the buffered glass.</b></li>
  <li>Next, take the metal strands of the jacket and bend them so that they go down the gray wire. Try to get them so that they are as flat as possible at the bend point—a tiny pair of needle nose pliers may help.
    <br><br>
    <div align="center">
      <table>
        <tr>
          <td align="center">
            <img width="701" height="520" alt="Wires Splayed Out" src="https://github.com/user-attachments/assets/592745b1-9dfe-4811-aff9-28c6b1379719" />
            <br>
            <b>Fanning Out Metal Jacketing Strands</b>
          </td>
          <td align="center">
            <img width="590" height="440" alt="Wires Folded Back" src="https://github.com/user-attachments/assets/66ea5059-6013-4b5b-9c9a-74181830c97f" />
            <br>
            <b>Bending Metal Strands Backward Flat</b>
          </td>
        </tr>
      </table>
    </div>
  </li>
  <li>Ensure you are still wearing your safety glasses and trim the metal strands until they are about a 1/4th of an inch long. When you are done trimming, make sure that the metal strands are still as flush as possible to the gray wire.</li>
</ol>

<br>

<h4>Part 4: Removing the 1st Buffer Layer from the Fiber</h4>

<ol>
  <li>Look at your hotplate ST picture. Notice the little rectangle between the crude "V"—that is how much of that buffer material you must remove from the fiber you've exposed. <b>Do not use a marker</b>, though. Instead, repeatedly reference the hotplate, if needed.</li>
  <li>Take a 3-hole fiber optic stripper, some isopropyl alcohol, and a low-lint wipe. Clean your 3-hole stripper with the alcohol and low-lint wipe. Then, using the second of the three holes, <b>GENTLY</b> strip away the buffer in small, short pieces. <b>CLEAN</b> your tool every time. Try to keep your movements straight and directly parallel with the fiber so that you do not break it.</li>
  <li>Keep removing the buffer (and cleaning your tool!) until you have reached the length indicated on the hotplate picture.</li>
</ol>

<br>

<h4>Part 5: Removing the Final Buffer from the Fiber</h4>

<ol>
  <li>Your fiber should now have a very thin layer of buffer left after the one you just removed. Using the smallest hole in your 3-hole stripper, <b>GENTLY</b> strip away the final layer in small, short pieces and <b>CLEAN your tool every time.</b> Try to keep your movements straight and directly parallel with the fiber so that you do not break the fiber.</li>
  <li>Keep removing the buffer (and cleaning your tool!) until you are even with the thicker buffer on your fiber.
    <br><br>
    <div align="center">
      <table>
        <tr>
          <td align="center">
            <img width="551" height="384" alt="Fiber Optic Stripper" src="https://github.com/user-attachments/assets/ec564a1d-8d91-473e-bef0-5e10f68e166c" />
            <br>
            <b>3-Hole Fiber Optic Stripper Tool</b>
          </td>
          <td align="center">
            <img width="780" height="513" alt="Cleaned Fiber Optic" src="https://github.com/user-attachments/assets/2d8bad4a-7d1f-44a3-8fe8-a75a7399f876" />
            <br>
            <b>Bare Glass Fiber Strand After Stripping</b>
          </td>
        </tr>
      </table>
    </div>
  </li>
  <li>Put some alcohol on a clean low-lint wipe, carefully position the wipe around your fiber, and gently give the fiber a few wipes to clear off any microscopic bits of buffer. <b>*Note: Missing this step could cause the fiber to break when inserting it into the ST connector.*</b></li>
</ol>

<h3>Fiber Optic ST Connectors</h3>

<h4>Part 1: Safety, Cleanliness, and Pre-Heating Your Oven 1)</h4>

<ol>
  <li>You will be working with small shards of metal and glass. Wear safety glasses <b>AT ALL TIMES</b> when working with the fiber optic wire ends.</li>
  <li>A majority of scratches, breaks, and mishaps come from improperly cleaned equipment dirt is not your friend. Therefore, clean and wipe down the area you will be working in as best you can and give yourself plenty of space. Always wipe down all your tools with alcohol and a lint-free wipe before stripping fiber optic buffers or polishing. And finally, always clean the ST ferrule with alcohol and a low-lint wipe before looking into the viewing scope.</li>
  <li>Take your 3M Hot Melt kit and find your oven. Set up, plug in, and turn on your oven within easy reach; it needs at least six minutes to uniformly heat up.</li>
</ol>

<br>

<h4>Part 2: Exposing the Protective Jacketing</h4>

<ol start="4">
  <li>Find the gray, black, and red fiber optic wires. These wires need ST connectors attached to them in order to function properly. Start with your gray wire.</li>
  <li>Open up a 3M Hot Melt Connector Singlemode ST Yellow Boot connector packet. Inside, you will find a metal connector with a cap, a yellow boot, and a thin tube of plastic. You may discard the plastic tube; it's for a different kind of fiber than the one that we will be using.</li>
  <li><b>*Place the yellow boot narrow-opening first onto the grey wire. *if you forget this step, you can slice open the side of the boot and ease it onto the wire from the side.</b></li>
  <li>Then, find your 3M oven's hotplate. On the plate, should be a to-scale guide for the lengths to cut your ST wire. Line up your gray wire with the hot plate picture and make a mark right where the lines that form a crude 'V' on the plate's ST picture end.</li>
</ol>

<br>

<h4>Part 3: Trimming Metal Strands</h4>

<ol>
  <li>Gently and evenly fan out the metal jacketing so that no strands are overlapping. <b>BE CAREFUL</b>, as there is a buffered piece of glass in the middle of those metal jacketing strands. <b>DO NOT BEND the buffered glass.</b></li>
  <li>Next, take the metal strands of the jacket and bend them so that they go down the gray wire. Try to get them so that they are as flat as possible at the bend point- a tiny pair of needle nose pliers may help.</li>
  <li>Ensure you are still wearing your safety glasses and trim the metal strands until they are about a 1/4th of an inch long. When you are done trimming, make sure that the metal strands are still as flush as possible to the gray wire.</li>
</ol>

<br>

<h4>Part 4: Removing the 1st Buffer Layer from the Fiber</h4>

<ol>
  <li>Look at your hotplate ST picture. Notice the little rectangle between the crude "V"- that is how much of that buffer material you must remove from the fiber you've exposed. <b>Do not use a marker</b>, though. Instead, repeatedly reference the hotplate, if needed.</li>
  <li>Take a 3-hole fiber optic stripper, some isopropyl alcohol, and a low-lint wipe. Clean your 3-hole stripper with the alcohol and low-lint wipe. Then, using the second of the three holes, <b>GENTLY</b> strip away the buffer in small, short pieces. <b>CLEAN</b> your tool every time. Try to keep your movements straight and directly parallel with the fiber so that you do not break it.</li>
  <li>Keep removing the buffer (and cleaning your tool!) until you have reached the length indicated on the hotplate picture.</li>
</ol>

<br>

<h4>Part 5: Removing the Final Buffer from the Fiber</h4>

<ol>
  <li>Your fiber should now have a very thin layer of buffer left after the one you just removed. Using the smallest hole in your 3-hole stripper, <b>GENTLY</b> strip away the final layer in small, short pieces and <b>CLEAN your tool every time.</b> Try to keep your movements straight and directly parallel with the fiber so that you do not break the fiber.</li>
  <li>Keep removing the buffer (and cleaning your tool!) until you are even with the thicker buffer on your fiber.</li>
  <li>Put some alcohol on a clean low-lint wipe, carefully position the wipe around your fiber, and gently give the fiber a few wipes to clear off any microscopic bits of buffer. <b>*Note: Missing this step could cause the fiber to break when inserting it into the ST connector.*</b></li>
</ol>

<br>

<h4>Part 6: Preparing to heat the ST Connector</h4>

<ol>
  <li>Find the ST connector that you removed from the packaging. Then, in your 3M Hot Melt kit, find the ST holders for the oven. Remove the cap from the ST connector and place the ST connector ferrule-side (pointy side) down into the ST holder.</li>
  <li>Your oven should already be hot. If you forgot to turn it on, do so now and wait about 6 minutes for it to uniformly heat up.</li>
</ol>

<br>

<h4>Part 7: Inserting the Fiber into the ST Connector- NOTE: <u>READ THIS ENTIRE PART FIRST BEFORE PROCEEDING</u></h4>

<ol>
  <li>Ready a stopwatch, so you can keep track of the seconds. Also, place your hot plate in front of you, so that you have some place to put the hot ST oven holders.</li>
  <li>Start your stopwatch and immediately place your ST oven holder with the connector inside in one of the oven holes.</li>
  <li>Pick up your gray fiber optic wire and position it over your hot plate with the fiber pointing down. You should be lightly bending the gray wire, but not so much that you kink it.
    <br><br>
    <div align="center">
      <table>
        <tr>
          <td align="center">
           <img width="452" height="316" alt="ST Holder" src="https://github.com/user-attachments/assets/783c47e2-b912-43cf-b310-a37277857d1c" />
            <br>
            <b>Placing ST Connector Ferrule into ST Holder</b>
          </td>
          <td align="center">
             <img width="412" height="246" alt="ST Epoxy" src="https://github.com/user-attachments/assets/338b6afa-446c-499d-a049-5d6a6e6589a0" />
            <br>
            <b>3M Hot Melt Oven & Hotplate Setup</b>
          </td>
        </tr>
      </table>
    </div>
  </li>
  <li>Watch the hole in the actual ST connector very carefully. Inside is a blue epoxy that is melting. You should see the epoxy begin to liquefy and make its way up the hole in the ST connector. At about 60 seconds, most of the epoxy should be melted. However, look at the connector hole. When the epoxy is a few 1/16th of an inch to the top (about 1min 30 seconds), but has not yet beaded over, that is your cue to remove the ST oven holder, QUICKLY place it on your hot plate, and IMMEDIATELY guide your fiber down into the very middle of the hot ST connector until the trimmed metal strands around the wire disappear and click into the connector. You have about 10-15 seconds until the epoxy becomes too cool to work with.</li>
  <li>Once your fiber is in place, let the connector and epoxy cool for about 3 minutes.</li>
</ol>

<p><b>Tips and Guidance:</b></p>
<ul>
  <li>Keep your fiber straight and your hands steady.</li>
  <li>Don't ever pull the fiber completely out of the ST connector, once you begin inserting it.</li>
  <li>Doing so may create air bubbles or multiple exit holes at the tip of the ST connector, all of which could create problems down the line. In the worst-case scenario, the fiber will have dried epoxy on it and be unable to fit through the other end of the ST connector.</li>
  <li>When you are guiding the fiber end into the ST connector, you may see it bend slightly. If you meet resistance, STOP, SLIGHTLY pull up on the fiber to get it in a different position, and then keep going.</li>
  <li>Any gusts of air through a window or doorway can cool the epoxy quicker and make it more difficult to work with. Try to eliminate or reduce any sources of wind, if you can.</li>
  <li>You may also try inserting the fiber while the ST connector is still in the oven. While risky, it has successfully been done. However, once you've inserted the fiber, immediately remove the holder from the oven so you do not melt the fiber.</li>
</ul>

<br>

<h4>Part 8: Remove the ST Connector from the Oven Holder</h4>

<ol>
  <li><b>BE CAREFUL, as you can easily break the fiber on this part.</b></li>
  <li>Slide down the yellow boot on your gray wire until it is over the connector hole that you pushed the fiber through. Gently press the boot until it snaps around the hole. You may have to steady the oven holder to be successful.</li>
  <li>Then, keeping your hands steady, slowly pull straight up on the yellow boot to remove the ST connector with your fiber in it from the oven holder.</li>
  <li>If you are lucky, you should see a significant portion of the fiber covered in blue epoxy sticking out the tip of your ST connector. If the fiber is exceptionally short or non-existent, it most likely broke inside the ST connector (sorry).</li>
  <li><b>NOTE: DO NOT LOOK DIRECTLY AT A LASER!</b> Use a laser and put it on the fiber end in the dry lab to see if you get light on the tip of the fiber you just put a connector on. If you do not see light, your fiber is broken; in that case, snip off the connector and repeat Parts 2-8. If you see light, continue.</li>
</ol>

<br>

<h4>Part 9: Scoring and Removing the Fiber</h4>

<ol>
  <li>In your fiber optic kit, find the scribe, which looks like a pen with a small, sloped cutting edge. Hold your upright and point towards the ceiling. Then, position your scribe and its edge perpendicular to the fiber.
    <br><br>
    <div align="center">
      <img width="425" height="414" alt="Scoring the Fiber" src="https://github.com/user-attachments/assets/a5de636a-8171-45a9-a71e-29571a702a85" />
      <p><i>Scribing Fiber Perpendicularly One Fiber Diameter from Ferrule Tip</i></p>
    </div>
  </li>
  <li>Carefully and lightly drag the edge of the scribe above the tip of the connector. You are aiming to make a slight cut or score about 1/16th of an inch up on fiber-you are NOT looking to completely cut it off, as breaking the fiber with the force of the scribe could lead to the glass shattering further down the ST connector.</li>
  <li>Once you score the fiber, position your fingers near the base of the connector and then move them up towards the fiber tip. Try to gently grasp the fiber as you make your way along. If the fiber does not easily come with you, try scoring the fiber again in the same spot and then repeating the process until all but the 1/16th inch fiber comes off.</li>
  <li>Discard the fiber tip into the sharps container in your fiber kit. <i>Tip: If you do break your fiber with the scribe, it is still worth proceeding, to the next two steps, as the fiber might still be salvageable.</i></li>
</ol>

<br>

<h4>Part 10: Air Polishing the Fiber</h4>

<ol>
  <li>In your fiber optic kit, find the round gray polishing sheets (9 micron grade)- one side should be shiny while the other side has the polishing paper. Take your fiber and use the polishing side of the gray sheet to make 15-20 figure-8 rotations. You are looking to polish down the fiber nub until it is basically flush with the bead of blue epoxy coming out of the fiber connector. Keep air polishing and visually checking your fiber until the glass nub is flush with the epoxy bead.</li>
</ol>

<br>

<h4>Part 11: Pad Polishing with Green Sheets</h4>

<ol>
  <li>Find the round, black polishing pad; a low-lint wipe; and some isopropyl alcohol. Put several drops of alcohol on the polishing pad and clean the pad with the wipe until any traces of dust or debris are gone.</li>
  <li>Put several drops of water on the pad, place the shiny side of the green polishing sheet down onto the pad, and then use a low-lint wipe on the polishing side to push that water around underneath and remove any air bubbles between the sheet and the pad.</li>
  <li>Take a polishing puck from the black pocket in the fiber optic tool holder and clean the puck with alcohol, too.</li>
  <li>Place the puck flat-side down onto your green polishing sheet and then ease your ferrule into the hole at the top of the puck. With a <b>slight pressure</b>, hold onto both the connector and the polishing puck. Make figure-8 rotations until the blue adhesive is just barely removed-you will see the epoxy turn from blue to light blue as it is removed until you are left with just the white ferrule at the tip of the ST connector. Be careful not to polish too much- once the epoxy is removed, you are essentially polishing the tip of the ST connector, which can be easily scratched.</li>
  <li>After you have successfully removed the epoxy, clean the tip of your ferrule with some alcohol and a low-lint wipe. Then, take your fiber optic viewing scope and carefully fit your ferrule tip into the bottom of the scope. Press the I button to see the top of your fiber optic ferrule (best for checking dirt, scratches, and surface chips) and the II button to see it lit from below (best option for checking damage to the core and the face of the fiber).</li>
  <li>Using the II button for viewing the scope, you should see the following: The dark gray circle represents your fiber and the small, light gray circle in the very middle of the image is your core. In your scope, everything should be the faintest hint of blue (from the epoxy). The core is the most important part of this operation. If there are any chips in the ferrule (which show up as black areas in the dark gray) or scratches and gouges that go through your core, there may be significant light loss and the ST connector is potentially useless. Small scratches may be remedied by polishing the ST connector with the green lapping film a few more times.
    <br><br>
    <div align="center">
      <table>
        <tr>
          <td align="center">
          <img width="908" height="361" alt="Polishing the Fiber" src="https://github.com/user-attachments/assets/409e6ab5-c1eb-4e76-a0fd-cff7fbd8d6f8" />
            <br>
            <b>Failed Scope Views: Chipped Core, Epoxy Rings & Scratches</b>
          </td>
          <td align="center">
            <img width="471" height="340" alt="Dirty View" src="https://github.com/user-attachments/assets/1476c15e-8bc9-4024-a2b5-a2f4d4533fed" />
            <br>
            <b>Dirty Ferrule View (Clean with Alcohol Wipe)</b>
          </td>
        </tr>
      </table>
    </div>
    <br>
    If they do not go away, then the scratches are deep within the ST connector and cannot be fixed. Chips can sometimes occur from improper scoring and cleaving with the scribe- if you broke the fiber while scoring it, then be sure to check for chips when looking at the ST connector under the scope.
    <br><br>
    The connector on the left has a large chip on the right side and small chips all around the fiber; it is also heavily scratched and has some pitting. The connector in the middle shows contamination from some liquid and a large chip along the bottom, but the rings around the fiber show the epoxy was not completely polished off. The connector on the right shows scratching and chipping also, including one very large scratch across the fiber and ferrule. All of these connectors are unusable. While you may be able to fix the scratches or remove the epoxy rings with more polishing, the chips will create too much light loss for the connector to work efficiently. If you see large chips, cut off the connector from your fiber wire and begin Part 1-11 again for the fiber optic connector.
    <br><br>
    This connector is simply dirty, possibly with oil from a fingertip. Cleaning it alcohol and a low-lint wipe should fix the problem.
  </li>
</ol>

<br>

<h4>Part 12: Pad Polishing with White Sheets</h4>

<ol>
  <li>If your connector appears mostly smooth and fairly free of scratches, debris, chips, etc., then you can proceed to the final polish.</li>
  <li>Discard your used green sheet and put several drops of water on the pad. Place the shiny side of a white polishing sheet down onto the pad, and then use a low-lint wipe on the polishing side to push that water around underneath and remove any air bubbles between the sheet and the pad.</li>
  <li>Take your polishing puck and clean it with alcohol again. Place the puck <b>flat-side down</b> onto your white polishing sheet and then ease your ferrule into the hole at the top of the puck. With a slight pressure, hold onto both the connector and the polishing puck. Make two to three figure-8 rotations. You are basically just fine-polishing the ferrule to ensure that the surface is as smooth as possible; not a lot of effort is needed here.</li>
  <li>Look at the fiber in your viewing scope. You should have as much of a close-to-perfect connector as possible, at this point.</li>
  <br><br>
    <div align="center">
      <img width="345" height="287" alt="Clean Fiber" src="https://github.com/user-attachments/assets/741690bd-0077-46bb-af76-020a343803a3" />
      <p><i>Ideal/Clean Fiber Ferrule Core View under Viewing Scope</i></p>
    </div>
  </li>
  <li><b>NOTE: <u>DO NOT LOOK DIRECTLY AT THE LASER!</u></b> Use a laser and put it on the fiber end in the Dry Lab to see if you get light on the tip of the fiber.</li>
</ol>

<br>

<h4>Part 13: Terminating the Black and Red Fiber Wires</h4>

<ol>
  <li>Repeat Parts 2-12 for the black and red wires. Of note, however, is that HabCam technically only needs one back up fiber, in case anything goes wrong with the main data acquisition one (gray). Therefore, do not stress too much if you're having issues getting all three connectors working. Reasonable efforts should be made, though, to ensure that we are terminating all the fibers ends; it is simply good practice and allows for more flexibility if fiber issues arise.</li>
</ol>

<h4>Part 14: Connecting Main Fiber to J-box Cable</h4>

<ol>
  <li>After all your fibers are terminated, you must connect the main fiber that sends information from Habcam down the cable- this is (usually) your gray wire. Look at your J-box. Connected to the red cable, which comes out the side of it, should be several black wires with white boots and ST connectors on the end.
    <br><br>
    3 out of the 4 connectors should have yellow pieces of plastic tubing around the ends. The last connector will have a metal coupler on the end; this coupler is where your gray wire will attach. Make sure you loop the gray wire around so that it rests comfortably in the J-box, once connected, and will not be kinked.
    <br><br>
    <div align="center">
      <img width="472" height="365" alt="J Box on Work Bench" src="https://github.com/user-attachments/assets/4834da12-ddbd-475e-9575-a53778837307" />
      <p><i>J-Box Layout and Cable Entry Positioning on Worktable</i></p>
    </div>
    <br>
<div align="center">
 <img width="780" height="303" alt="Connecting Main Fiber in J Box" src="https://github.com/user-attachments/assets/7c58f4a8-3b29-4522-9254-a8f1198cb95e" />
  <p><i>Coupling Primary Gray ST Fiber to Metal Adapter Assembly (Left: Aligning Connector; Right: Mated in Position)</i></p>
</div>
  </li>
  <li>Finally, carefully loop the red and black fibers around in the J-box, so they rest neatly amongst the rest of the wires. Use small, thin zip ties to loosely secure all the wires in place.
    <br><br>
    <div align="center">
    <img width="671" height="414" alt="Coiled Fiber" src="https://github.com/user-attachments/assets/b2b73024-c5e1-47a5-8326-c6395c59ede6" />
      <p><i>Red and Black Backup Fibers Coiled and Zip-Tied inside J-Box</i></p>
    </div>
  </li>
</ol>

<br>
<hr>
<br>

<h3>Buttoning Up the J-box</h3>

<h4>Part 1: Securing the Bladder</h4>

<ol>
  <li>The bladder is a yellow piece of urethane that is flexible, covers all the J-box wiring, and (hopefully) prevents seawater intrusion. Find the bladder and look at the surface. One side will have a relatively deep indentation of where it rested against the face of the J-box- this is the side that must be placed down (against the face).
    <br><br>
    Try to line up the holes on the bladder with the holes on the J-box; they will not be exact, however, as the bladder stretches once the screws are inserted.
  </li>
  <li>Next, there is a metal plate with screw holes that goes over the bladder. The side with the most obvious rings around the holes (from metal washers) is the side that should face up.</li>
  <li>Next, take the J-box screws, a lock washer, and a flat washer. The lock washer should go on the screw first and then the flat washer.</li>
  <li>Place the screws through the metal plate holes and bladder. You might have to slightly change the direction you are inserting the screws in order to get the bladder to stretch properly.
    <br><br>
    <div align="center">
      <table>
        <tr>
          <td align="center">
            <img width="577" height="421" alt="Sealing J Box 1" src="https://github.com/user-attachments/assets/5fd940f1-cd82-458e-bcee-041503a5e439" />
            <br>
            <b>1. Aligning Yellow Bladder Indentation Face Down</b>
          </td>
          <td align="center">
           <img width="647" height="366" alt="Sealing J Box 2" src="https://github.com/user-attachments/assets/d29f90ce-5dfc-4173-8c5d-4a78a3cb5324" />
            <br>
            <b>2. Metal Retaining Plate Alignment</b>
          </td>
        </tr>
        <tr>
          <td align="center">
            <img width="437" height="331" alt="J Box Bolt" src="https://github.com/user-attachments/assets/a4913ba1-5176-4070-aeef-3ae0b590b694" />
            <br>
            <b>3. 5mm Allen Screw with Lock & Flat Washers</b>
          </td>
          <td align="center">
           <img width="587" height="409" alt="Sealing J Box 3" src="https://github.com/user-attachments/assets/0daa1063-de92-4aac-9c4f-4433890c33be" />
            <br>
            <b>4. Threading 5mm Allen Screws into Perimeter</b>
          </td>
        </tr>
      </table>
    </div>
  </li>
  <li>Once all screws are in the J-box, take a 5mm Allen key and tighten the screws only to the point that they do not turn with light pressure. Tighten the screws as you would tire lug nuts- once you tighten a screw, go to the opposite side and tighten its counterpoint until you make your way around the J-box.
    <br><br>
    All the screws should be secured in such a manner that they no longer turn with slight pressure <b>AND</b> the bladder is not dramatically sticking out from beneath the metal plate. Therefore, do not crank down on the screws! If the bladder bleeds out too much, it can compromise the water-tight integrity.
  </li>
</ol>

<br>

<h4>Part 2: Filling the J-box with Oil</h4>

<ol>
  <li>On your J-box should be two white valves. Take your jug full of oil and insert the valve attachment (on the clear tubing) into one of the white valves- press the metal tab on the side of the J-box valve to get the attachment to fit correctly.</li>
  <li>Take a clear tube with an open end and a valve attachment. Insert the attachment into the second white valve and then have someone hold the open end over a bucket or reservoir.</li>
  <li>Then, using the oil-filled jug, pump oil into the J-box. There is a release valve on the tube coming from the jug that you must press to get the oil to start flowing- be careful not to press it for too long or the middle of the bladder will start ballooning out from the air pressure and could burst or damage the integrity of the urethane.</li>
  <li>To completely fill the J-box with oil and prevent any air bubbles from remaining, you might have to tilt the J-box vertically so that the white valves are facing up and the valve that has the open tube (where the air is purged) is at the highest point.</li>
  <li>Once you are done filling the J-box, do a visual inspection. There should be no oil leaks anywhere around the screws and there should be no (or very, very small) air bubbles inside the J-box.
    <br><br>
    <div align="center">
    <img width="437" height="331" alt="J Box Bolt" src="https://github.com/user-attachments/assets/38641f6e-fc2f-46e1-a659-aa37854b9dae" />
      <p><i>Compensating Oil Vacuum Pump & Purge Reservoir Setup</i></p>
    </div>
  </li>
</ol>

<br>

<h4>Part 3: Securing the J-box to HabCam</h4>

<ol>
  <li>Carry the oil-filled J-box and clevis out to HabCam. The J-box and black wiring must first be fed along the <b>BACK</b> of the towing bridle (Stand at the front of HabCam and imagine the bridle is vertical- the wire should not be visible from the towing direction).</li>
  <li>Next, guide it <b>INSIDE</b> the towing bridle (port side), <b>OVER</b> the towing bridle crossbar (port side), down the <b>INSIDE</b> of a side car, and through a small opening so that it ends up upside down on the port-aft side of the HabCam; the red and black fiber/power wires coming out of the J-box should be facing aft, so that they are closest to where they connect to the telemetry bottle. Basically, once you’re done attaching the J-box, no part of the stripped black cable should be exposed in such a way that it would easily be crunched, kinked, snagged, etc. from anything that could make contact with the HabCam underwater- when in doubt, keep the wire to the inside of the vehicle and away from the tow direction.</li>
  <li>Secure the black wire to the vehicle with zip ties. You may also have extra black wiring. If so, create a large loop with the black wire and secure it to HabCam with zip ties, so that it is not flapping around.</li>
  <li>Plug in the red wire on the J-box to the fiber optic port on HabCam's telemetry bottle. The black wire will plug into the power port on the telemetry bottle.</li>
</ol>

<h2>Fiber Optics Pull Test</h2>

<h3>Purpose</h3>

<p>A pull test (or proof load test) using a water bag on a hydraulic winch line is performed to safely verify that the winch and its mounting structure can handle their maximum rated weight capacity. This test uses weights or simulated loads to prove that the mechanical, hydraulic, and brake systems work perfectly in real working conditions and that your winch is safe to use for anchoring, towing, and mooring operation.</p>

<p><b>1. Load Testing:</b><br>
<b>Purpose:</b> To ensure that the winch is capable of pulling or holding loads according to its nominal capacity without structural failure. The winch is tested using actual loads of up to 110–125% of its design capacity.</p>

<p><b>2. Brake Test:</b><br>
<b>Purpose:</b> To ensure that the main and emergency brake systems can safely hold loads, even under extreme conditions. The brake test is performed by suddenly stopping the winch while pulling a specific load. Technicians will evaluate whether the brakes can hold the load without slipping or dropping.</p>

<p><b>3. Functional Test:</b><br>
<b>Purpose:</b> To evaluate the overall operational performance of the winch in real conditions. The functional test is performed after the load and brake tests to ensure that all components work together and that your winch is ready for safe and efficient use at sea.</p>

<br>

<h3>Preparation</h3>

<p>After the termination is complete (and tested) and the epoxy inside the clevis has cured you can proceed to the pull test. Attach the clevis to the water bag in the order shown in the image below. Note the hose clamp at the top, up against the clevis (Don't forget to install this).</p>

<p><i>You will need to coordinate with the Bigelow ahead of time to borrow the water bag from the U.S. Coast Guard and help from the Chief Bosun to perform the test.</i></p>

<br>

<div align="center">
  <table>
    <tr>
      <td valign="top" style="padding-right: 20px;">
        <p><b>Order of Operation:</b></p>
        <div style="border: 1px solid #000; padding: 12px; width: 160px; line-height: 1.6;">
          Clevis &rarr;<br>
          Swivel Shackle &rarr;<br>
          Shackle &rarr;<br>
          Load Sensor &rarr;<br>
          Water Bag
        </div>
      </td>
      <td align="center" valign="top">
        <img width="403" height="325" alt="Hanging Connection" src="https://github.com/user-attachments/assets/60e38f22-a018-4d84-adaf-d3b4caa9063d" />
        <br>
        <p><i>Rigging Linkage: Clevis, Swivel Shackle, Shackle, Load Sensor, & Water Bag</i></p>
      </td>
    </tr>
  </table>
</div>

<br>

<h3>Test Execution & Verification</h3>

<p><i>HabCam J-Box and cables positioned safely out of the way for testing.</i></p>

<div align="center">
  <img width="489" height="367" alt="Bag" src="https://github.com/user-attachments/assets/cf879147-8fd8-47d0-b739-e960c1d922e3" />
  <p><i>Water Bag Suspended over Deck during Pump Filling</i></p>
</div>
<p>With the water bag in position, the Chief Bosun will coordinate with the engineers to turn on the pumps and begin filling the bag.</p>
<p>Monitor the tension on the load sensor and let the bosun know when you get to 9,000lbs so they can slowly close the pumps with the intention to fully close the pumps at 10,000lbs tension.</p>
<p>Next hold the tension at 10,000lbs for approximately 1 minute.</p>

<br>

<div align="center">
  <table>
    <tr>
      <td align="center" valign="top">
       <img width="480" height="550" alt="Weight" src="https://github.com/user-attachments/assets/2e893083-c56f-4322-842a-9c36a50162f4" />
        <br>
        <p><i>Load Sensor Readout Displaying 10,000 lbs Test Tension</i></p>
      </td>
      <td valign="top" style="padding-left: 20px;">
        <p>Once complete, the water bag can be emptied and brought back on the deck.</p>
        <p>Inspect the hose ring that was cinched above the clevis and verify that the clevis has <b>not <u>slipped</u></b> under tension.</p>
        <p>If the location has changed and the clevis slipped then adjustments must be made, and the test must be run again.</p>
        <p>If its location hasn't changed, attach the J-box cables and retest the fiber optics with the HabCam vehicle.</p>
        <p>If everything is working you are good to go.</p>
      </td>
    </tr>
  </table>
</div>


<div align="center">
<table>
  <tr>
    <td><a href="README.md">Home</a></td>
    <td><a href="01-overview-and-species.md"><b>01 Overview</b></a></td>
    <td><a href="02-hardware-and-schematics.md">02 Hardware</a></td>
    <td><a href="03-software-and-data.md">03 Software</a></td>
    <td><a href="04-staging-and-surveys.md">04 Staging</a></td>
    <td><a href="05-data-processing-and-analysis.md">05 Data & Analysis</a></td>
    <td><a href="06-maintenance-and-troubleshooting.md">06 Maintenance</a></td>
  </tr>
</table>

</div>

</div>
