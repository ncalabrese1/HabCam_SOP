<div align="center">

# HabCam Staging and Survey Protocols

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

<br>


<br>

<h2 id="annual-timeline">1. Annual 12-Month Operational Calendar (Mid-May Survey Schedule)</h2>

<p>Overview of the 12-month lifecycle starting 6 months out from a Mid-May cruise departure:</p>

<table width="100%" border="1" cellpadding="12" cellspacing="0" style="border-collapse: collapse; border: 1px solid #cccccc; text-align: left;">
  <tr>
    <td width="25%" valign="top" bgcolor="#f8f9fa">
      <h4 style="margin-top:0; color:#2e7d32;">NOVEMBER</h4>
      <p><b>~6 Months Out</b></p>
      <hr>
      <p style="font-size: 0.9em;"><b>Calibrations & Procurement</b><br>Confirm ship time; send CTDs/puck to WA for RMA calibration; order long-lead supplies; ship damaged gear for repair.</p>
    </td>
    <td width="25%" valign="top" bgcolor="#f8f9fa">
      <h4 style="margin-top:0; color:#2e7d32;">DECEMBER</h4>
      <p><b>~5 Months Out</b></p>
      <hr>
      <p style="font-size: 0.9em;"><b>Inventory & Ordering</b><br>Track repair shipments, audit spare parts inventory, and finalize pre-cruise ordering lists.</p>
    </td>
    <td width="25%" valign="top" bgcolor="#f8f9fa">
      <h4 style="margin-top:0; color:#2e7d32;">JANUARY</h4>
      <p><b>~15 Weeks Out</b></p>
      <hr>
      <p style="font-size: 0.9em;"><b>IT & Security Audit</b><br>Check in with ITD to ensure software security patching is applied to all field machines prior to surveys.</p>
    </td>
    <td width="25%" valign="top" bgcolor="#f8f9fa">
      <h4 style="margin-top:0; color:#2e7d32;">FEBRUARY</h4>
      <p><b>~12 Weeks Out</b></p>
      <hr>
      <p style="font-size: 0.9em;"><b>Software & Workstations</b><br>Setup 2026 software directories/GUIs, install R packages, verify IP addresses, and load laptops.</p>
    </td>
  </tr>
  <tr>
    <td width="25%" valign="top" bgcolor="#f8f9fa">
      <h4 style="margin-top:0; color:#2e7d32;">MARCH</h4>
      <p><b>~10 to 8 Weeks Out</b></p>
      <hr>
      <p style="font-size: 0.9em;"><b>DB & Bench Assembly</b><br>Clevis burnout; create Postgres DB; assemble vehicle; check fuses/O-rings; pull 16 inHg vacuum on main bottle.</p>
    </td>
    <td width="25%" valign="top" bgcolor="#f8f9fa">
      <h4 style="margin-top:0; color:#2e7d32;">APRIL</h4>
      <p><b>~6 to 4 Weeks Out</b></p>
      <hr>
      <p style="font-size: 0.9em;"><b>Tank Tests & Staffing</b><br>WHOI tank calibration test; replace pinger batteries; send selection emails; build watch bills & assign berthing.</p>
    </td>
    <td width="25%" valign="top" bgcolor="#f8f9fa">
      <h4 style="margin-top:0; color:#2e7d32;">MAY</h4>
      <p><b>Survey Month</b></p>
      <hr>
      <p style="font-size: 0.9em;"><b>Staging & Departure</b><br>Mount weak link; hand off .GPX file to bridge; hold pre-cruise meeting; execute active field survey operations.</p>
    </td>
    <td width="25%" valign="top" bgcolor="#f8f9fa">
      <h4 style="margin-top:0; color:#2e7d32;">JUNE</h4>
      <p><b>Post-Survey</b></p>
      <hr>
      <p style="font-size: 0.9em;"><b>Data Offload & Breakdown</b><br>Offload primary raw image/sensor data, wash down vehicle, log maintenance, and store vehicle in Net Loft.</p>
    </td>
  </tr>
  <tr>
    <td width="25%" valign="top" bgcolor="#f8f9fa">
      <h4 style="margin-top:0; color:#2e7d32;">JULY</h4>
      <p><b>Data Processing</b></p>
      <hr>
      <p style="font-size: 0.9em;"><b>Data Verification</b><br>Verify complete offload of prior survey image databases and clear/reformat server backup drives.</p>
    </td>
    <td width="25%" valign="top" bgcolor="#f8f9fa">
      <h4 style="margin-top:0; color:#2e7d32;">AUGUST</h4>
      <p><b>Maintenance</b></p>
      <hr>
      <p style="font-size: 0.9em;"><b>Hardware Refurbishment</b><br>Inspect frame integrity, service mechanical connectors, and log spare parts consumption.</p>
    </td>
    <td width="25%" valign="top" bgcolor="#f8f9fa">
      <h4 style="margin-top:0; color:#2e7d32;">SEPTEMBER</h4>
      <p><b>Planning Phase</b></p>
      <hr>
      <p style="font-size: 0.9em;"><b>Ship Time Allocation</b><br>Confirm upcoming year survey dates with NOAA marine operations and review past cruise performance logs.</p>
    </td>
    <td width="25%" valign="top" bgcolor="#f8f9fa">
      <h4 style="margin-top:0; color:#2e7d32;">OCTOBER</h4>
      <p><b>Pre-Season Prep</b></p>
      <hr>
      <p style="font-size: 0.9em;"><b>RMA Preparation</b><br>Prepare Return to Manufacturer Authorization (RMA) paperwork for upcoming November calibration shipments.</p>
    </td>
  </tr>
</table>

<br>
<hr>
<br>

</div>

<h2 id="pre-cruise-checklist">2. Pre-Cruise Operational Checklist</h2>

<h3 id="chk-6-months" style="color: #2e7d32; text-align: left;">6 Months out: ~ November</h3>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Confirm ship time and set cruise date</li>
  <li><input type="checkbox"> Send Seabird 37, Seabird 49 CTDs and Wetlabs ecotriplet puck to Washington for Calibrations [Return to Manufacturer Authorization (RMA) form]</li>
  <li><input type="checkbox"> Begin ordering equipment and supplies needed before upcoming cruise [itemized ordering guide here]</li>
  <li><input type="checkbox"> Send out any equipment that was damaged from last survey</li>
</ul>

<h3 id="chk-15-weeks" style="color: #2e7d32; text-align: left;">15 Weeks out:</h3>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> If ITD hasn't reached out to have computer software security added to machines prior to surveys (i.e. patched), check-in</li>
</ul>

<h3 id="chk-12-weeks" style="color: #2e7d32; text-align: left;">12 Weeks out:</h3>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Set up all servers with 2026 software directories and GUIs</li>
  <li><input type="checkbox"> Collect flashdrive from POPDY and Install R packages on annotation machines</li>
  <li><input type="checkbox"> Verify that IP address can be changed on annotation machines</li>
  <li><input type="checkbox"> Ensure sonar software and coastal explorer are installed on 2 field laptops</li>
</ul>

<h3 id="chk-10-weeks" style="color: #2e7d32; text-align: left;">10 Weeks out:</h3>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Hand-off Clevis to Shellfish group to have the epoxy burned out at Reidar's in New Bedford</li>
  <li><input type="checkbox"> Ensure Seabird 37, Seabird 49 and Wetlabs ecotriplet puck have returned from Washington</li>
  <li><input type="checkbox"> Ensure any damaged equipment sent for repairs has been returned</li>
  <li><input type="checkbox"> Create a new HABCAM database on Postgres servers</li>
  <li><input type="checkbox"> Confirm previous years data has been offloaded</li>
  <li><input type="checkbox"> Clear server drives</li>
  <li><input type="checkbox"> Reformat back-up drives</li>
</ul>

<h3 id="chk-8-weeks" style="color: #2e7d32; text-align: left;">8 Weeks out:</h3>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Prepare HABCAM for WHOI Sundance Tank Calibration Test</li>
  <li><input type="checkbox"> Pack supply kit for WHOI sundance tank calibration test</li>
  <li><input type="checkbox"> If applicable, install chanos onto tow sled</li>
  <li><input type="checkbox"> Science center staffing call</li>
</ul>

<h3 id="chk-6-weeks" style="color: #2e7d32; text-align: left;">6 Weeks out:</h3>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Take vehicles to WHOI sea water tank test to calibrate equipment (<a href="https://example.com" target="_blank">Camera calibrations for dummies</a>)</li>
  <li><input type="checkbox"> Repair or Resolve any issues that came up during the WHOI tank test</li>
  <li><input type="checkbox"> Store Vehicle at netloft until staging</li>
  <li><input type="checkbox"> Replace batteries in Pinger (Benthos UAT 376 acoustic transponder) </li>
</ul>

<h3 id="chk-5-weeks" style="color: #2e7d32; text-align: left;">5 Weeks out:</h3>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Send “You are scheduled Email” notifying staff they have been selected for the survey. Include:</li>
  <li><input type="checkbox"> Survey expectations</li>
  <li><input type="checkbox"> Medical clearance forms</li>
  <li><input type="checkbox"> Dietary restrictions</li>
  <li><input type="checkbox"> Packing list (i.e. foul weather gear)</li>
  <li><input type="checkbox"> Preparing for sea packet</li>
  <li><input type="checkbox"> Notify watch chiefs that they will be sailing in leadership positions</li>
  <li><input type="checkbox"> Create balanced watches with cruise personnel list</li>
  <li><input type="checkbox"> Assign berthing</li>
</ul>

<h3 id="chk-1-week" style="color: #2e7d32; text-align: left;">1 Week out:</h3>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Email the scientific party a few days prior to departure letting them know about...</li>
  <li><input type="checkbox"> Departure times</li>
  <li><input type="checkbox"> Meeting points</li>
  <li><input type="checkbox"> Parking procedures</li>
  <li><input type="checkbox"> Any last minute issues that may arise (bad weather, etc).</li>
</ul>

<h3 id="chk-staging" style="color: #2e7d32; text-align: left;">Staging</h3>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Mounting the weak link</li>
  <li><input type="checkbox"> Provide the captain/bridge with the .GPX file of station locations so they can import it into their navigation software and check tracklines and make recommendations for any shifts in waypoints.</li>
  <li><input type="checkbox"> Chanos sensor dissolved inorganic carbon sensor (PH, DIC, total alkalinity)</li>
</ul>

<h3 id="chk-departure" style="color: #2e7d32; text-align: left;">Day of Departure:</h3>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> If leaving from WH store vehicle keys in the locker by the Survey refrigerator. Parking forms must be filled out and placed on the car dashboard.</li>
  <li><input type="checkbox"> When heading to Newport, RI, keep the ship informed about the science party’s arrival time.</li>
  <li><input type="checkbox"> Ensure all members of scientific party are aboard</li>
  <li><input type="checkbox"> Muster to bridge 30 min prior to departure time</li>
  <li><input type="checkbox"> Inspect underwater cables for damage and/or voltage leaks.</li>
  <li><input type="checkbox"> Host an on-board, pre-cruise meeting with scientific staff</li>
  <li><input type="checkbox"> Perform Introductions; Thank everyone for participating</li>
  <li><input type="checkbox"> <span style="background-color: #ffff00; padding: 2px 4px;"><b>Identify Watch Chief for first shift; they must be listened to concerning FSCS procedures</b></span></li>
  <li><input type="checkbox"> Announce area of operation, general cruise direction, and ETA to first station, and sequence of events at station</li>
  <li><input type="checkbox"> Emphasize importance of ‘Safety First’ (i.e. hard hats and safety vests)</li>
  <li><input type="checkbox"> Go over protocols for injuries</li>
  <li><input type="checkbox"> Relieve other watch 10 mins early</li>
  <li><input type="checkbox"> Remind Scientific Staff to notify Watch Chief and Chef of any food allergies</li>
  <li><input type="checkbox"> Ensure watch times on day of departure/arrival are divided equally for pay purposes</li>
  <li><input type="checkbox"> Track federal employee time</li>
</ul>

<br>
<hr>
<br>

<h2 id="staging-detail-sections">3. Detailed Staging & Survey Procedures</h2>

<h3 id="sec-6-months">6 Months Out (~November): Calibrations & Long-Lead Procurement</h3>

<ul>
  <li>Confirm ship time and set cruise date</li>
  <li>Send Seabird 37, Seabird 49 CTDs, and Wetlabs ECO-Triplet puck to Washington for calibrations [Return to Manufacturer Authorization (RMA) form]</li>
  <li>Begin ordering equipment and supplies needed before upcoming cruise [itemized ordering guide here]</li>
  <li>Send out any equipment that was damaged from last survey</li>
</ul>

<br>

<h4 id="sec-6mo-ship-time">Confirm Ship Time & Cruise Date</h4>
<p><i>[Insert details on contacting NOAA Marine Operations, confirming vessel availability, and setting firm survey departure/return windows]</i></p>

<h4 id="sec-6mo-ctd-calibration">CTD & ECO-Triplet Calibration Shipments (RMA)</h4>
<p><i>[Insert RMA submission instructions, packaging requirements, Sea-Bird/WET Labs shipping addresses, and tracking protocols]</i></p>

<h4 id="sec-6mo-procurement">Equipment & Supply Procurement</h4>
<p><i>[Insert itemized ordering guide, long-lead component lists, vendor contacts, and requisition procedures]</i></p>

<p><b>Quick Task:</b></p>
<ul>
  <li>Send out any equipment that was damaged from last survey.</li>
</ul>

<br>
<hr>
<br>

<h3 id="sec-15-weeks">15 Weeks Out: IT & Software Security Audit</h3>

<ul>
  <li>Check in with ITD regarding computer security patching if they haven't reached out</li>
</ul>

<br>

<p><b>Quick Task:</b></p>
<ul>
  <li>If ITD hasn't reached out to have computer software security added to machines prior to surveys (i.e., patched), check-in.</li>
</ul>

<h4 id="sec-15wk-patched">Patched</h4>
<p><i>[Insert details explaining OS patch requirements, security software updates, firewall rules, and offline field machine clearance steps]</i></p>

<br>
<hr>
<br>

<h3 id="sec-12-weeks">12 Weeks Out: Server, GUI & Workstation Setup</h3>

<ul>
  <li>Set up all servers with software directories and GUIs</li>
  <li>Collect flashdrive from POPDY and Install R packages on annotation machines</li>
  <li>Verify that IP address can be changed on annotation machines</li>
  <li>Ensure sonar software and Coastal Explorer are installed on 2 field laptops</li>
</ul>

<br>

<h4 id="sec-12wk-server-setup">Server Directory & GUI Setup</h4>
<p><i>[Insert server folder structure templates, database pathing, GUI executable placements, and directory permission settings]</i></p>

<h4 id="sec-12wk-r-packages">POPDY Flash Drive & R Package Installation</h4>
<p><i>[Insert steps for retrieving the POPDY flash drive, offline R package repository paths, dependency installations, and workstation scripts]</i></p>

<h4 id="sec-12wk-ip-config">Annotation Machine IP Configuration</h4>
<p><i>[Insert network adapter settings, static IP assignment procedures, subnets, and verification commands for annotation machines]</i></p>

<h4 id="sec-12wk-field-laptops">Field Laptop Sonar & Navigation Software</h4>
<p><i>[Insert software installation steps for Coastal Explorer, BlueView sonar drivers, license key verifications, and laptop field profiles]</i></p>

<br>
<hr>
<br>

<h3 id="sec-8-weeks" style="color: #2e7d32; text-align: left;">8 Weeks Out: Vehicle Bench Assembly & Pre-Calibration Prep</h3>

<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Prepare HABCAM for WHOI Sundance Tank Calibration Test</li>
  <li><input type="checkbox"> Pack supply kit for WHOI sundance tank calibration test</li>
  <li><input type="checkbox"> If applicable, install chanos onto tow sled</li>
  <li><input type="checkbox"> Science center staffing call</li>
</ul>

<br>

<h4 id="sec-8wk-sundance-prep">Prepare HabCam for WHOI Sundance Tank Calibration Test</h4>
<p><i>[Insert overview and general preparation steps for the WHOI Sundance Tank calibration deployment]</i></p>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Attach/Install CTDs, ecotriplet puck, and Blueview forward looking sonar</li>
  <li><input type="checkbox"> Open main electronics bottle, check fuses, inspect O-rings, replace desiccant and pull a vacuum</li>
  <li><input type="checkbox"> After 24 hours, confirm PSI has remained stable: Pressure holds at 16 inHg. If leak or change in pressure is detected, likely to reinspect O-rings.</li>
  <li><input type="checkbox"> Pull the camera plate and inspect O-rings in both housings. Refocus camera lenses if necessary.</li>
  <li><input type="checkbox"> Attach altimeter and attitude sensors onto camera plate. Re-attach camera plate to HABCAM.</li>
  <li><input type="checkbox"> Inspect underwater cables for damage and/or voltage leaks</li>
  <li><input type="checkbox"> Regrease Connector Faces & Plug Into Sensors</li>
  <li><input type="checkbox"> Power On Main Electronics Bottle & Verify Engineering GUI Data</li>
  <li><input type="checkbox"> Connect to Stereocameras & Verify Camera/Strobe Trigger Rates</li>
</ul>

<br>

<h4 id="sec-8wk-pack-supply-kit">Pack Supply Kit for WHOI Sundance Tank Calibration Test</h4>
<p><i>[Insert packing list, required hand tools, spare O-rings, calibration targets, and test gear inventory here]</i></p>

<h4 id="sec-8wk-install-chanos">Install Chanos Sensor onto Tow Sled (If Applicable)</h4>
<p><i>[Insert mechanical mounting, bracket alignment, cable harness routing, and power/data integration steps for the Chanos sensor]</i></p>

<h4 id="sec-8wk-staffing-call">Science Center Staffing Call</h4>
<p><i>[Insert staffing call protocol, participant application deadlines, skill set requirements, and roster collection guidelines]</i></p>

<br>

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

<br>
