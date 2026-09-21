# Software & Data Overview

## Stereo Acquisition Suite

### Topside Status
| Application Control | Control / Field | Example Value | Definition |
| :--- | :--- | :--- | :--- |
| **Co-Pilot** | Survey/Cruise (HabCam) ID | `2026/HabCam/Bigelow` | Designates the survey type and vessel (typically `Year/ID`). |
| **Co-Pilot** | Survey/Cruise (AUV) ID | `2026/AUV/Smallboat` | Designates the survey type and vessel for AUV operations. |
| **Co-Pilot** | OP Area | `Newport, RI to Newport, RI` | Operation Area where data is currently being collected. |

### Sensor Status
| Application Control | Sensor | Status Light | Definition |
| :--- | :--- | :--- | :--- |
| **Co-Pilot** | **AHRS** | Green = ON<br>Red = OFF | Attitude and Heading Reference System; computes 3D orientation (roll, pitch, yaw) and direction. |
| **Co-Pilot** | **CTD** | Green = ON<br>Red = OFF | Conductivity, Temperature, and Depth sensor; determines salinity, density, and sound velocity. |
| **Co-Pilot** | **ECO Triplet** | Green = ON<br>Red = OFF | Environmental Characterization Optics; highly customizable 3-channel optical sensor. |
| **Co-Pilot** | **SeaFET** | Green = ON<br>Red = OFF | Ocean pH sensor designed for long-term, high-precision marine monitoring. |
| **Co-Pilot** | **GPS** | Green = ON<br>Red = OFF | Global Positioning System; tracks physical location (latitude, longitude) and altitude. |
| **Co-Pilot** | **Fathometer** | Green = ON<br>Red = OFF | Active sonar device measuring water depth beneath the vessel via acoustic echo travel time. |
| **Co-Pilot** | **Altimeter 1** | Green = ON<br>Red = OFF | Sensor measuring vehicle altitude above a fixed reference point (seafloor). |

### Vehicle Metrics
| Application Control | Parameter | Example Value | Definition |
| :--- | :--- | :--- | :--- |
| **Co-Pilot** | Heading | `226.75°` | Compass direction in which the front of the vehicle is pointing. |
| **Co-Pilot** | Pitch | `-5.0°` | Vehicle attitude along the lateral axis in decimal degrees. |
| **Co-Pilot** | Roll | `46.3°` | Vehicle attitude along the longitudinal axis in decimal degrees. |
| **Co-Pilot** | Depth | `60.72m` | Depth of the vehicle in the water column. |
| **Co-Pilot** | Altitude | `2.32m` | Vertical distance between the vehicle and the ocean floor. |

### CTD Module
| Application Control | Parameter | Example Value | Definition |
| :--- | :--- | :--- | :--- |
| **Co-Pilot** | Conductivity | `3.208770 S/m` | Measures the water's ability to conduct an electrical current. |
| **Co-Pilot** | Salinity | `32.836000 psu` | Concentration of dissolved salts in the water column. |
| **Co-Pilot** | Sound Speed | `1471.20 m/s` | Rate at which acoustic waves travel through the water column. |
| **Co-Pilot** | Temperature | `5.55°C` | Water temperature measured directly using thermistors or platinum thermometers. |
| **Co-Pilot** | Pressure | `61.147000 dbar` | Barometric pressure used to calculate precise vehicle depth. |

### Vessel Data
| Application Control | Parameter | Example Value | Definition |
| :--- | :--- | :--- | :--- |
| **Co-Pilot** | Latitude | `40° 0.8764` | Geographic north-south position coordinate. |
| **Co-Pilot** | Longitude | `-72° 35.5802` | Geographic east-west position coordinate. |
| **Co-Pilot** | Depth Below Transducer | `65.76m` | Vertical distance from the sonar sensor to the seafloor. |
| **Co-Pilot** | Heading | `0.00°` | Compass direction in which the vessel's bow is pointing. |
| **Co-Pilot** | COG | `59.6°` | Course Over Ground; actual direction moving across Earth's surface (0° to 360°). |
| **Co-Pilot** | SOG | `5.559 knots` | Speed Over Ground; actual speed relative to Earth's surface. |

### Oxygen Sensor
| Application Control | Parameter | Example Value | Definition |
| :--- | :--- | :--- | :--- |
| **Co-Pilot** | Conductivity | `3.208770 S/m` | Water's ability to transmit electrical current; indicates total dissolved ions/salts. |
| **Co-Pilot** | Salinity | `32.836000 psu` | Total concentration of dissolved salts in water. |
| **Co-Pilot** | Dissolved Oxygen | `6.418000 ml/L` | Measurement of free, non-compound O₂ molecules mixed into liquid. |
| **Co-Pilot** | Temperature | `5.56°C` | Temperature of the water environment. |
| **Co-Pilot** | Pressure | `61.603000 dbar` | Ambient pressure measurement. |

### SeaFET (pH Sensor)
| Application Control | Parameter | Example Value | Definition |
| :--- | :--- | :--- | :--- |
| **Co-Pilot** | Int pH | `N/A` | Internal pH calculated via closed KCl reference electrode. |
| **Co-Pilot** | t | `N/A` | Water temperature. |
| **Co-Pilot** | Int V | `N/A` | Raw voltage from internal reference electrode. |
| **Co-Pilot** | Therm V | `N/A` | Thermistor voltage reading for internal sensor temperature. |
| **Co-Pilot** | Supply V | `N/A` | Main supply voltage. |
| **Co-Pilot** | 5V | `N/A` | Regulated DC power for integrated system components. |
| **Co-Pilot** | Ext pH | `N/A` | External pH calculated using seawater-exposed reference electrode. |
| **Co-Pilot** | hum | `N/A` | Internal moisture/humidity level inside housing. |
| **Co-Pilot** | Ext V | `N/A` | Raw voltage from external solid-state reference electrode. |
| **Co-Pilot** | stat | `N/A` | Instrument operational status and configuration state. |
| **Co-Pilot** | Supply 1 | `N/A` | Sensor power usage / current draw. |
| **Co-Pilot** | Iso V | `N/A` | Isolation voltage limit for safety components. |

### Attitude Plots
| Application Control | Parameter | Range Limits | Definition |
| :--- | :--- | :--- | :--- |
| **Co-Pilot** | Heading | No Min/Max | Compass direction of the vehicle's bow. |
| **Co-Pilot** | Pitch | Max: 0 / Min: -12 | Vehicle lateral axis tilt limits in decimal degrees. |
| **Co-Pilot** | Roll | Max: 50 / Min: 45 | Vehicle longitudinal axis tilt limits in decimal degrees. |

### Dsvimview (Cameras & Winchfly)
| Application Control | Control / Setting | Example Setting | Definition |
| :--- | :--- | :--- | :--- |
| **Co-Pilot** | Show Histogram | Toggled off | Visual chart grouping pixel response values across brightness ranges. |
| **Co-Pilot** | Histogram Equalize | Toggled off | Contrast adjustment technique spreading pixel intensities across full dynamic range. |
| **Co-Pilot** | Histogram Stretch | Toggled off | Contrast adjustment technique expanding cramped brightness ranges to highlight shadows/details. |
| **Co-Pilot** | Gain | `6.00 hz` | Signal amplification control to distinguish seabed substrate types. |
| **Co-Pilot** | Exposure | Max: 10.00 ms<br>Min: 0.00 ms | Camera exposure control balancing brightness while preventing glare or shadow detail loss. |
| **Co-Pilot** | RCVD | Gain: 18.0<br>Exposure: 1.5 ms | Received signal strength control filtering out water column acoustic noise. |
| **Co-Pilot** | Show Winchfly | Toggled on Green | Enables automated vehicle steering to maintain set altitude above seafloor. |
| **Pilot** | Bottom | `-50 m` | Strongest acoustic return indicating the physical seafloor. |
| **Pilot** | Fish Depth | `59.9 m` | Calculated vertical distance from water surface to vehicle. |
| **Pilot** | Computed Bottom | `-75 m` | Algorithmically calculated seabed boundary correcting for false echoes. |
| **Pilot** | Alt | `3.5 m` | Vertical distance between vehicle and seafloor. |
| **Pilot** | Fathometer | `65.5 m` | Echo sounder water depth measurement. |
| **Pilot** | Fathometer Filter | `0.8` | Acoustic noise filter smoothing depth readings. |
| **Pilot** | Depth Filter | `0.8` | Restricts sonar/mapping display to specific vertical bounds. |
| **Pilot** | Calc Depth | `63.3 m` | Depth compensation setting adjusting image brightness/color for light attenuation. |

---

## Winch Joystick Control

### Manual Winch Panel
| Application Control | Field | Example Value | Definition |
| :--- | :--- | :--- | :--- |
| **Pilot** | Cast Duration | `26:26` | Elapsed time since the current cast was initiated. |
| **Pilot** | Set Length | `500 meter` | Maximum allowable winch cable payload payout limit. |
| **Pilot** | Tension | `5.77 tons` | Mechanical load threshold protecting cable from over-strain. |
| **Pilot** | Linespeed | `0 meter/min` | Rate at which cable spools on/off the winch drum. |
| **Pilot** | Length | `91.2 meter` | Total cable paid out in meters. |

> *Examples referenced from HabCam Survey 2026 operations.*
