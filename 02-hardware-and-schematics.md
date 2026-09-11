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

## Frame Schematics & Physical Envelope

### Structural Core & Design Principles
* **Primary Frame Architecture:** Built from 304 Stainless Steel welded tubular/pipe roll-cage construction for high tensile strength, impact toughness, and chassis rigidity[cite: 2].
* **Corrosion Mitigation:** Exposed stainless steel structures utilize sacrificial zinc/aluminum anodes and marine-grade anti-corrosion coatings to combat pitting and galvanic action[cite: 2].
* **Fasteners & Hardware:** Passivated 316/304 Stainless Steel hardware with anti-seize provisions prevents thread galling during deck maintenance[cite: 2].
* **Hydrodynamic Tow Envelope:** Engineered to minimize roll and drag at 5–7 knot tow speeds approximately 2 meters above the seabed[cite: 2].

<br>

### Physical Specifications

| Parameter | Specification | Operational Details |
| :--- | :--- | :--- |
| **Primary Material** | 304 Stainless Steel | Welded tubular roll-cage assembly[cite: 2] |
| **Dimensions (Frame Only)** | 108.0 in x 62.0 in x 41.0 in | Core chassis clearance envelope[cite: 2] |
| **Dimensions (With Tail)** | 155.52 in x 62.0 in x 41.0 in | Total operational length with elevator doors[cite: 2] |
| **Max Depth Rating** | 110 to 113 meters (360–370 ft) | Structural frame and housing pressure limit[cite: 2] |
| **Operational Tow Speed** | 5 to 7 knots | Hydrodynamic flight stability window[cite: 2] |

<br>

---

<br>

## Cable Schematics & Pinout Configurations

### Cable Harness Design Standards
* **Wet-Pluggable Interconnects:** Utilizes marine-grade wet-mate circular connectors (SubConn, Impulse, Teledyne) rated for subsea hydrostatic pressures[cite: 2].
* **Mechanical Protection:** Heavy-duty polyurethane/neoprene jackets with water-blocking compounds and Kevlar strain-relief members[cite: 2].
* **Bend Radius Limits:** Static bend radius minimum 6x cable diameter; dynamic bend radius minimum 10x cable diameter[cite: 2].
* **Care & Lubrication:** Clean rubber faces with isopropyl alcohol and lubricate exclusively with Dow Corning 111 silicone grease (never petroleum products)[cite: 2].

<br>

### Subsea Cable Pinout Reference

| Harness Assembly | Vehicle End | Device End | Protocol / Signals | Operating Voltage |
| :--- | :--- | :--- | :--- | :--- |
| **Chanos Cable** | 13-Pin Circular (P1) | 13-Pin Circular (P2) | Biogeochemical Data & Dual Power Rails | +12 VDC[cite: 2] |
| **Camera Power Ethernet** | 13-Pin Circular (P1) | 13-Pin Rectangular (P2) | Cat6 Gigabit Ethernet, Camera Power, Strobe Sync | System Power[cite: 2] |
| **A-Sphere Cable** | SubConn MCIL4F (P1) | SubConn MCIL6F (P2) | RS-232 Serial Data (Moxa) + Power | +24 VDC[cite: 2] |
| **Microstrain AHRS** | SubConn MCIL6F (P2) | SubConn MCIL4F (P1) | RS-232 Orientation Data (Moxa) + Power | +12 VDC[cite: 2] |
| **BlueView Sonar** | SubConn DIL13M (P1) | Teledyne Impulse Titan (P2) | Multibeam Sonar Differential TX/RX + Power | 12–48 VDC[cite: 2] |
| **Sonar Altimeter** | SubConn MCIL6F (P2) | Impulse RMG-6FS (P1) | RS-232 Distance Telemetry (Moxa) + Power | +12 VDC (+6–24V)[cite: 2] |
| **Eco-Triplet Cable** | SubConn MCIL6F (P2) | SubConn MCIL6F (P1) | RS-232 Fluorometer Telemetry (Moxa) + Power | +12 VDC[cite: 2] |
| **SBE 37 / 49 CTD** | SubConn MCIL6F (J4) | SubConn MCIL4F (P4) | RS-232 Oceanographic Telemetry + Power | 9–24 VDC[cite: 2] |

<br>

---

<br>

## Electrical Schematics & Network Architecture

### Optical Telemetry & CWDM Wavelength Allocation
Coarse Wavelength Division Multiplexing (CWDM) aggregates subsea copper Ethernet data onto single-mode fiber optical channels routed through an OptiLink subsea bulkhead[cite: 2]:

* **Camera 1 (Allied Vision Mako G-234C):** Tx 1470 nm / Rx 1490 nm[cite: 2]
* **Camera 2 (Allied Vision Mako G-234C):** Tx 1510 nm / Rx 1530 nm[cite: 2]
* **Sonar Ethernet (BlueView Multibeam):** Tx 1570 nm / Rx 1550 nm[cite: 2]
* **Data Net (Moxa Serial & Switch Bus):** Tx 1610 nm / Rx 1590 nm[cite: 2]

<br>

### Main Electronics Bottle Bulkhead Assignments

#### Front Endcap (Power, Imaging, Strobes & Fiber)
* **J1 (AC Power In):** SubConn MCBH3M-SS (3 pins: Ground, Hot, Neutral)[cite: 2]
* **J2 (Main Fiber Input):** SubConn OptiLink A-04-BCR (4 Single-Mode Fibers)[cite: 2]
* **J3 (Camera #1):** SubConn DBH13M-SS (13 pins: Gigabit Ethernet, Camera Power, Strobe Sync)[cite: 2]
* **J4 (Camera #2):** SubConn DBH13M-SS (13 pins: Gigabit Ethernet, Camera Power, Strobe Sync)[cite: 2]
* **J5–J8 (Strobes #1 to #4):** SubConn MCBH4M-SS (4 pins: High-Voltage AC & Opto-Isolated Trigger Lines)[cite: 2]
* **J50–J52 (Direct Optical Ports):** Lancer 500-BST-S1-B02-000 ST-Dry Penetrators (Camera #1, Camera #2, Sonar Fibers)[cite: 2]

#### Back Endcap (Ethernet & Serial Instrumentation)
* **J9 (Ethernet #1):** SubConn DBH13M-SS (13 pins: Primary Network Trunk)[cite: 2]
* **J10 (Ethernet #2):** SubConn DBH13M-SS (13 pins: Auxiliary Network Trunk)[cite: 2]
* **J11–J22 (Serial Ports #1 to #12):** SubConn MCBH6M-SS (6 pins: Moxa N-Port 5650 RS-232 Interfaces)[cite: 2]
  * **Pin 1:** Power Return (BLK #22)[cite: 2]
  * **Pin 2:** Power Output #1 (WHT #22)[cite: 2]
  * **Pin 3:** Power Output #2 (RED #22)[cite: 2]
  * **Pin 4:** Instrument Rx / Moxa Tx (GRN #22)[cite: 2]
  * **Pin 5:** Instrument Tx / Moxa Rx (ORG #22)[cite: 2]
  * **Pin 6:** Comms Return (BLU #22)[cite: 2]

<br>

### Expansion Bottle Connector Assignments
* **J1 (AC Power In):** SubConn MCBH3F-SS (3 pins female)[cite: 2]
* **J2 (Data Net In):** SubConn DBBH13F-SS (13 pins female)[cite: 2]
* **J3–J5 (Ethernet #2, BlueView, Ethernet #3):** SubConn DBBH13M-SS (13 pins male)[cite: 2]
* **J6 (Unused / Spare):** SubConn DBBH13M-SS (13 pins male)[cite: 2]
* **J7–J11 (Serial Ports #1 to #5):** SubConn MCBH8F-SS (8 pins female)[cite: 2]

<br>

---

<br>

## Mounting Hardware & Tooling Inventory

| Subsystem | Mounting Location | Required Hardware & Fasteners | Required Tools |
| :--- | :--- | :--- | :--- |
| **Electronics Bottle** *(1x)* | Aft Vehicle Frame | • (4x) Black Aluminum Brackets<br>• (4x) Barrier Rubber Pieces (Pliobond 35 glued)<br>• (8x) 9/16"-12 (3 ½") Partial Thread Bolts<br>• (8x) 9/16"-12 (2 ¼") Partial Thread Bolts<br>• (4x) 32" 11mm Fully Threaded Rods<br>• (6x) Plastic Washers, (10x) Steel Washers<br>• (8x) Steel Lock Nuts, (8x) Hex Nuts[cite: 2] | • 9/16" Socket & Wrench<br>• 7/16" Wrench<br>• 14mm Wrench[cite: 2] |
| **BlueView Sonar** *(1x)* | Forward Vehicle Frame | • (4x) Steel Brackets<br>• (4x) Barrier Rubber Pieces<br>• (6x) 9/16"-12 (3 ½") Steel Partial Thread Bolts<br>• (4x) 9/16"-12 (2 ¼") Steel Partial Thread Bolts<br>• (20x) 3/16" Steel Washers<br>• (10x) Steel Lock Nuts, (10x) Hex Nuts[cite: 2] | • 9/16" Socket & Wrench<br>• 14mm Wrench<br>• Aqua Shield Grease[cite: 2] |
| **CTD 39 Oxygen** *(1x)* | Starboard Forward Rail | • (2x) UHMW Brackets, (2x) Plastic Brackets<br>• (4x) Barrier Rubber Pieces<br>• (4x) 7/16"-14 (4 ¾") Steel Partial Thread Bolts<br>• (2x) 7/16"-14 (1") Steel Full Thread Bolts<br>• (3x) 3/16" (1") Socket Head Screws<br>• (10x) Steel Washers, (6x) Lock Nuts, (2x) Hex Nuts[cite: 2] | • 7/16" Socket & Wrench<br>• 11mm Wrench<br>• Hex Key Set (1/4"–1/16")[cite: 2] |
| **CTD 49 Sound Speed** *(1x)* | Port Forward Rail | • (6x) Plastic Brackets (Sensor, Center, Frame)<br>• (8x) Barrier Rubber Pieces<br>• (8x) 9/16"-12 (2 ¾") Steel Partial Thread Bolts<br>• (16x) Steel Washers<br>• (8x) Steel Lock Nuts, (8x) Hex Nuts[cite: 2] | • 9/16" Socket & Wrench<br>• 14mm Wrench[cite: 2] |
| **Eco-Triplet Puck** *(1x)* | Center Forward Expansion Rail | • (2x) Steel Brackets (Top & Bottom)<br>• (2x) Barrier Rubber Pieces<br>• (2x) 9/16"-12 (2 ½") Steel Partial Thread Bolts<br>• (2x) 9/16"-12 (2") Steel Partial Thread Bolts<br>• (6x) Steel Washers, (4x) Lock Nuts, (2x) Hex Nuts[cite: 2] | • 9/16" Socket & Wrench<br>• 14mm Wrench[cite: 2] |
| **Habitat Cameras** *(2x)* | Center Frame Plate | • (1x) Steel Mounting Plate (16 in x 16 in)<br>• (6x) Metal Brackets<br>• (4x) M7-1.0 x 45mm Threaded Bolts<br>• (4x) 1/4"-20 (2") Socket Head Screws<br>• (8x) 1/4"-20 (1") Socket Head Screws<br>• (6x) Steel Washers, (6x) Steel Lock Nuts[cite: 2] | • Hex Key Set (1/4"–1/16")<br>• M7 / 3/16" Allen Keys[cite: 2] |
| **Strobe Lights** *(4x)* | Forward, Aft, Port, Starboard | • (8x) Steel Brackets<br>• (8x) Barrier Rubber Pieces<br>• (8x) 9/16"-12 (3 ½") Steel Partial Thread Bolts<br>• (8x) 7/16"-14 (1 ¾") Steel Partial Thread Bolts<br>• (32x) Plastic Washers, (32x) Steel Washers<br>• (16x) Steel Lock Nuts, (16x) Hex Nuts[cite: 2] | • 9/16" Socket & Wrench<br>• 7/16" Socket & Wrench<br>• 14mm / 11mm Wrenches[cite: 2] |
| **Sonar Altimeter** *(1x)* | Center Camera Plate | • (2x) Plastic Brackets<br>• (4x) Barrier Rubber Pieces<br>• (4x) 9/16"-12 (6 ½") Steel Partial Thread Bolts<br>• (8x) Steel Washers<br>• (4x) Steel Lock Nuts, (4x) Hex Nuts[cite: 2] | • 9/16" Socket & Wrench<br>• 14mm Wrench[cite: 2] |

<br>

<div align="center">

<br>
<hr>

**Navigation:** [Home](README.md) | [01 Overview](01-overview-and-species.md) | **02 Hardware** | [03 Checklists](03-checklists-and-calibration.md) | [04 Software](04-software-and-data.md) | [05 Sea Ops](05-staging-and-sea-ops.md)

</div>
