# HabCam Electrical Schematics & Network Architecture

## 1. HabCam Network Connectivity & Telemetry Architecture

The HabCam network architecture details the end-to-end data conversion and multiplexing pipeline[cite: 8]. High-resolution subsea imaging, acoustic sonar, and serial instrument telemetry convert from copper electrical signals into Coarse Wavelength Division Multiplexing (CWDM) optical signals for long-distance transmission across the primary tow cable umbilical[cite: 8].

<div align="center">
<img width="1268" height="823" alt="Network Connectivity" src="https://github.com/user-attachments/assets/b6d04387-a717-4559-a1af-26f3b52abf03" />
  <p><i>Figure 1.1: HabCam Subsea Network Connectivity & CWDM Conversion Schematic.</i></p>
</div>

<br>

### CWDM Wavelength Allocation & Subsystem Routing

| Subsystem / Device | Data Output Type | Wavelength Allocation (Tx / Rx) | Intermediate Conversion | Primary Optical Link |
| :--- | :--- | :--- | :--- | :--- |
| **Allied Vision Mako G-234C (Cam 1)** | Copper Gigabit Ethernet | Tx 1470 nm / Rx 1490 nm | SFP Media Converter | CWDM Multiplexer &rarr; OptiLink J2 |
| **Allied Vision Mako G-234C (Cam 2)** | Copper Gigabit Ethernet | Tx 1510 nm / Rx 1530 nm | SFP Media Converter | CWDM Multiplexer &rarr; OptiLink J2 |
| **Sonar / Data Switch Bus** | RS-232 / Copper Ethernet | Tx 1590 nm / Rx 1610 nm | Moxa Server &rarr; SFP Converter | CWDM Multiplexer &rarr; OptiLink J2 |

<br>
<hr>
<br>

## 2. Ethernet Electrical Schematic & Internal Switch Routing

Routing across dual Ethernet switches inside the Electronics Bottle handles internal data switching, diagnostic test ports, and subsea 13-pin connector breakouts (Data1Net and Data2Net)[cite: 8].

<div align="center">
<img width="1276" height="841" alt="Ethernet Pinout" src="https://github.com/user-attachments/assets/511180be-6801-4f53-931a-c948b1439548" />
  <p><i>Figure 2.1: Dual Switch Ethernet Architecture & Subsea Pinout Breakout.</i></p>
</div>

<br>

## 3. Bulkhead Connector Specifications & Pinout Reference

Master technical specifications for all SubConn bulkhead connectors installed on the Electronics Bottle endcaps[cite: 8].

<div align="center">
<img width="1270" height="829" alt="Bulkhead Pinouts" src="https://github.com/user-attachments/assets/6d8d0149-95b8-44a0-a048-a19b268fa883" />
  <p><i>Figure 3.1: SubConn Bulkhead Face Views and Hardware Specifications.</i></p>
</div>

<br>

## 4. Electronics Bottle Internal Fiber Cabling

Details internal optical media conversion, CWDM wavelength multiplexing, and fiber pass-through routing inside the Electronics Bottle to bridge copper Ethernet devices to the SubConn OptiLink subsea bulkhead[cite: 8].

<div align="center">
<img width="1280" height="880" alt="Bottle Fiber Cabling" src="https://github.com/user-attachments/assets/5123f9c5-6b91-48be-9f4a-656a459024e3" />
  <p><i>Figure 4.1: Internal Optical Media Conversion & CWDM Routing.</i></p>
</div>

<br>

## 5. Bottle Endcap Connector Placements & Designation Maps

External bulkhead connector placements, designations, part numbers, and gender specifications for both the Electronics Bottle and Expansion Bottle[cite: 8].

<div align="center">
<img width="1258" height="819" alt="Endcap Connector Placement" src="https://github.com/user-attachments/assets/100949ed-dd02-4bee-9d20-c77d0e01dbc9" />
  <p><i>Figure 5.1: Electronics Bottle Front and Back Endcap Bulkhead Layouts.</i></p>
</div>

<br>

<div align="center">
<img width="1248" height="818" alt="Expansion Connector Placement" src="https://github.com/user-attachments/assets/88d9ceb8-bf1a-4be6-ab0d-6c3839617479" />
  <p><i>Figure 5.2: Expansion Bottle Endcap Bulkhead Layout.</i></p>
</div>

<br>

## 6. Serial Instrumentation Port Arrays (INST 1–12)

Internal power distribution buses, Moxa N-Port serial server interfaces, and pin routings for auxiliary instrumentation ports INST 1 through INST 12 (J11–J22) inside the Electronics Bottle[cite: 8].

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

## 7. AC Power Distribution & MVS 5000 Strobe Controls

Governs high-voltage AC input distribution, internal DC power generation (5V, 12V, 24V, 48V), system cooling fans, camera power control, and flash pulse triggers for four MVS 5000 strobe units[cite: 8].

<div align="center">
<img width="1254" height="834" alt="AC Power" src="https://github.com/user-attachments/assets/c943e173-9c90-4b22-b80e-8f91a35f3040" />
  <p><i>Figure 7.1: AC Power Distribution, Rectifiers, and Strobe Control Schematic.</i></p>
</div>

<br>

## 8. Sensor Bottles, Strobe Units & Camera Housings

### 8.1 Strobe Bottle Internal Schematic

<div align="center">
<img width="1234" height="838" alt="Strobe Bottle" src="https://github.com/user-attachments/assets/16c26846-5ed4-4318-ac23-aa0c5d430d06" />
  <p><i>Figure 8.1: WHOI Strobe Bottle Internal Electrical Schematic.</i></p>
</div>

<br>

### 8.2 Attitude Bottle Internal Schematic

<div align="center">
<img width="1226" height="827" alt="Attitude Bottle" src="https://github.com/user-attachments/assets/eac244c8-2b77-4025-a97c-7e7b2bc27c7c" />
  <p><i>Figure 8.2: WHOI Attitude Bottle (Microstrain 3DM-GX3-25 IMU) Schematic.</i></p>
</div>

<br>

### 8.3 Camera Synchronization Bus Circuit Analysis

<div align="center">
<img width="1206" height="804" alt="Camera Trigger" src="https://github.com/user-attachments/assets/8be62985-f4e8-4581-846c-8b9f9c71552a" />
  <p><i>Figure 8.3: Optically Isolated Shared Camera / Strobe Synchronization Bus.</i></p>
</div>

<br>

### 8.4 Allied Vision Mako G-234C Camera Housing Wiring

<div align="center">
<img width="1195" height="883" alt="Camera Wiring" src="https://github.com/user-attachments/assets/1d0c551d-283e-417a-8295-8503d2ee9ade" />
  <p><i>Figure 8.4: Allied Vision Mako G-234C Camera Housing Electrical Wiring Diagram.</i></p>
</div>

<br>

## 9. CTD & Environmental Sensor Cable Harnesses

### 9.1 Sea-Bird SBE 37 / SBE 49 CTD Cable Assembly

<div align="center">
<img width="1234" height="881" alt="CTD Wiring" src="https://github.com/user-attachments/assets/e79fb571-f2c0-4c4f-bfd4-d1134a0c35e7" />
  <p><i>Figure 9.1: Sea-Bird SBE 37/49 CTD Sensor Cable Schematic.</i></p>
</div>

<br>

### 9.2 ECO-Triplet Fluorometer Cable Assembly

<div align="center">
<img width="1234" height="881" alt="Eco-Triplet Wiring" src="https://github.com/user-attachments/assets/b112bbf6-75a1-43c8-b4a5-00ff100705ca" />
  <p><i>Figure 9.2: Sea-Bird / WET Labs ECO-Triplet Cable Schematic.</i></p>
</div>