# HabCam Electrical Schematics & Network Architecture

<br>

## Master Table

<table class="table table-striped">
  <thead>
    <tr>
      <th align="left">Section</th>
      <th align="left">Description</th>
      <th align="left">Primary Components / Schematics</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="#network-connectivity"><b>Network Connectivity & CWDM</b></a></td>
      <td>Copper-to-fiber multiplexing and subsea telemetry pipeline.</td>
      <td>Mako Cameras, BlueView Sonar, SFP Media Converters, OptiLink</td>
    </tr>
    <tr>
      <td><a href="#ethernet-schematics"><b>Ethernet Electrical Routing</b></a></td>
      <td>Dual switch architecture inside the Electronics Bottle.</td>
      <td>Ubiquiti Switches, SubConn DBH13M Data Breakouts, Test Ports</td>
    </tr>
    <tr>
      <td><a href="#bulkhead-specs"><b>Bulkhead Specifications</b></a></td>
      <td>Pinouts, O-rings, and thread specs for Electronics Bottle bulkheads.</td>
      <td>SubConn MCBH3M, MCBH4M, MCBH6M, DBH13M, OptiLink A-04-BCR</td>
    </tr>
    <tr>
      <td><a href="#fiber-cabling"><b>Internal Fiber Cabling</b></a></td>
      <td>Media conversion, SFP transceivers, and CWDM channels.</td>
      <td>IMC IE-ModeConverter, AFL CWDM Mux, L-Com ST Barrels</td>
    </tr>
    <tr>
      <td><a href="#endcap-placements"><b>Bottle Endcap Layouts</b></a></td>
      <td>External port assignments for Electronics & Expansion bottles.</td>
      <td>Front/Back Endcaps (J1–J22, J50–J52), Expansion Bottle (J1–J11)</td>
    </tr>
    <tr>
      <td><a href="#serial-ports"><b>Serial Port Arrays (INST 1–12)</b></a></td>
      <td>Moxa N-Port servers and regulated DC power buses.</td>
      <td>Moxa 5650-8-DT, Terminal Blocks T5–T16, SubConn MCBH6M</td>
    </tr>
    <tr>
      <td><a href="#ac-power-strobes"><b>AC Power & Strobe Control</b></a></td>
      <td>AC distribution, DC rail rectifiers, and strobe timing bus.</td>
      <td>Astrodyne PS1–PS4, Sealevel CC320, MVS 5000 Strobes</td>
    </tr>
    <tr>
      <td><a href="#subsystem-housings"><b>Sensor Bottles & Housings</b></a></td>
      <td>Wiring schematics for individual pressure housings.</td>
      <td>Strobe Bottle, Attitude Bottle, Prosilica & Mako Camera Housings</td>
    </tr>
    <tr>
      <td><a href="#sensor-cables"><b>CTD & Environmental Cables</b></a></td>
      <td>Dedicated cable assemblies for oceanographic sampling.</td>
      <td>Sea-Bird SBE 37/49 CTD, ECO-Triplet Fluorometer Cable</td>
    </tr>
  </tbody>
</table>

<br>
<hr>
<br>

<a name="network-connectivity"></a>

## HabCam Network Connectivity & Telemetry Architecture

The HabCam network architecture details the end-to-end data conversion and multiplexing pipeline. High-resolution subsea imaging, acoustic sonar, and serial instrument telemetry convert from copper electrical signals into Coarse Wavelength Division Multiplexing (CWDM) optical signals for long-distance transmission across the primary tow cable umbilical.

<div align="center">
<img width="1268" height="823" alt="Network Connectivity" src="https://github.com/user-attachments/assets/b6d04387-a717-4559-a1af-26f3b52abf03" />
  <p><i>Figure 1.1: HabCam Subsea Network Connectivity & CWDM Conversion Schematic.</i></p>
</div>

<br>

### CWDM Wavelength Allocation & Subsystem Routing

<table class="table table-striped">
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

## Ethernet Electrical Schematic & Internal Switch Routing

Routing across dual Ethernet switches inside the Electronics Bottle handles internal data switching, diagnostic test ports, and subsea 13-pin connector breakouts (Data1Net and Data2Net).

<div align="center">
<img width="1276" height="841" alt="Ethernet Pinout" src="https://github.com/user-attachments/assets/511180be-6801-4f53-931a-c948b1439548" />
  <p><i>Figure 2.1: Dual Switch Ethernet Architecture & Subsea Pinout Breakout.</i></p>
</div>

<br>

### Switch Port Assignment Matrix

<table class="table table-striped">
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

## Bulkhead Connector Specifications & Pinout Reference

Master technical specifications for all SubConn bulkhead connectors installed on the Electronics Bottle endcaps.

<div align="center">
<img width="1270" height="829" alt="Bulkhead Pinouts" src="https://github.com/user-attachments/assets/6d8d0149-95b8-44a0-a048-a19b268fa883" />
  <p><i>Figure 3.1: SubConn Bulkhead Face Views and Hardware Specifications.</i></p>
</div>

<br>

### Bulkhead Hardware & Pinout Specifications

* **3-Pin AC Input Bulkhead (J1):**
  * **Hardware Spec:** SubConn MCBH3M-SS | **Thread:** 7/16-20 UNF-2A | **O-Ring:** 2-014
  * **Pinout:** Pin 1: Ground Return | Pin 2: AC (Hot) | Pin 3: AC (Neutral)
* **4-Pin Strobe Bulkheads (J5–J8):**
  * **Hardware Spec:** SubConn MCBH4M-SS | **Thread:** 7/16-20 UNF-2A | **O-Ring:** 2-014
  * **Pinout:** Pin 1: Strobe Signal Return | Pin 2: Strobe Signal | Pin 3: AC (Hot) | Pin 4: AC (Neutral)
  * **Power Rating:** MVS-5002 Strobe (12V @ 4.5A) & fan (12V @ 0.5A) via Astrodyne LPR75-12 (75W total).
* **6-Pin Serial Bulkheads (J11–J22):**
  * **Hardware Spec:** SubConn MCBH6M-SS | **Thread:** 7/16-20 UNF-2A | **O-Ring:** 2-014
  * **Pinout:** Pin 1: Power Return | Pin 2: Power Output #1 | Pin 3: Power Output #2 | Pin 4: Instrument Rx (Tx by Moxa) | Pin 5: Instrument Tx (Rx by Moxa) | Pin 6: Comms Return
  * **Power Limits (Per Port):** 100W @ 48V (2A), 75W @ 24V (3A), 35W @ 12V (3A), 15W @ 5V (3A).
  * **Total Serial Bus Power Available:** 100W (48V), 90W (24V), 100W (12V), 70W (5V).
* **13-Pin Ethernet / Camera Bulkheads (J3, J4, J9, J10):**
  * **Hardware Spec:** SubConn DBH13M-SS | **Thread:** 1/2-20 UNF-2A | **O-Ring:** 2-015
  * **Camera Pinout (J3, J4):** Pin 1: Camera Return | Pin 3: Strobe Signal | Pins 4–11: Ethernet Color Pairs | Pin 12: Camera Power | Pin 13: Strobe Return
  * **Ethernet Pinout (J9, J10):** Pins 1–3: Power Conductors (#18 BLK, #18 ORN, #18 WHT) | Pins 4–11: Cat6 Ethernet Pairs | Pins 12–13: Main Power Rails (#18 RED, #18 GRN)
* **SubConn OptiLink Fiber Bulkhead (J2):**
  * **Hardware Spec:** SubConn OptiLink A-04-BCR | **Thread:** 7/8-14 | **O-Rings:** 2-019 & 2-022
  * **Capacity:** 4 Single-Mode (SM) Optical Fiber channels.

<br>
<hr>
<br>

<a name="fiber-cabling"></a>

## Electronics Bottle Internal Fiber Cabling

Details internal optical media conversion, CWDM wavelength multiplexing, and fiber pass-through routing inside the Electronics Bottle to bridge copper Ethernet devices to the SubConn OptiLink subsea bulkhead.

<div align="center">
<img width="1280" height="880" alt="Bottle Fiber Cabling" src="https://github.com/user-attachments/assets/5123f9c5-6b91-48be-9f4a-656a459024e3" />
  <p><i>Figure 4.1: Internal Optical Media Conversion & CWDM Routing.</i></p>
</div>

<br>

### Fiber Channel Routing Map

<table class="table table-striped">
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

## Bottle Endcap Connector Placements & Designation Maps

External bulkhead connector placements, designations, part numbers, and gender specifications for both the Electronics Bottle and Expansion Bottle.

<div align="center">
<img width="1258" height="819" alt="Endcap Connector Placement" src="https://github.com/user-attachments/assets/100949ed-dd02-4bee-9d20-c77d0e01dbc9" />
  <p><i>Figure 5.1: Electronics Bottle Front and Back Endcap Bulkhead Layouts.</i></p>
</div>

<br>

### Electronics Bottle Bulkhead Assignments

<table class="table table-striped">
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

### Expansion Bottle Bulkhead Assignments

<table class="table table-striped">
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

## Serial Instrumentation Port Arrays (INST 1–12)

Internal power distribution buses, Moxa N-Port serial server interfaces, and pin routings for auxiliary instrumentation ports INST 1 through INST 12 (J11–J22) inside the Electronics Bottle.

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

### Serial Port Wiring & Terminal Block Matrix

<table class="table table-striped">
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

## AC Power Distribution & MVS 5000 Strobe Controls

Governs high-voltage AC input distribution, internal DC power generation (5V, 12V, 24V, 48V), system cooling fans, camera power control, and flash pulse triggers for four MVS 5000 strobe units.

<div align="center">
<img width="1254" height="834" alt="AC Power" src="https://github.com/user-attachments/assets/c943e173-9c90-4b22-b80e-8f91a35f3040" />
  <p><i>Figure 7.1: AC Power Distribution, Rectifiers, and Strobe Control Schematic.</i></p>
</div>

<br>

### Internal Rectifiers & Interface Allocation

* **AC Main Input (J1):** High-voltage AC enters via SubConn MCBH3M-SS with a 4A slow-blow fuse (F1: Littelfuse 03540821ZXBL) guarding the main AC rails.
* **Internal DC Regulators:**
  * **PS1 (Astrodyne RS150-48):** Generates +48V DC (Fused via F2 @ 1A Fast) &rarr; Terminal Strip T1.
  * **PS2 (Astrodyne RS150-24):** Generates +24V DC (Fused via F3 @ 1A Fast) &rarr; Terminal Strip T2.
  * **PS3 (Astrodyne RS150-12):** Generates +12V DC (Fused via F2-3 @ 8A Fast) &rarr; Terminal Strip T3.
  * **PS4 (Astrodyne RS100-5):** Generates +5V DC (Fused via F4-5 @ 8A Fast) &rarr; Terminal Strip T4.
* **System Cooling:** Dual Mechatronics GDA6025-12BB 12V cooling fans equipped with tachometer feedback lines.
* **Timing Unit (U1):** Sealevel CC320 timing interface on the Timing Net with optical trigger outputs (Out1–Out8) pulled up via 1.2k&Omega; resistors.

<br>

### Strobe & Camera Bulkhead Connections

<table class="table table-striped">
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

## Sensor Bottles, Strobe Units & Camera Housings

### Strobe Bottle Internal Schematic

<div align="center">
<img width="1234" height="838" alt="Strobe Bottle" src="https://github.com/user-attachments/assets/16c26846-5ed4-4318-ac23-aa0c5d430d06" />
  <p><i>WHOI Strobe Bottle Internal Electrical Schematic.</i></p>
</div>

<br>

Details AC power conversion, thermal regulation, opto-isolated trigger pulse amplification, and driving circuit connections for the Perkin-Elmer MVS-5002 strobe unit:

* **Internal Power Converter (PS1):** Astrodyne LPR75-12 converting high-voltage AC into regulated +12V DC.
* **Trigger Conditioning:** Dual NPN transistors (Q1, Q2 2N3904) driving a Perkin-Elmer MVS-5002 optocoupler stage with a 150&Omega; current-limiting resistor. Nominal trigger: 5V @ 20mA (4.5V @ 18mA minimum).
* **Internal Cooling:** Sunon KDE1206PHV2 12V fan drawing air out through housing side vents.

<br>

### Attitude Bottle Internal Schematic

<div align="center">
<img width="1226" height="827" alt="Attitude Bottle" src="https://github.com/user-attachments/assets/eac244c8-2b77-4025-a97c-7e7b2bc27c7c" />
  <p><i>Figure WHOI Attitude Bottle (Microstrain 3DM-GX3-25 IMU) Schematic.</i></p>
</div>

<br>

<table class="table table-striped">
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

### Camera Synchronization Bus Circuit Analysis

<div align="center">
<img width="1206" height="804" alt="Camera Trigger" src="https://github.com/user-attachments/assets/8be62985-f4e8-4581-846c-8b9f9c71552a" />
  <p><i>Optically Isolated Shared Camera / Strobe Synchronization Bus.</i></p>
</div>

<br>

* **Bus Bias:** Single 2050&Omega; (0.5W) pull-up resistor to +24V DC in the Electronics Bottle.
* **Active Low State (Trigger Pulled Low):** Line near 0V; 11.7mA through pull-up resistor; 0mA through camera LEDs; 0.3mA through each strobe; total collector sinking current = 12.9mA.
* **Inactive High State (Floating High):** Line at 3.4V; 10.1mA through pull-up resistor; 5.3mA through each camera input LED (exceeds drive threshold).
* **Worst-Case Single Camera Load:** Single-camera / 4-strobe line rises to 5.0V, delivering 9.5mA to the camera LED.

<br>

### Allied Vision Mako G-234C Camera Housing Wiring

<div align="center">
<img width="1195" height="883" alt="Camera Wiring" src="https://github.com/user-attachments/assets/1d0c551d-283e-417a-8295-8503d2ee9ade" />
  <p><i>Allied Vision Mako G-234C Camera Housing Electrical Wiring Diagram.</i></p>
</div>

<br>

<table class="table table-striped">
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

## CTD & Environmental Sensor Cable Harnesses

### Sea-Bird SBE 37 / SBE 49 CTD Cable Assembly

<div align="center">
<img width="1234" height="881" alt="CTD Wiring" src="https://github.com/user-attachments/assets/e79fb571-f2c0-4c4f-bfd4-d1134a0c35e7" />
  <p><i>Sea-Bird SBE 37/49 CTD Sensor Cable Schematic.</i></p>
</div>

<br>

<table class="table table-striped">
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

### ECO-Triplet Fluorometer Cable Assembly

<div align="center">
<img width="1234" height="881" alt="Eco-Triplet Wiring" src="https://github.com/user-attachments/assets/b112bbf6-75a1-43c8-b4a5-00ff100705ca" />
  <p><i>Figure 9.2: Sea-Bird / WET Labs ECO-Triplet Cable Schematic.</i></p>
</div>

<br>

<table class="table table-striped">
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
