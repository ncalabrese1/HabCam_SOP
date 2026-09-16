# Cable Harness Specifications

## System Overview
This slide set contains the electrical schematics, pinout diagrams, cable harness routing plans, and interconnect specifications for the Habitat Mapping Camera System (HabCam).

As a continuously towed underwater imaging vehicle operating near the seabed, the HabCam relies on oceanographic sensors, imaging systems, and acoustic tools. The cable harnesses described herein provide the link between the centralized vehicle telemetry housing, power distribution manifolds, and individual payload sensors.

## Cable Harness Design Standards
All HabCam cable assemblies are engineered to withstand prolonged immersion in seawater under hydrostatic pressure, high tension, and continuous vibration. Design criteria include:
* **Wet-Pluggable Connectors:** Utilize marine-grade wet-mate circular connectors (e.g., SubConn, Impulse, Glenair) rated for deep-water hydrostatic pressures.
* **Mechanical Protection:** Cables feature heavy-duty polyurethane or neoprene outer jackets with embedded water-blocking compounds and Kevlar strain-relief strength members.
* **Noise Mitigation:** High-speed data pairs and sensitive optical feedback lines utilize individual foil wrapping, tinned-copper braided shielding, and isolated analog/digital ground returns to eliminate EMI and crosstalk from power lines.
* **Color-Coded Conductor Wiring:** Standardized color coding (following marine instrumentation standards) is maintained across all sub-assemblies to facilitate rapid deck repairs.

## Maintenance, Deck Handling & Quality Assurance
To ensure system reliability during sea trials and survey operations, technicians must adhere to the following servicing guidelines:

**Connector Care & Lubrication:**
* Inspect rubber faces and O-rings for grit, salt crystals, or hair prior to deployment.
* Apply a light coating of Dow Corning 111 silicone grease to neoprene connector faces.
* Never use petroleum-based lubricants, as they degrade neoprene seals.

**Bend Radius & Mechanical Anchoring:**
* Maintain a minimum static bend radius of 6x the cable diameter, and a dynamic bend radius of 10x the cable diameter.
* Secure all cables along the 304 Stainless Steel frame using rubber-lined P-clamps and heavy-duty UV-resistant cable ties.

**Dummy Plug Usage:**
* Always cap un-mated bulkhead connectors with protective dummy plugs immediately upon disconnect on deck to protect pin contacts from salt spray.

<br>
<hr>
<br>

## Cable Harness Master Reference

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
