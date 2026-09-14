<div align="center">

# HabCam Hardware, Schematics & Mounting Specifications

<table>
  <tr>
    <td><a href="README.md">Home</a></td>
    <td><a href="01-overview-and-species.md">01 Overview</a></td>
    <td><b>02 Hardware</b></td>
    <td><a href="03-checklists-and-calibration.md">03 Checklists</a></td>
    <td><a href="04-software-and-data.md">04 Software</a></td>
    <td><a href="05-staging-and-sea-ops.md">05 Sea Ops</a></td>
  </tr>
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

## Mounting Hardware Hardware & Tooling Inventory
<p>Master breakdown of structural brackets, fasteners, barrier rubbers, and specialized tools required for vehicle payload integration.</p>

| Subsystem | Mounting Location | Required Hardware & Fasteners | Required Tools |
| :--- | :--- | :--- | :--- |
| **Electronics Bottle** *(1x)* | Aft Vehicle Frame | • (4x) Black Aluminum Brackets<br>• (4x) Barrier Rubber Pieces (Pliobond 35 glued)<br>• (8x) 9/16"-12 (3 ½") Partial Thread Bolts<br>• (8x) 9/16"-12 (2 ¼") Partial Thread Bolts<br>• (4x) 32" 11mm Fully Threaded Rods<br>• (6x) Plastic Washers, (10x) Steel Washers<br>• (8x) Steel Lock Nuts, (8x) Hex Nuts | • 9/16" Socket & Wrench<br>• 7/16" Wrench<br>• 14mm Wrench |
| **BlueView Sonar** *(1x)* | Forward Vehicle Frame | • (4x) Steel Brackets<br>• (4x) Barrier Rubber Pieces<br>• (6x) 9/16"-12 (3 ½") Steel Partial Thread Bolts<br>• (4x) 9/16"-12 (2 ¼") Steel Partial Thread Bolts<br>• (20x) 3/16" Steel Washers<br>• (10x) Steel Lock Nuts, (10x) Hex Nuts | • 9/16" Socket & Wrench<br>• 14mm Wrench<br>• Aqua Shield Grease |
| **CTD 39 Oxygen** *(1x)* | Starboard Forward Rail | • (2x) UHMW Brackets, (2x) Plastic Brackets<br>• (4x) Barrier Rubber Pieces<br>• (4x) 7/16"-14 (4 ¾") Steel Partial Thread Bolts<br>• (2x) 7/16"-14 (1") Steel Full Thread Bolts<br>• (3x) 3/16" (1") Socket Head Screws<br>• (10x) Steel Washers, (6x) Lock Nuts, (2x) Hex Nuts | • 7/16" Socket & Wrench<br>• 11mm Wrench<br>• Hex Key Set (1/4"–1/16") |
| **CTD 49 Sound Speed** *(1x)* | Port Forward Rail | • (6x) Plastic Brackets (Sensor, Center, Frame)<br>• (8x) Barrier Rubber Pieces<br>• (8x) 9/16"-12 (2 ¾") Steel Partial Thread Bolts<br>• (16x) Steel Washers<br>• (8x) Steel Lock Nuts, (8x) Hex Nuts | • 9/16" Socket & Wrench<br>• 14mm Wrench |
| **Eco-Triplet Puck** *(1x)* | Center Forward Expansion Rail | • (2x) Steel Brackets (Top & Bottom)<br>• (2x) Barrier Rubber Pieces<br>• (2x) 9/16"-12 (2 ½") Steel Partial Thread Bolts<br>• (2x) 9/16"-12 (2") Steel Partial Thread Bolts<br>• (6x) Steel Washers, (4x) Lock Nuts, (2x) Hex Nuts | • 9/16" Socket & Wrench<br>• 14mm Wrench |
| **Habitat Cameras** *(2x)* | Center Frame Plate | • (1x) Steel Mounting Plate (16 in x 16 in)<br>• (6x) Metal Brackets<br>• (4x) M7-1.0 x 45mm Threaded Bolts<br>• (4x) 1/4"-20 (2") Socket Head Screws<br>• (8x) 1/4"-20 (1") Socket Head Screws<br>• (6x) Steel Washers, (6x) Steel Lock Nuts | • Hex Key Set (1/4"–1/16")<br>• M7 / 3/16" Allen Keys |
| **Strobe Lights** *(4x)* | Forward, Aft, Port, Starboard | • (8x) Steel Brackets<br>• (8x) Barrier Rubber Pieces<br>• (8x) 9/16"-12 (3 ½") Steel Partial Thread Bolts<br>• (8x) 7/16"-14 (1 ¾") Steel Partial Thread Bolts<br>• (32x) Plastic Washers, (32x) Steel Washers<br>• (16x) Steel Lock Nuts, (16x) Hex Nuts | • 9/16" Socket & Wrench<br>• 7/16" Socket & Wrench<br>• 14mm / 11mm Wrenches |
| **Sonar Altimeter** *(1x)* | Center Camera Plate | • (2x) Plastic Brackets<br>• (4x) Barrier Rubber Pieces<br>• (4x) 9/16"-12 (6 ½") Steel Partial Thread Bolts<br>• (8x) Steel Washers<br>• (4x) Steel Lock Nuts, (4x) Hex Nuts | • 9/16" Socket & Wrench<br>• 14mm Wrench |


<h2>Detailed Hardware Specifications & Tooling Breakdown</h2>

<a name="electronics-bottle"></a>
<h3>Electronics Bottle (1x)</h3>

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
  <li>(6x) Plastic Washers</li>
  <li>(10x) 3/16" Steel Washers</li>
  <li>(8x) Steel Lock Nuts</li>
  <li>(8x) 9/16”-12 Steel Hex Nuts</li>
</ul>

<p><b>Tools Needed:</b></p>
<ul>
  <li>9/16" Socket Wrench</li>
  <li>9/16" Combination Wrench</li>
  <li>14mm Combination Wrench (Optional)</li>
</ul>

<br>
<hr>
<br>

<a name="blueview-sonar"></a>
<h3>BlueView Forward Facing Sonar (1x)</h3>

<div align="center">
<img width="530" height="705" alt="BlueView" src="https://github.com/user-attachments/assets/992d102a-c524-457e-b3f7-2bba977efd09" />
  <br><br>
  <!-- Secondary Installed Photo Space -->
  [DROP BLUEVIEW SONAR MOUNTED / EXTRA PHOTO HERE]
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
</ul>

<br>
<hr>
<br>

<a name="ctd-39-dissolved-oxygen"></a>
<h3>CTD-39 Dissolved Oxygen Sensor (1x)</h3>

<div align="center">
<img width="530" height="708" alt="CTD-39" src="https://github.com/user-attachments/assets/2b06c7c3-7110-4aab-bc1d-03d5f765ab2b" />
  <br><br>
  <!-- Secondary Installed Photo Space -->
  [DROP CTD-39 MOUNTED / EXTRA PHOTO HERE]
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

<br>
<hr>
<br>

<a name="ctd-49-sound-speed"></a>
<h3>CTD-49 Sound Speed Sensor (1x)</h3>

<div align="center">
<img width="537" height="715" alt="CTD-49" src="https://github.com/user-attachments/assets/acfb146e-98b2-4127-ae30-f809362fa6a9" />
  <br><br>
  <!-- Secondary Installed Photo Space -->
  [DROP CTD-49 MOUNTED / EXTRA PHOTO HERE]
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

<br>
<hr>
<br>

<a name="eco-triplet-puck"></a>
<h3>Eco-Triplet Puck (1x)</h3>

<div align="center">
<img width="546" height="727" alt="Eco-Triplet" src="https://github.com/user-attachments/assets/55354b6d-fcf0-46a6-9249-841b3b7e2f9f" />
  <br><br>
  <!-- Secondary Installed Photo Space -->
  [DROP ECO-TRIPLET MOUNTED / EXTRA PHOTO HERE]
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

<br>
<hr>
<br>

<a name="habitat-cameras"></a>
<h3> Cameras (2x)</h3>

<div align="center">
<img width="549" height="732" alt="Camera" src="https://github.com/user-attachments/assets/d41133ad-3292-487d-b2d3-f8a05d4d4eb6" />
  <br><br>
  <!-- Secondary Installed Photo Space -->
  [DROP HABITAT CAMERAS MOUNTED / EXTRA PHOTO HERE]
</div>

<br>

<p><b>Hardware Inventory:</b></p>
<ul>
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

<br>
<hr>
<br>

<a name="strobe-lights"></a>
<h3>Strobe Lights (4x)</h3>

<div align="center">
<img width="550" height="734" alt="Strobes" src="https://github.com/user-attachments/assets/4cb76693-0378-47cd-b581-d94f0644c457" />
  <br><br>
  <!-- Secondary Installed Photo Space -->
  [DROP STROBE LIGHTS MOUNTED / EXTRA PHOTO HERE]
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

<br>
<hr>
<br>

<a name="attitude-sensor"></a>
<h3>Attitude Sensor (1x)</h3>

<div align="center">
 
  <br><br>
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

<br>
<hr>
<br>

<a name="altimeter"></a>
<h3>Altimeter (1x)</h3>

<div align="center">
<img width="557" height="743" alt="Altimeter" src="https://github.com/user-attachments/assets/968aa9ce-5334-483f-b910-758af423c30d" />

  <br><br>
  <!-- Secondary Installed Photo Space -->
  [DROP ALTIMETER MOUNTED / EXTRA PHOTO HERE]
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

<div align="center">

# HabCam Vehicle Sensor Preparation & Assembly Protocols

<table>
  <tr>
    <td><a href="README.md">Home</a></td>
    <td><a href="01-overview-and-species.md">01 Overview</a></td>
    <td><a href="02-hardware-and-schematics.md">02 Hardware</a></td>
    <td><b>03 Checklists & Prep</b></td>
    <td><a href="04-software-and-data.md">04 Software</a></td>
    <td><a href="05-staging-and-sea-ops.md">05 Sea Ops</a></td>
  </tr>
</table>

</div>

<br>

<h2>Master Sensor Assembly Reference</h2>

<table>
  <thead>
    <tr>
      <th align="left">Component / Subsystem</th>
      <th align="left">Primary Function</th>
      <th align="left">Fastener / Bracket Spec</th>
      <th align="left">Interface / Protocol</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="#blueview-sonar"><b>BlueView Forward Looking Sonar</b></a></td>
      <td>Real-time 2D acoustic obstacle avoidance & seabed imaging</td>
      <td>Steel Brackets + Rubber Gaskets, (4x) 9/16" Bolts</td>
      <td>Ethernet / Impulse MKS</td>
    </tr>
    <tr>
      <td><a href="#ctd-39-do"><b>SBE CTD 39 Dissolved Oxygen (Optional)</b></a></td>
      <td>High-accuracy oceanographic temperature & depth recording</td>
      <td>UHMW/Plastic Brackets, (4x) 7/16" Bolts</td>
      <td>RS-232 / SubConn MCBH</td>
    </tr>
    <tr>
      <td><a href="#ctd-49-fastcat"><b>SBE CTD 49 FastCAT Sound Speed</b></a></td>
      <td>Integrated CTD sensor for high spatial resolution profiling</td>
      <td>Plastic Brackets + Rubber Gaskets, (4x) 9/16" Bolts</td>
      <td>RS-232C (16 Hz) / SubConn MCBH</td>
    </tr>
    <tr>
      <td><a href="#eco-triplet"><b>ECO V2 Triplet Puck Fluorometer</b></a></td>
      <td>Multi-channel optical biological & dye trace monitoring</td>
      <td>Expansion Rail Steel Brackets, (2x) 9/16" Bolts</td>
      <td>RS-232 / SubConn MCBH-6M</td>
    </tr>
    <tr>
      <td><a href="#main-electronics-bottle"><b>Main Electronics Bottle</b></a></td>
      <td>Pressure-resistant central computer, power & telemetry housing</td>
      <td>Aluminum Clamps + Pliobond 35 Rubber, Threaded Rods</td>
      <td>CWDM Fiber / SubConn Bulkheads</td>
    </tr>
    <tr>
      <td><a href="#mako-cameras"><b>Allied Vision Mako G-234 Cameras (x2)</b></a></td>
      <td>2.35 MP stereo image capture synchronized with strobes</td>
      <td>Center Mounting Plate, Steel Brackets</td>
      <td>GigE IEEE 802.3af PoE</td>
    </tr>
    <tr>
      <td><a href="#dragonfish-strobes"><b>Dragonfish Mini LED Strobes (x4)</b></a></td>
      <td>High-output 30,000-lumen pulsed illumination</td>
      <td>Steel Brackets + Barrier Rubbers, 9/16" & 7/16" Bolts</td>
      <td>5V TTL Logic Trigger / SubConn MCBH4M</td>
    </tr>
    <tr>
      <td><a href="#attitude-sensor"><b>Microstrain AHRS Attitude Sensor</b></a></td>
      <td>9-axis IMU vehicle orientation (pitch, roll, yaw) tracking</td>
      <td>Internal Housing Chassis Mounting</td>
      <td>RS-232 / USB</td>
    </tr>
    <tr>
      <td><a href="#benthos-altimeter"><b>Teledyne Benthos PSA 916 Altimeter</b></a></td>
      <td>200 kHz acoustic distance-to-seafloor measurement</td>
      <td>Plastic Brackets + Rubber Gaskets, (4x) 9/16" Bolts</td>
      <td>RS-232 / Analog 0–5 VDC</td>
    </tr>
  </tbody>
</table>

<br>
<hr>
<br>

<a name="blueview-sonar"></a>
<h2>BlueView Forward Looking Sonar</h2>

<div align="center">
  <!-- Primary Assembly Photo Placeholder -->
  [DROP BLUEVIEW SONAR OVERVIEW PHOTO HERE]
  <br><br>
  <!-- Installed Detail Photo Placeholder -->
  [DROP BLUEVIEW SONAR MOUNTING DETAIL PHOTO HERE]
</div>

<br>

<p><b>System Overview:</b> A forward-facing sonar system designed to provide high-resolution imaging of the underwater environment in front of the vehicle. Unlike traditional single-beam down-looking sonars, it scans the area ahead to detect obstacles, submerged structures, and features during poor-visibility tow operations.</p>

<h3>Sonar Preparation & Mounting Steps</h3>
<ol>
  <li>Prior to attaching BlueView to the front of the vehicle, ensure the mounting bracket has rubber gaskets glued to it (brackets should already be secured to the HabCam frame).</li>
  <li>Attach BlueView to the bracket with the Impulse connector facing towards the back of the vehicle.</li>
  <li>Thread four stainless steel screws through the bracket.</li>
  <li>Prior to adding the stainless steel washer, lock washer, and nut, apply Aqua Shield grease over all bolt threads.</li>
  <li>Install the hardware on all four screws: stainless steel washer on the inside, lock washer in the middle, and hex nut on the outside.</li>
  <li>Use 9/16" ratcheting wrenches to tighten all four nuts securely.</li>
</ol>

<br>

<h3>Teledyne Marine BlueView M450 Mk2 System Specifications</h3>

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
      <td>Impulse MKS(W) Splash-mate</td>
    </tr>
    <tr>
      <td><b>Beam Width (Horiz / Vert)</b></td>
      <td>1&deg; / 10&deg;</td>
      <td><b>Weight in Air (S Mk2)</b></td>
      <td>3.5 kg</td>
    </tr>
    <tr>
      <td><b>Number of Beams</b></td>
      <td>768 (0.18&deg; spacing)</td>
      <td><b>Weight in Water (S Mk2)</b></td>
      <td>1.6 kg</td>
    </tr>
    <tr>
      <td><b>Update Rate</b></td>
      <td>Up to 20 Hz</td>
      <td><b>Depth Rating (S / D6)</b></td>
      <td>1,000 m / 6,000 m</td>
    </tr>
  </tbody>
</table>

<br>
<hr>
<br>

<a name="ctd-39-do"></a>
<h2>SBE CTD 39 Dissolved Oxygen Sensor (Optional)</h2>

<div align="center">
  <!-- Primary Assembly Photo Placeholder -->
  [DROP CTD 39 OVERVIEW PHOTO HERE]
  <br><br>
  <!-- Installed Detail Photo Placeholder -->
  [DROP CTD 39 MOUNTING DETAIL PHOTO HERE]
</div>

<br>

<p><b>System Overview:</b> A high-accuracy, fast-sampling temperature and pressure recorder featuring internal logging memory and external power/data interfaces. Designed for long-duration fixed deployments, net monitoring, or towed vehicle payloads.</p>

<h3>CTD 39 Preparation & Mounting Steps</h3>
<ol>
  <li>Prior to attaching the Sea-Bird 39 CTD to the starboard forward vertical frame rail, verify the bracket has rubber gaskets glued inside.</li>
  <li>Orient the sensor so the bulkhead connector faces downwards and position it into the bracket.</li>
  <li>Apply Aqua Shield grease over all bolt threads prior to installing hardware.</li>
  <li>Thread four 7/16"-14 screws through the bracket and secure with a stainless steel washer on the inside, lock washer in the middle, and hex nut on the outside.</li>
  <li>Tighten all nuts evenly using 7/16" ratcheting wrenches.</li>
</ol>

<br>

<h3>Sea-Bird Scientific SBE 39plus Specifications</h3>

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
      <td><b>Communication</b></td>
      <td>RS-232</td>
      <td><b>Sampling Rate</b></td>
      <td>Up to 2 Hz (2 samples/sec)</td>
    </tr>
    <tr>
      <td><b>Depth Rating</b></td>
      <td>600 m</td>
      <td><b>Accuracy (Temp)</b></td>
      <td>&plusmn;0.002 &deg;C (-5 to +35 &deg;C)</td>
    </tr>
    <tr>
      <td><b>Housing Material</b></td>
      <td>Plastic or Titanium</td>
      <td><b>Accuracy (Pressure)</b></td>
      <td>&plusmn;0.1% of full scale range</td>
    </tr>
    <tr>
      <td><b>Connector Type</b></td>
      <td>SubConn MCBH</td>
      <td><b>Memory Capacity</b></td>
      <td>9.5M samples (T); 5.5M (TD)</td>
    </tr>
  </tbody>
</table>

<ul>
  <li><a href="https://www.seabird.com/hubfs/Product%20Assets/SBE%2039plus/Manuals/39plusrevB.pdf?hsLang=en" target="_blank">SBE 39plus Technical Manual</a></li>
</ul>

<br>
<hr>
<br>

<a name="ctd-49-fastcat"></a>
<h2>SBE CTD 49 FastCAT Sound Speed Sensor</h2>

<div align="center">
  <!-- Primary Assembly Photo Placeholder -->
  [DROP CTD 49 OVERVIEW PHOTO HERE]
  <br><br>
  <!-- Installed Detail Photo Placeholder -->
  [DROP CTD 49 MOUNTING DETAIL PHOTO HERE]
</div>

<br>

<p><b>System Overview:</b> An integrated CTD sensor designed for modular payload integration on towed vehicles. Features a pump-controlled TC-ducted flow cell that minimizes salinity spiking, sampling at 16 Hz for high spatial resolution of oceanographic gradients.</p>

<h3>CTD 49 Preparation & Mounting Steps</h3>
<ol>
  <li>Verify that the plastic mounting brackets on the port forward vertical frame rail have rubber barrier gaskets applied.</li>
  <li>Seat the FastCAT sensor into the bracket with the internal pump facing downwards.</li>
  <li>Apply Aqua Shield anti-corrosion grease to all screw threads.</li>
  <li>Install four 9/16"-12 partial thread bolts fitted with a stainless steel washer inside, lock washer in the middle, and hex nut outside.</li>
  <li>Tighten all four mounting points securely using 9/16" ratcheting wrenches.</li>
</ol>

<br>

<h3>Sea-Bird Scientific SBE 49 FastCAT Specifications</h3>

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
      <td><b>Communication</b></td>
      <td>RS-232C</td>
      <td><b>Sampling Rate</b></td>
      <td>16 Hz (16 samples/sec)</td>
    </tr>
    <tr>
      <td><b>Depth Rating</b></td>
      <td>350 m</td>
      <td><b>Accuracy (Conductivity)</b></td>
      <td>&plusmn;0.0003 S/m</td>
    </tr>
    <tr>
      <td><b>Power Input</b></td>
      <td>0.75 A @ 9–24 VDC</td>
      <td><b>Accuracy (Temperature)</b></td>
      <td>&plusmn;0.002 &deg;C</td>
    </tr>
    <tr>
      <td><b>Connector Type</b></td>
      <td>SubConn MCBH</td>
      <td><b>Accuracy (Pressure)</b></td>
      <td>&plusmn;0.1% of full scale range</td>
    </tr>
  </tbody>
</table>

<ul>
  <li><a href="https://www.seabird.com/hubfs/Product%20Assets/SBE%2049/Datasheets/SBE%2049DS53May25.pdf?hsLang=en" target="_blank">SBE 49 FastCAT Datasheet</a></li>
</ul>

<br>
<hr>
<br>

<a name="eco-triplet"></a>
<h2>ECO V2 Triplet Puck Fluorometer</h2>

<div align="center">
  <!-- Primary Assembly Photo Placeholder -->
  [DROP ECO TRIPLET OVERVIEW PHOTO HERE]
  <br><br>
  <!-- Installed Detail Photo Placeholder -->
  [DROP ECO TRIPLET MOUNTING DETAIL PHOTO HERE]
</div>

<br>

<p><b>System Overview:</b> Multi-parameter optical sensor providing 16-bit resolution across optical backscatter and fluorescence channels. Designed for biological monitoring, turbidity, and chlorophyll sampling with potted optics for long-term calibration stability.</p>

<h3>Fluorometer Preparation & Mounting Steps</h3>
<ol>
  <li>Ensure rubber barrier gaskets are glued inside the mounting brackets attached to the center forward horizontal expansion rails.</li>
  <li>Mount the ECO-Triplet puck with its bulkhead connector facing towards the center of HabCam, resting immediately above the frame crossbar.</li>
  <li>Apply Aqua Shield grease to all screw threads prior to fastening.</li>
  <li>Insert two 9/16"-12 partial thread bolts and secure with a stainless washer, lock washer, and hex nut per bolt.</li>
  <li>Tighten the assembly using 9/16" ratcheting wrenches.</li>
</ol>

<br>

<h3>HabCam Optical Sensor Configuration (Model BBFL2, S/N: 627)</h3>

<table>
  <thead>
    <tr>
      <th align="left">Channel</th>
      <th align="left">Target Parameter</th>
      <th align="left">Wavelength</th>
      <th align="left">Sensitivity / Typical Range</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Channel 1</b></td>
      <td>Scattering (NTU)</td>
      <td>650 nm</td>
      <td>Sensitivity: ~0.003 m<sup>-1</sup> | Range: 0–5 m<sup>-1</sup></td>
    </tr>
    <tr>
      <td><b>Channel 2</b></td>
      <td>Chlorophyll (EX/EM)</td>
      <td>695 nm</td>
      <td>Sensitivity: 0.025 &mu;g/l | Range: 0–50 &mu;g/l</td>
    </tr>
    <tr>
      <td><b>Channel 3</b></td>
      <td>fDOM</td>
      <td>460 nm</td>
      <td>Sensitivity: 0.28 ppb/count | Range: 0–375 ppb</td>
    </tr>
  </tbody>
</table>

<br>
<hr>
<br>

<a name="main-electronics-bottle"></a>
<h2>Main Electronics Bottle Servicing & Vacuum Seal Procedure</h2>

<div align="center">
  <!-- Primary Assembly Photo Placeholder -->
  [DROP MAIN ELECTRONICS BOTTLE OVERVIEW PHOTO HERE]
  <br><br>
  <!-- Installed Detail Photo Placeholder -->
  [DROP MAIN BOTTLE DISASSEMBLY PHOTO HERE]
</div>

<br>

<h3>1. Disassembly & Removal from Chassis</h3>
<ol>
  <li>Ensure vehicle power is completely shut down before touching any electrical connections.</li>
  <li>Disconnect all external cables from the bulkhead connectors on both endcaps.</li>
  <li>Remove the top retaining clamps using 9/16" ratcheting wrenches.</li>
  <li>Position the main bottle cradle onto a clean worktable.</li>
  <li>Using two technicians, gently slide the main bottle out of the rear of the vehicle frame (one person climbing inside/above the frame guiding, the second holding weight from behind) and place it into the table cradle.</li>
  <li>Inspect frame clamps for wear. If replacing clamps, secure rubber liners to the inside faces using Pliobond 35 adhesive.</li>
</ol>

<br>

<div align="center">
  <!-- Chassis Inspection Photo Placeholder -->
  [DROP BOTTLE CRADLE PHOTO HERE]
  <br><br>
  <!-- Internal Components Photo Placeholder -->
  [DROP INTERNAL CHASSIS DESICCANT PHOTO HERE]
</div>

<br>

<h3>2. Internal Servicing, Desiccant & Fuse Verification</h3>
<ol>
  <li>Remove the four 32" threaded rods along the outer bottle body using 7/16" ratcheting wrenches.</li>
  <li>Use a 3/16" hex key to loosen the vacuum purge plug on the back endcap (listen for air entering the housing).</li>
  <li>Remove the forward endcap first (marked "open this end first" as it is NOT mechanically tethered to the internal chassis). Use a rubber mallet to lightly tap the outer rim to break the O-ring seal.</li>
  <li>Disconnect internal Ethernet lines, two mini AMP connectors, and three large AMP power connectors before lifting the endcap away. Set down carefully to avoid stressing bulkhead pins.</li>
  <li>Tap the rear endcap rim with a mallet to loosen, stand the housing vertically on a soft pad, and carefully extract the chassis onto the cradle.</li>
  <li>Unscrew the underside prototype board, replace desiccant packs with four fresh large packs using painter's tape, and reattach the board.</li>
  <li>Verify all power line fuses using a multimeter set to continuity mode (confirming audible beeps across every fuse).</li>
</ol>

<br>

<div align="center">

<p><b>FUSE CONTINUITY VERIFICATION</b></p>
<!-- Fuse Block Photo Placeholder -->
[DROP FUSE BLOCK TEST PHOTO HERE]

</div>

<br>

<h3>3. Reassembly, O-Ring Maintenance & 24-Hour Vacuum Test</h3>
<ol>
  <li>Perform a bench test: connect 3-pin power and optical fiber (Port 3), power up step-up transformer (Input FIRST, then Output), and verify connection to both Moxa servers and connected sensors via the Engineering GUI. Power down (Output FIRST, then Input).</li>
  <li>Remove endcap O-rings, clean off old grease, and wipe down lightly with isopropyl alcohol using a paper towel (avoid over-applying alcohol).</li>
  <li>Inspect O-rings for nicks or debris, apply a uniform coat of Molykote 55 grease to O-rings and inner housing sealing surfaces.</li>
  <li>Carefully slide internal chassis into housing, reconnect internal wiring connectors, align endcap handles with rod holes, and press endcaps firmly until fully seated.</li>
  <li>Reinstall outer threaded rods and verify handle integrity.</li>
  <li>Attach vacuum pump fixture to the purge port, draw vacuum down to <b>16 inHg</b>, seal valve, and shut off pump.</li>
  <li><b>Hold vacuum for 24 hours</b> and verify that gauge reading remains steady at 16 inHg before approving for sea operations.</li>
  <li>Apply dielectric grease to all female cable connector faces, align keyways, press until a characteristic cracking/seating sound is heard, and hand-tighten locking collars.</li>
</ol>

<br>
<hr>
<br>

<a name="mako-cameras"></a>
<h2>Allied Vision Mako G-234 Cameras (x2)</h2>

<div align="center">
  <!-- Primary Assembly Photo Placeholder -->
  [DROP MAKO CAMERAS OVERVIEW PHOTO HERE]
  <br><br>
  <!-- Installed Detail Photo Placeholder -->
  [DROP MAKO CAMERAS MOUNTING DETAIL PHOTO HERE]
</div>

<br>

<p><b>System Overview:</b> High-performance 2.35 megapixel GigE machine vision cameras utilizing Type 1/1.2 Sony IMX249 CMOS sensors with global shutters. Mounted downward in stereo configuration to capture synchronized seabed imagery at frame rates up to 41.5 fps.</p>

<h3>Allied Vision Mako G-234 System Specifications</h3>

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
      <td>1936 &times; 1216 (2.40 MP)</td>
      <td><b>Sensor Model</b></td>
      <td>Sony IMX249 CMOS</td>
    </tr>
    <tr>
      <td><b>Frame Rate</b></td>
      <td>41 fps @ full resolution</td>
      <td><b>Shutter Type</b></td>
      <td>Global Shutter (GS)</td>
    </tr>
    <tr>
      <td><b>Digital Interface</b></td>
      <td>IEEE 802.3 1000BASE-T (PoE)</td>
      <td><b>Pixel Size</b></td>
      <td>5.86 &mu;m &times; 5.86 &mu;m</td>
    </tr>
    <tr>
      <td><b>Exposure Time Range</b></td>
      <td>16 &mu;s to 85 s</td>
      <td><b>Power Supply</b></td>
      <td>10.8 to 26.4 VDC AUX / PoE</td>
    </tr>
  </tbody>
</table>

<br>
<hr>
<br>

<a name="dragonfish-strobes"></a>
<h2>Arctic Rays (INKFISH) Dragonfish Mini LED Strobes (x4)</h2>

<div align="center">
  <!-- Primary Assembly Photo Placeholder -->
  [DROP DRAGONFISH STROBES OVERVIEW PHOTO HERE]
  <br><br>
  <!-- Installed Detail Photo Placeholder -->
  [DROP DRAGONFISH STROBES MOUNTING DETAIL PHOTO HERE]
</div>

<br>

<p><b>System Overview:</b> High-output 30,000-lumen compact LED strobe units featuring patented internal driver electronics. Deliver rapid-repetition pulsed flash illumination synchronized with stereo camera exposure triggers.</p>

<h3>Dragonfish Mini Technical Specifications</h3>

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
      <td>Luminous Output<br>Color Temp<br>Beam Angle</td>
      <td>30,000 Lm @ 5,700K<br>5700K standard (2700K–6500K optional)<br>100&deg; FWHM standard</td>
    </tr>
    <tr>
      <td><b>Electrical</b></td>
      <td>Operating Voltage<br>Max Power / Current<br>Pulse Duration / Rep Rate</td>
      <td>9–35 VDC<br>16 W pulsed max | 650 mA @ 24V recharge<br>0.1–5 ms duration | 2 Hz standard (10 Hz max)</td>
    </tr>
    <tr>
      <td><b>Control & Mechanical</b></td>
      <td>Trigger Input<br>Weight / Materials<br>Depth Rating</td>
      <td>5V TTL active-low logic trigger<br>350g (air) / 175g (water) | 6061-T6 Al<br>300 m (984 ft) operational depth</td>
    </tr>
  </tbody>
</table>

<br>
<hr>
<br>

<a name="attitude-sensor"></a>
<h2>Microstrain AHRS Sensor (3DM-GX5-25-HRS) - Attitude Sensor</h2>

<div align="center">
  <!-- Primary Assembly Photo Placeholder -->
  [DROP ATTITUDE SENSOR OVERVIEW PHOTO HERE]
  <br><br>
  <!-- Installed Detail Photo Placeholder -->
  [DROP ATTITUDE SENSOR MOUNTING DETAIL PHOTO HERE]
</div>

<br>

<p><b>System Overview:</b> Industrial-grade 9-axis Attitude and Heading Reference System (AHRS). Uses triaxial accelerometers, gyroscopes, and magnetometers processed through an onboard Extended Kalman Filter (EKF) to deliver high-accuracy pitch, roll, and yaw orientation data over serial lines.</p>

<h3>Microstrain 3DM-GX5-25-HRS Specifications</h3>

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
      <td><b>Sensor Type</b></td>
      <td>9-axis IMU / AHRS</td>
      <td><b>Supply Voltage</b></td>
      <td>4.25 to 36 VDC</td>
    </tr>
    <tr>
      <td><b>Communication</b></td>
      <td>RS-232, USB</td>
      <td><b>Operating Temp</b></td>
      <td>-40 &deg;C to +85 &deg;C</td>
    </tr>
    <tr>
      <td><b>Accelerometer Resolution</b></td>
      <td>0.02 mg</td>
      <td><b>Sensing Axes</b></td>
      <td>X, Y, Z</td>
    </tr>
  </tbody>
</table>

<br>
<hr>
<br>

<a name="benthos-altimeter"></a>
<h2>Teledyne Benthos PSA 916 Sonar Altimeter</h2>

<div align="center">
  <!-- Primary Assembly Photo Placeholder -->
  [DROP BENTHOS ALTIMETER OVERVIEW PHOTO HERE]
  <br><br>
  <!-- Installed Detail Photo Placeholder -->
  [DROP BENTHOS ALTIMETER MOUNTING DETAIL PHOTO HERE]
</div>

<br>

<p><b>System Overview:</b> Programmable 200 kHz acoustic sonar altimeter housed in hard-anodized marine-grade aluminum. Measures precise vehicle height above seafloor by calculating round-trip pulse travel times, providing real-time altitude telemetry to pilot navigation GUIs.</p>

<h3>Teledyne Benthos PSA 916 Specifications</h3>

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
      <td><b>Range & Resolution</b></td>
      <td>100 m full scale | 1 cm (RS-232)</td>
    </tr>
    <tr>
      <td><b>Beam Width</b></td>
      <td>14&deg; conical typical</td>
      <td><b>Operating Depth</b></td>
      <td>6,000 m</td>
    </tr>
    <tr>
      <td><b>Pulse Length / Rep Rate</b></td>
      <td>250 &mu;s | 5 pps or external</td>
      <td><b>Power Required</b></td>
      <td>7 to 24 VDC (60 mA @ 15 VDC)</td>
    </tr>
    <tr>
      <td><b>Signal Outputs</b></td>
      <td>RS-232 Digital / 0–5 VDC Analog</td>
      <td><b>Dimensions / Weight</b></td>
      <td>2.25" dia &times; 9.75" L | 0.63 kg (air)</td>
    </tr>
  </tbody>
</table>

<br>
<hr>


<div align="center">

<br>
<hr>

**Navigation:** [Home](README.md) | [01 Overview](01-overview-and-species.md) | **02 Hardware** | [03 Checklists](03-checklists-and-calibration.md) | [04 Software](04-software-and-data.md) | [05 Sea Ops](05-staging-and-sea-ops.md)

</div>
