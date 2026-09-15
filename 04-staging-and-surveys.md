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
  <li><input type="checkbox"> Notify watch chiefs that they will be sailing in leadership positions</li>
  <li><input type="checkbox"> Create balanced watches with cruise personnel list</li>
  <li><input type="checkbox"> Assign berthing</li>
</ul>

<h3 id="chk-1-week" style="color: #2e7d32; text-align: left;">1 Week out:</h3>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Email the scientific party a few days prior to departure letting them know about...</li>
</ul>

<h3 id="chk-staging" style="color: #2e7d32; text-align: left;">Staging</h3>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> <a href="02-hardware-and-schematics.md#weak-link">Mounting the weak link</a></li>
  <li><input type="checkbox"> <a href="02-hardware-and-schematics.md#fiber-optic-termination">Splice fiber optics</a></li>
  <li><input type="checkbox"> <a href="02-hardware-and-schematics.md#pull-test">Do the pull test</a></li>
  <li><input type="checkbox"> Load vehicle
  <li><input type="checkbox"> Load equipment
  <li><input type="checkbox"> Setup stations
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

<h3 id="sec-6-weeks" style="color: #2e7d32; text-align: left;">6 Weeks Out: WHOI Seawater Tank Calibration Test & Logistics</h3>

<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Take vehicles to WHOI sea water tank test to calibrate equipment (<a href="https://example.com" target="_blank">Camera calibrations for dummies</a>)
  <li><input type="checkbox"> Repair or Resolve any issues that came up during the WHOI tank test</li>
  <li><input type="checkbox"> Store Vehicle at netloft until staging</li>
  <li><input type="checkbox"> Pinger: Benthos UAT 376 acoustic transponder - replace batteries</li>
</ul>

<br>

<h4 id="sec-6wk-calibration">Calibration</h4>

<div align="center">
<img width="510" height="680" alt="Calibration for Dummies" src="https://github.com/user-attachments/assets/8d6a9da0-36e2-4693-946e-39ed412aff16" />
</div>

<br>

<h5 id="sec-6wk-reserving-tank">Reserving the Tank</h5>
<p><i>[Insert reservation procedures, point of contact at WHOI, scheduling lead times, and facility access requirements here]</i></p>

<h5 id="sec-6wk-transporting-vehicle">Transporting the Vehicle</h5>
<p><i>[Insert vehicle transport logistics, truck/trailer loading steps, strapping protocols, and staging at the Sundance Tank here]</i></p>

<h5 id="sec-6wk-setting-up-calibration">Setting Up Calibration</h5>
<p><i>[Insert tank placement, water fills, sensor submersion setup, power hookups, and initial system checks here]</i></p>

<h5 id="sec-6wk-collecting-data">Collecting Calibration Data</h5>

<h6>1. Checkerboard Target Data Collection:</h6>
<ul style="text-align: left;">
  <li><b>Common Area Positioning:</b> Ensure the entire checkerboard is placed in the overlap zone (common area) between the left and right cameras' fields of view so it appears fully on both cameras.
    <br><br>
    <div align="center">
      <img width="515" height="123" alt="Checkerboard Common Area View" src="https://github.com/user-attachments/assets/be5faafa-43ce-45de-9d7a-ed6db7d5ab3e" />
      <p><i>Checkerboard Positioned Within the Overlapping Common Viewing Area</i></p>
    </div>
  </li>
  <li><b>Grid Coverage:</b> Divide the common viewing area into 9 equal regions and take photos in all 9 regions to ensure full spatial coverage.
    <br><br>
    <div align="center">
      <img width="233" height="101" alt="Region Grid Overlay" src="https://github.com/user-attachments/assets/575fc675-9594-4792-a14a-02add361cc14" />
      <p><i>9-Region Division Grid Across Common Field of View</i></p>
    </div>
  </li>
  <li><b>Glare & Tilting:</b> Avoid direct strobe glare on the board (glare images will be rejected by estimation software). Tilting the board slightly is preferred over lying flat to minimize glare.</li>
  <li><b>Altitude & Angle Sampling:</b> Capture images across 2–3 different vehicle altitudes and multiple angles (both flat and tilted).
    <br><br>
    <div align="center">
    <img width="550" height="287" alt="Checkerboard Calibration Array" src="https://github.com/user-attachments/assets/7ae5f0fd-043b-4d2d-9f56-e07ab8b1a017" />
    <p><i>Figure 1: Acceptable Checkerboard Sample Images Across Angles and Altitudes from the 2015 Calibration (Best) </i></p>
    </div>
  </li>
</ul>

<br>

<h6>2. Scallop Target Data Collection:</h6>
<ul style="text-align: left;">
  <li><b>Placement:</b> Lay the scallop target board flat on the bottom of the dunk tank for accurate altimeter reference. Lower and raise the vehicle using the overhead crane.
    <br><br>
    <div align="center">
     <img width="1600" height="1200" alt="Scallop Shell Target Board" src="https://github.com/user-attachments/assets/6ff6101d-0e0a-4711-bbf8-8d25fda95d35" />
      <p><i>Physical Scallop Calibration Target Board with Known Shell Heights</i></p>
    </div>
  </li>
  <li><b>Field-of-View Distribution:</b> Divide the full field of view into 9 regions. Capture images with the target in 5 regions of the left field of view and 2 regions at the far right of the right field of view (or 5 right / 2 far left).
    <br><br>
    <div align="center">
      <table>
        <tr>
          <td align="center">
            <img width="233" height="101" alt="Left FOV Grid" src="https://github.com/user-attachments/assets/13132c48-2efb-4184-9298-c485f5ebe986" />
            <br>
            <b>5 Regions Left FOV / 2 Regions Far Right</b>
          </td>
          <td align="center">
           <img width="233" height="101" alt="Right FOV Grid" src="https://github.com/user-attachments/assets/6ae5f703-9018-4119-a6b8-e8fc527d0c8b" />
            <br>
            <b>5 Regions Right FOV / 2 Regions Far Left</b>
          </td>
        </tr>
      </table>
    </div>
  </li>
  <li><b>Varied Sampling:</b> Take photos at 2–3 distinct altitudes and varying tilt angles.</li>
</ul>

<br>

<h6>3. Altitude Logging:</h6>
<ul style="text-align: left;">
  <li>Ensure the Engineering GUI is actively running and logging live altimeter depth/altitude data during all test passes.</li>
</ul>

<br>
<hr>
<br>

<h5 id="sec-6wk-evaluation-criteria">Evaluation Criteria & Processing Iterations</h5>

<h6>Criteria for a Successful Calibration:</h6>
<ol style="text-align: left;">
  <li><b>Visual Integrity:</b> Processed images must be undistorted with minimal black edge bands (black border pixels must represent &lt; 5% of total image pixels).
    <br><br>
    <div align="center">
      <table>
        <tr>
          <td align="center">
            <img width="1600" height="602" alt="Bad Calibration Distortion" src="https://github.com/user-attachments/assets/fa5a1da3-b19b-4dd2-8907-3786d6307a3d" />
            <br>
            <b>Bad Calibration: Heavy Distortion & Black Edge Bands (>10%)</b>
          </td>
          <td align="center">
          <img width="1600" height="602" alt="Good Calibration" src="https://github.com/user-attachments/assets/d9b9e008-9969-4f9d-a85c-2d93b0c0b91d" />
              <br>
            <b>Good Calibration: Minimal Edge Distortion (<5% Black Pixels)</b>
          </td>
        </tr>
      </table>
    </div>
  </li>
  <li><b>Stereo Coverage Rate:</b> Successful stereo altitude estimates must be generated for &gt; 95% of total captured images.</li>
  <li><b>Measurement Accuracy:</b> Estimated scallop shell lengths (calculated via stereo altitude) must fall within &plusmn;3% of true physical measurements.</li>
</ol>

<br>

<h6>Step-by-Step Parameter Estimation Workflow:</h6>
<ol style="text-align: left;">
  <li>Estimate initial calibration parameters from selected checkerboard images.</li>
  <li>Process all scallop target images using the candidate calibration parameters.</li>
  <li>Inspect processed output images visually for optical distortion.</li>
  <li>Calculate the percentage of black edge pixels (&lt; 5% threshold).</li>
  <li>Determine the percentage of total images receiving valid stereo altitude estimates.</li>
  <li>Annotate the scallop target board images in numbered sequence (1 through 9).
    <br><br>
    <div align="center">
      <img width="230" height="173" alt="Numbered Scallop Annotation Sequence" src="https://github.com/user-attachments/assets/0e527551-f924-4c83-af72-cea6627f152f" />
      <p><i>Required Numbered Sequence (1–9) for Scallop Target Board Annotations</i></p>
    </div>
  </li>
  <li>Calculate average percentage bias in estimated scallop shell height compared to ground truth.</li>
  <li>Iterate image selection and parameter fitting until all three success criteria are satisfied.</li>
</ol>

</div>

<h4 id="sec-6wk-2018-experiment">The 2018 calibration experiment (Chang and Godlewski)</h4>

<h5>Rationale</h5>

<p>The paired tows of NEFSC Habcam, NEFSC dredge, and VIMS dredge were conducted at the same time at 19 overlapping stations in Elephant Trunk (ET) in 2018 (Figure 1). These pair tows were designed to study the dredge filling issue at high density area and the difference between 10 minutes and 15 minutes tows.</p>

<div align="center">
  <img width="720" height="720" alt="Figure 1" src="https://github.com/user-attachments/assets/e3c8d71e-e2c8-4b13-9fdb-df2834329beb" />
  <p><i>Figure 1. The paired tow locations for NEFSC Habcam, NEFSC dredge, and VIMS dredge survey, along with the locations for the entire VIMS dredge and WHOI Habcam survey in ET (the right gray polygon is ET-Open and the left gray polygon is ET-Flex) in 2018.</i></p>
</div>

<br>

<p>However, a problem for the NEFSC Habcam data emerged when analyzing the paired tow data - the mean scallop shell height collected by NEFSC Habcam estimated using the altimeter altitudes (122mm in ET-Open and 119mm in ET-Flex) was 13-16% higher than the mean scallop shell height collected by the NEFSC dredge (108mm in ET-Open and 103mm in ET-Flex; Figure 2). The shell height distributions from the NEFSC dredge and Habcam survey should be nearly identical since they were surveying overlapping locations and there is only one dominate cohort in ET.</p>

<p>The WHOI Habcam data have a similar problem compared to the VIMS dredge data, the mean shell height estimated using stereo altitudes was 6-8% higher (Figure 2). Even though the two surveys were not completely overlapped (Figure 1), a 6-8% difference in mean shell height is not expected in ET. If the altitudes from the Habcam data are accurate, the comparison of dredge and Habcam data in areas with only a single cohort are expected to be similar to Figure 3.</p>

<div align="center">
  <img width="1100" height="500" alt="Figure 2" src="https://github.com/user-attachments/assets/8e419861-dcc7-4df9-be6a-c5304e8d205a" />
</div>
  <p><i>Figure 2. Shell height frequencies, the number of shells measured, and mean shell height from multiple surveys in ET in 2018.</i></p>


<br>

<div align="center">
  <img width="650" height="500" alt="Figure 3" src="https://github.com/user-attachments/assets/bd735580-b3ff-4514-901a-7652335bf9ca" />
  <p><i>Figure 3. Shell height frequencies, the number of shells measured, and mean shell height from VIMS dredge and CFF Habcam survey (altimeter altitude) in the Nantucket Light Ship South Deep area in 2018.</i></p>
</div>

<br>

<p>Because the NESFC Habcam altimeter was not collecting accurate altitudes, the usefulness of stereo altitudes was explored. However, of 119,645 NEFSC Habcam images annotated in 2018, only 3,627 images have stereo altitudes. The estimated stereo altitudes are either closed to the altimeter altitudes or centered at 0.93 meters, which means that the stereo altitudes were estimated poorly and also biased (Figure 4).</p>

<div align="center">
 <img width="720" height="720" alt="Figure 4" src="https://github.com/user-attachments/assets/3a7b2ddb-1e10-4395-9f0e-0bc37f945a23" />
  <p><i>Figure 4. Comparison of altimeter and stereo altitudes for NEFSC Habcam data (annotated images) in 2018. Redline is a one to one line.</i></p>
</div>

<br>

<p>The comparison between Habcam and dredge survey shell heights were further examined from 2011 to 2018 for all areas surveyed to see if this is a single year problem or it persists over years. The list of the type of altitudes (and field of view calculations) used to estimate scallop shell heights for the Habcam data for each year is below (Burton Shank personal comm.):</p>

<ul style="text-align: left;">
  <li>2019 stereo altitudes only.</li>
  <li>2018 sonar altitudes only.</li>
  <li>2017 sonar altitudes only; 386 stereo altitudes in database.</li>
  <li>2016 stereo altitudes for 36,844 images of 97266 images; sonar for the rest.</li>
  <li>2015-sonar altitudes only; no direct FOV calculation, had to use altitude-based second-order polygon model; should fix this in the future.</li>
  <li>2014- sonar altitudes only. Direct FOV calculation for all except 723 images with FOV filled in with polygon model.</li>
  <li>2011 to 2013-working on this.</li>
</ul>

<p>The problem of altitudes for the NEFSC Habcam started in 2017. There are no accurate altitudes recorded or estimated for 2017 and 2018 NEFSC Habcam data. The problem is still not resolved to this date. This forced us to use stereo altitudes for the 2019 data. However, even though the bias of shell heights calculated using stereo altitudes are less than 5% in 2019, it is still not as good as the altimeter altitudes if the altimeter is working properly (Figure 3) because the stereo altitudes are estimates and estimates have errors.</p>

<h5>Goals</h5>

<ol style="text-align: left;">
  <li>Find a method to examine the accuracy of the stereo altitudes estimated from the calibration - at least one set of altitude needs to be accurate, if not both.</li>
  <li>Identify a method to correct the 2017 and 2018 NEFSC Habcam data.</li>
</ol>

<h5>Experiment design</h5>

<ol style="text-align: left;">
  <li>Three targets were made to explore the accuracy of the stereo altitudes, one with scallop shells and two with plastic disks to represent smaller scallops shell heights.
    <br><br>
    <div align="center">
      <table>
        <tr>
          <img width="1600" height="1200" alt="Figure 5C" src="https://github.com/user-attachments/assets/4525fa0b-a3e5-4324-9ab4-eb160206cf2f" />
          <img width="1047" height="785" alt="Figure 5B" src="https://github.com/user-attachments/assets/54942b51-a05a-4d7c-8bdc-2ab3d2c47d9d" />
          <img width="1600" height="1200" alt="Figure 5A" src="https://github.com/user-attachments/assets/e05d22be-cb6c-4f58-b544-7d554e4acdd5" />
         </tr>
      </table>
    </div>
  </li>
  <li>Images of the 3 targets were taken during the 2018 post-cruise calibration at 2 different altitudes and 5 different locations of the left field of view.
    <br><br>
    <div align="center">
   <img width="233" height="101" alt="Target Position Grid" src="https://github.com/user-attachments/assets/26c85e44-d7ec-47fb-bc74-706a8e07c6a6" />
     </div>
  </li>
  <li>For each target, 2 images at each locations and altitude were processed and annotated, resulting in a total of 64 images analyzed (should be 60 but some locations have 3 images annotated by mistake).</li>
  <li>The 64 selected target images were processed using the calibration estimated using the checkerboard images taken during the experiment (2018 post-cruise calibration, 20181102), as well as the calibrations from the past:
    <ul>
      <li>2018 post-cruise calibration (20181102)</li>
      <li>2018 pre-cruise calibration (20180507)</li>
      <li>2018 during-cruise calibration (20180527)</li>
      <li>2017 pre-cruise calibration (20170501)</li>
      <li>2015 post-cruise calibration (20150801)</li>
      <li>2015 pre-cruse calibration (20150501)</li>
    </ul>
  </li>
  <li>Each of the 64 target images was processed 6 times (using the above 6 calibrations). All of these processed images were annotated, even though they are the same image just processed with different calibrations. The annotations were done by two annotators. The percent of images that can get stereo altitude estimated for each calibration were documented.</li>
  <li>The scallop shell heights (or disk sizes) estimated using the stereo altitudes were compared to their true sizes and percent biases of the measurements were calculated using the following equation:
    <br><br>
    $$\% \text{Bias} = \frac{\text{Estimated Size} - \text{True Size}}{\text{True Size}} \times 100\%$$
  </li>
  <li>The percent biases were compared by calibrations, annotators, scallop or disk sizes, 3 targets, 2 altitudes, and 5 locations in the field of view.</li>
  <li>Once the best calibration (the calibration with the mean percent bias of measurement closest to zero) is identified, the measurements estimated from the annotations that were done on 5 other calibrations, the biased measurements, were reestimated using the stereo altitudes from the best calibration. The percent bias was calculated again for these updated measurements. This is specifically used to see if the images annotated with bad calibrations (i.e. 2017 and 2018 images) need to be reannotated, or these biased measurements can simply be corrected by reprocessing the images using a good calibration and reestimate the measurements using more accurate stereo altitudes.</li>
  <li>To test the sensitivity of checkerboard images to the calibration estimations, 200 calibrations were estimated from 82 checkerboard images that were randomly selected from a pool of ~200 2018 post-cruise checkerboard images iteratively for 200 times.</li>
</ol>

<h5>Results</h5>

<ol style="text-align: left;">
  <li>Below is the summary table of the number of images that have stereo altitude estimated. The numbers varied dramatically by calibrations. The 2018 post-cruise calibration can estimate the stereo altitudes for all 64 images, whereas the 2018 pre-cruise calibration can estimate stereo altitude for only 22% of the images.
    <br><br>
    <table width="80%" border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; text-align: left;">
      <thead>
        <tr bgcolor="#f2f2f2">
          <th>Calibration</th>
          <th># of images that have stereo altitude estimates</th>
          <th>Percent of images that have stereo altitude estimates</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>2018 post-cruise (20181102)</td><td>64</td><td>100%</td></tr>
        <tr><td>2018 pre-cruise (20180507)</td><td>14</td><td>22%</td></tr>
        <tr><td>2018 during-cruise (20180527)</td><td>41</td><td>64%</td></tr>
        <tr><td>2017 pre-cruise (20170501)</td><td>25</td><td>39%</td></tr>
        <tr><td>2015 post-cruise (20150801)</td><td>61</td><td>95%</td></tr>
        <tr><td>2015 pre-cruse (20150501)</td><td>53</td><td>83%</td></tr>
      </tbody>
    </table>
  </li>
  <li>There are significant differences in percent biases of the measurements by different calibrations. The mean bias can be as large as +14% (the estimated measurements are on average 14% larger than their true size; 2018 pre-cruise calibration, 20180524) and as small as -2% (the estimated measurements are on average 2% smaller than their true size; 2015 post-cruise calibration, 20150801; Figure 5).
    <br><br>
    <div align="center">
      <img width="1000" height="1000" alt="Figure 5" src="https://github.com/user-attachments/assets/94e75c09-3d27-43c4-ba10-4cac9b95bd83" />
      <p><i>Figure 5. Density plot of percent biases from all measurements (gray bars) and measurements by calibrations. Dash lines are the mean percent bias by calibrations.</i></p>
    </div>
  </li>
  <li>The best calibration is the 2015 post-cruise calibration (20150801) - it can estimate 95% of the stereo altitudes and the mean bias in measurement is 2%. The 2015 post-cruise calibration (20150801) was then used to reestimate the measurements that were annotated on images processed using 5 other calibrations to see if these biased measurements can be corrected using the stereo altitudes estimated from the 2015 post-cruise calibration (20150801). The reprocessing did reduce the mean percent biases from -5% to 14% (Figure 5) to +-3% (Figure 6), except for the measurements from the annotations of images processed using 2018 pre-cruise calibration (20180524), which still has a mean bias around 6%.
    <br><br>
    <div align="center">
      <img width="1000" height="1000" alt="Figure 6" src="https://github.com/user-attachments/assets/30ad477b-209e-4541-9418-9b14dcb48920" />
      <p><i>Figure 6. Density plot of percent biases from all measurements (gray bars) and measurements by calibrations. These measurements were originally estimated from annotations of images processed using different calibrations and then reestimated using stereo altitudes from the 2015 post-cruise calibration (20150801). Dash lines are the mean percent bias by calibrations.</i></p>
    </div>
  </li>
  <li>There are no significant differences in percent biases of the measurements by annotators, scallop or disk sizes, and 2 altitudes. However, there are differences in percent biases of the measurements by target locations in the field of view and 3 targets. Figure 7 is an example of the biases from the 2015 post-cruise calibration (20150801) by 3 targets, 2 altitudes, and 5 locations. The biases are similar for the 2 altitudes but seem to be more biased when the targets are placed at the top-right corner of the field of view. The biased also varied by the 3 targets.
    <br><br>
    <div align="center">
      <img width="1000" height="1000" alt="Figure 7 " src="https://github.com/user-attachments/assets/69338334-145b-4cb8-bd2d-cbac618352c3" />
      <p><i>Figure 7. Density plot of percent biases from all measurements (gray bars) and measurements by the 3 targets placed in different locations of the field of view and shot at different altitudes (1.92m and 2.41m). Dash lines are the mean percent bias from all measurements.</i></p>
    </div>
  </li>
  <li>The 200 calibrations estimated from the randomly selected checkerboard images (selected from the same pool of checkerboard images) show dramatic differences in their performances (Figure 8). The mean biases of the measurement ranged between +-20%. There is no further examination as to which checkboard images caused the biases.
    <br><br>
    <div align="center">
     <img width="1310" height="763" alt="Figure 8" src="https://github.com/user-attachments/assets/77861a0f-dc4e-4b4f-a55c-6464493f3477" />
    <p><i>Figure 8. Density plot of percent biases from all measurements (gray bars) and measurements by iterations. Dash lines are the mean percent bias from all measurements.</i></p>
    </div>
  </li>
</ol>

<h5>Conclusions</h5>

<ol style="text-align: left;">
  <li>The performance of different calibrations (in terms of percent images that have stereo altitude estimates and percent bias of measurement) varied dramatically, and therefore a calibration should be examined carefully and thoroughly before it is used officially.</li>
  <li>The 2015 post-cruise calibration (20150801) is the best calibration among all the calibrations tested.</li>
  <li>The calibration is not sensitive to the camera specifications - the 2015 post-cruise calibration (20150801) performed better than the 2018 post-cruise calibration (20181102) that were estimated using the checkerboard images taken during the calibration experiment.</li>
  <li>The calibration is sensitive to the checkerboard images used for the calibrations - the performances of calibration estimated from the same pool of checkerboard images (but randomly selected sets) differ greatly. Further examinations are required to see what checkerboard images caused the biases.</li>
  <li>The mean bias of measurement differs by 3 targets for unknown reasons. The target with scallop shells seems to be most stable.</li>
  <li>The mean bias of measurement differs when the targets are placed at different locations in the field of view. This is expected because the camera was not parallel to the target during the experiment, similar to the situation when the camera is shooting uneven surfaces and so the altitudes of any given points in the field of view relative to the camera are not the exactly same. The stereo altitude estimated is an average altitude of all points in the field of view.</li>
  <li>The biased measurements estimated from the annotations of images processed using a bad calibration can be corrected by reprocessing images using a good calibration and reestimating the measurements without reannotating the images. However, the correction is still not perfect so unless necessary, this situation should be avoided. The 2017 and 2018 NEFSC Habcam data were reprocessed using 2019 calibration that was estimated using the 2015 post-cruise checkerboard images without the third-polynomial term in the calibration model, the measurements were reestimated, and the scallop abundance and biomass estimates were updated accordingly.</li>
</ol>

<h3 id="sec-5-weeks" style="color: #2e7d32; text-align: left;">5 Weeks Out: Staff Notifications, Watch Bills & Berthing Assignments</h3>

<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Send “You are scheduled Email” notifying staff they have been selected for the survey. Include:
    <ul style="list-style-type: none; padding-left: 20px;">
      <li><input type="checkbox"> Survey expectations</li>
      <li><input type="checkbox"> Medical clearance forms</li>
      <li><input type="checkbox"> Dietary restrictions</li>
      <li><input type="checkbox"> Packing list (i.e. foul weather gear)</li>
      <li><input type="checkbox"> Preparing for sea packet</li>
    </ul>
  </li>
  <li><input type="checkbox"> Notify watch chiefs that they will be sailing in leadership positions</li>
  <li><input type="checkbox"> Create balanced watches with cruise personnel list</li>
  <li><input type="checkbox"> Assign berthing</li>
</ul>

<br>

<h4 id="sec-5wk-scheduled-email">Send "You Are Scheduled" Email & Participant Packet</h4>

<p>Send formal notification emails to all selected scientific personnel. Attach the complete participant packet containing the required forms, guidelines, and expectations outlined below.</p>

<h5 id="sec-5wk-survey-expectations">1. Survey Expectations</h5>
<p><i>[Insert survey expectations overview: 12-hour watch shifts, zero tolerance policies, data logging protocols, deck safety, and operational conduct]</i></p>

<blockquote>
  <b>Example Survey Expectations Summary:</b><br>
  • Scientific staff are expected to stand 12-hour daily watch rotations (6-on / 6-off or 12-on / 12-off).<br>
  • Active participation in gear deployment, image annotation quality control, and deck operations is required.<br>
  • Strict adherence to NOAA safety guidelines, including mandatory hard hats and safety vests during deck work.
</blockquote>

<br>

<h5 id="sec-5wk-medical-clearance">2. Medical Clearance Forms</h5>
<p><i>[Insert instructions for completing NOAA Health Services Form NHS 56-29, submission deadlines, and regional medical officer contact info]</i></p>

<p><b>Example Medical Clearance Form Checklist:</b></p>
<ul style="text-align: left;">
  <li>NOAA Form 56-29 (Report of Physical Examination)</li>
  <li>Tuberculosis (TB) Screening / PPD Test Verification</li>
  <li>Current prescription medication disclosures</li>
</ul>

<br>

<h5 id="sec-5wk-dietary-restrictions">3. Dietary Restrictions Form</h5>
<p><i>[Insert dietary restriction questionnaire link, galley submission protocols, and severe allergy notification steps]</i></p>

<p><b>Example Dietary Restriction Submission Form:</b></p>
<table width="100%" border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; text-align: left;">
  <tr bgcolor="#f2f2f2">
    <th>Participant Name</th>
    <th>Dietary Requirement (Vegetarian, Vegan, Gluten-Free, Halal, etc.)</th>
    <th>Severe Food Allergies (Nuts, Shellfish, Dairy, etc.)</th>
  </tr>
  <tr>
    <td><i>[Participant Name]</i></td>
    <td><i>[List Dietary Restrictions]</i></td>
    <td><i>[List Medical Allergies / Anaphylaxis Risk]</i></td>
  </tr>
</table>

<br>

<h5 id="sec-5wk-packing-list">4. Packing List (Foul Weather Gear)</h5>
<p><i>[Insert comprehensive offshore gear requirements, clothing recommendations, and prohibited items list]</i></p>

<p><b>Example Essential Packing List:</b></p>
<ul style="text-align: left;">
  <li><b>Personal Protective Equipment (PPE):</b> Steel-toe boots (ANSI rated), commercial foul weather gear (bibs and jacket).</li>
  <li><b>Work Attire:</b> Layered thermal clothing, non-slip deck shoes, work gloves, wool socks.</li>
  <li><b>Personal Items:</b> Government-issued ID/passport, personal prescription medications (1.5x cruise duration supply), toiletries, bed linen/towel (if required by vessel).</li>
</ul>

<br>

<h5 id="sec-5wk-preparing-for-sea">5. Full "Preparing for Sea" Packet</h5>
<p><i>[Insert full text/download link for the official NOAA / HabCam "Preparing for Sea" orientation packet, vessel emergency contacts, life-at-sea guidelines, and port access directions]</i></p>

<br>
<hr>
<br>

<h4 id="sec-5wk-watch-bills">Create Balanced Watch Bills</h4>

<p>Construct balanced 12-hour watch schedules pairing experienced sea-going personnel (Watch Chiefs, lead annotators) with novice scientists across Watch A and Watch B.</p>

<p><b>Example Watch Schedule Table:</b></p>

<div align="center">

<table width="100%" border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; text-align: left;">
  <thead>
    <tr bgcolor="#f2f2f2">
      <th>Watch Team</th>
      <th>Shift Hours</th>
      <th>Watch Chief</th>
      <th>Lead Annotator</th>
      <th>Watch Standers</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Watch A (Day)</b></td>
      <td>0000–0600 / 1200–1800</td>
      <td><i>[Name]</i></td>
      <td><i>[Name]</i></td>
      <td><i>[Name], [Name], [Name]</i></td>
    </tr>
    <tr>
      <td><b>Watch B (Night)</b></td>
      <td>0600–1200 / 1800–2400</td>
      <td><i>[Name]</i></td>
      <td><i>[Name]</i></td>
      <td><i>[Name], [Name], [Name]</i></td>
    </tr>
  </tbody>
</table>

</div>

<br>
<hr>
<br>

<h4 id="sec-5wk-berthing-assignments">Assign Berthing</h4>

<p>Assign stateroom berthing according to vessel stateroom layouts, watch schedules (separating day and night shifts to ensure uninterrupted sleep), and gender balance requirements.</p>

<p><b>Example Berthing Layout Plan:</b></p>

<div align="center">

<table width="100%" border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; text-align: left;">
  <thead>
    <tr bgcolor="#f2f2f2">
      <th>Stateroom #</th>
      <th>Deck / Location</th>
      <th>Berth Type</th>
      <th>Assigned Watch</th>
      <th>Occupants</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Room 101</b></td>
      <td>Main Deck / Port</td>
      <td>Double Bunk</td>
      <td>Watch A (Day)</td>
      <td>1. <i>[Name]</i><br>2. <i>[Name]</i></td>
    </tr>
    <tr>
      <td><b>Room 102</b></td>
      <td>Main Deck / Port</td>
      <td>Double Bunk</td>
      <td>Watch B (Night)</td>
      <td>1. <i>[Name]</i><br>2. <i>[Name]</i></td>
    </tr>
    <tr>
      <td><b>Room 103</b></td>
      <td>01 Deck / Starboard</td>
      <td>Double Bunk</td>
      <td>Watch A (Day)</td>
      <td>1. <i>[Name]</i><br>2. <i>[Name]</i></td>
    </tr>
    <tr>
      <td><b>Room 104</b></td>
      <td>01 Deck / Starboard</td>
      <td>Double Bunk</td>
      <td>Watch B (Night)</td>
      <td>1. <i>[Name]</i><br>2. <i>[Name]</i></td>
    </tr>
  </tbody>
</table>

</div>

<br>

<p><b>Quick Task:</b></p>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Notify watch chiefs that they will be sailing in leadership positions.</li>
</ul>

</div>

<h3 id="sec-1-week" style="color: #2e7d32; text-align: left;">1 Week Out: Logistics & Pre-Departure Briefings</h3>

<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Email the scientific party a few days prior to departure letting them know about:
    <ul style="list-style-type: none; padding-left: 20px;">
      <li><input type="checkbox"> Departure times</li>
      <li><input type="checkbox"> Meeting points</li>
      <li><input type="checkbox"> Parking procedures</li>
      <li><input type="checkbox"> Any last minute issues that may arise (bad weather, etc).</li>
    </ul>
  </li>
</ul>

<br>

<h4 id="sec-1wk-pre-departure-email">Pre-Departure Logistics Email to Scientific Party</h4>

<p>Send a comprehensive logistics email to all confirmed scientific personnel 3–5 days prior to sailing to finalize travel schedules, arrival coordinates, parking permits, and environmental contingency protocols.</p>

<h5 id="sec-1wk-departure-meeting-points">1. Departure Times & Meeting Points</h5>
<p><i>[Insert specific departure times, mandatory arrival buffers, vessel pier/dock location, and gate access codes]</i></p>

<blockquote>
  <b>Example Meeting & Arrival Details:</b><br>
  • <b>Vessel Location:</b> Pier 2, NOAA Marine Operations Dock / WHOI Facility, Woods Hole, MA.<br>
  • <b>Mandatory Boarding Time:</b> 0700 EDT on Departure Day (Vessel departs promptly at 0900 EDT).<br>
  • <b>Pre-Sailing Assembly Point:</b> Main pier loading bay adjacent to the survey gear staging area.
</blockquote>

<br>

<h5 id="sec-1wk-parking-procedures">2. Parking Procedures</h5>
<p><i>[Insert vehicle registration rules, long-term parking lot maps, dashboard permit display rules, and key handoff protocols]</i></p>

<blockquote>
  <b>Example Parking Instructions:</b><br>
  • All long-term vehicles must be parked in designated Scientist Lot C.<br>
  • Complete the NOAA/WHOI temporary parking slip and place it face-up on the driver’s side dashboard.<br>
  • Leave spare vehicle keys in the designated key locker near the Survey Refrigerator prior to boarding.
</blockquote>

<br>

<h5 id="sec-1wk-weather-protocols">3. Weather Protocols & Operational Limits</h5>
<p><i>[Insert meteorological tracking protocols, weather delay triggers, max sailing wind limits, and max operational towing limits]</i></p>

<blockquote>
  <b>Example Operational Weather Thresholds:</b><br>
  • <b>Max Sailing Wind (Transit Limit):</b> Sustained winds &gt; 35 knots or seas &gt; 10 ft trigger a departure delay assessment with the Captain.<br>
  • <b>Max Operational Wind (HabCam Deployment Limit):</b> Sustained winds &gt; 25 knots or seas &gt; 6 ft require halting vehicle towing operations and recovering the sled.<br>
  • <b>Weather Contingency Communication:</b> In the event of forecasted adverse weather, updates will be issued via email/SMS every 6 hours by the Chief Scientist.
</blockquote>

</div>

<div align="left" style="text-align: left !important;">

<h3 id="sec-staging" style="color: #2e7d32; text-align: left;">Staging Protocols: Deck Assembly & Navigation Setup</h3>

<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> <a href="02-hardware-and-schematics.md#weak-link">Mounting the weak link</a></li>
  <li><input type="checkbox"> <a href="02-hardware-and-schematics.md#fiber-optic-termination">Splice fiber optics</a></li>
  <li><input type="checkbox"> <a href="02-hardware-and-schematics.md#pull-test">Do the pull test</a></li>
  <li><input type="checkbox"> Load vehicle</li>
  <li><input type="checkbox"> Load equipment</li>
  <li><input type="checkbox"> Setup stations</li>
  <li><input type="checkbox"> Provide the captain/bridge with the .GPX file of station locations so they can import it into their navigation software and check tracklines and make recommendations for any shifts in waypoints.</li>
  <li><input type="checkbox"> Chanos sensor dissolved inorganic carbon sensor (PH, DIC, total alkalinity)</li>
</ul>

<br>

<h4 id="sec-staging-weak-link">Mounting the Weak Link</h4>
<p><i>Refer to <a href="02-hardware-and-schematics.md#weak-link">02 Hardware & Schematics (Section 6: Mechanical Weak Link Assembly)</a> for detailed instructions.</i></p>

<h4 id="sec-staging-fiber-splicing">Splice Fiber Optics</h4>
<p><i>Refer to <a href="02-hardware-and-schematics.md#fiber-optic-termination">02 Hardware & Schematics (Section 7: Fiber Optic Termination)</a> for detailed instructions.</i></p>

<h4 id="sec-staging-pull-test">Do the Pull Test</h4>
<p><i>Refer to <a href="02-hardware-and-schematics.md#pull-test">02 Hardware & Schematics (Section 9: Fiber Optics Pull Test Protocol)</a> for detailed instructions.</i></p>

<h4 id="sec-staging-load-vehicle">Load Vehicle</h4>
<p><i>[Insert details for vehicle deck loading, crane hoisting protocols, tie-down locations, and secure deck placement here]</i></p>

<h4 id="sec-staging-load-gear">Load Equipment</h4>
<p><i>[Insert details for loading auxiliary crates, spare parts, toolboxes, calibration targets, and laboratory hardware here]</i></p>

<h4 id="sec-staging-setup-stations">Setup Stations</h4>
<p><i>[Insert detailed station setup instructions here]</i></p>

<p>HabCam operations aboard the R/V <i>Henry B. Bigelow</i> are distributed across four main laboratory spaces: the Acoustic Lab (Primary Control Center), Dry Lab, Chemistry Lab, and Cutting Room.</p>

<div align="center">
  <img width="800" src="PASTE_BIGELOW_LAYOUT_MAP_HERE.jpg" alt="R/V Henry B. Bigelow Lab Layout Map" />
  <p><i>Figure 1: R/V Henry B. Bigelow Acoustic Lab & Dry Lab Layout Map</i></p>
</div>

<br>

<h5 id="sec-station-acoustic-lab">1. Acoustic Lab Command Center Overview</h5>
<p>The Acoustic Lab serves as the primary HabCam flight and monitoring hub. It houses 4 distinct stations operated by NOAA Fisheries personnel and Ship Survey Technicians:</p>

<ul style="text-align: left;">
  <li><b>Watch Chief Station:</b> Located in the rear row with a 2-monitor setup directly behind the flight team.</li>
  <li><b>Co-Pilot Station:</b> Located in the front row (left) with a dedicated 4-monitor array.</li>
  <li><b>Pilot Station:</b> Located in the front row (right) with a 4-monitor array, vehicle joystick, and winch controller.</li>
  <li><b>Survey Technician Station:</b> Located adjacent to the flight team to monitor shipboard multibeam, EK-80, and vessel navigation.</li>
</ul>

<div align="center">
  <img width="1012" height="616" alt="Acoustic Lab" src="https://github.com/user-attachments/assets/44782226-f3e3-40e1-92d1-ecf85a5b51b2" />
  <p><i>Acoustic Lab Wall of Monitors & Operator Workstations Overview</i></p>
</div>

<br>

<h5 id="sec-station-watch-chief">2. Watch Chief Station</h5>
<p>Operated on 12-hour rotating shifts (2 Watch Chiefs per cruise) to maintain continuous leadership, maintenance oversight, and quality control.</p>

<ul style="text-align: left;">
  <li><b>Hardware Setup:</b> 2-monitor workstation positioned behind the Pilot/Co-Pilot.</li>
  <li><b>Primary Responsibilities:</b> Watch roster assignment, training new scientists on flight operations, reviewing image quality, and beginning preliminary image annotations.</li>
</ul>

<div align="center">
  <img width="748" height="560" alt="Watch Chief Station" src="https://github.com/user-attachments/assets/3838154c-1232-4db9-8562-11d5500e8230" />
  <p><i>Watch Chief Workstation (Positioned Behind Pilot/Co-Pilot)</i></p>
</div>

<br>

<h5 id="sec-station-copilot">3. Co-Pilot Station</h5>
<p>Positions the Co-Pilot to the left of the Pilot to continuously monitor imaging telemetry, software health, and incoming seabed features.</p>

<div align="center">
  <img width="624" height="468" alt="Pilot-Copilot Station" src="https://github.com/user-attachments/assets/5416a5f1-3344-4d50-87c1-57e6d76d70de" />
  <p><i>Co-Pilot Workstation Array</i></p>
</div>

<br>

<table width="100%" border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; text-align: left;">
  <thead>
    <tr bgcolor="#f2f2f2">
      <th width="20%">Monitor #</th>
      <th width="30%">Application / Display</th>
      <th width="50%">Operational Function & Image Placement</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Monitor 1</b></td>
      <td><b>EK-80 Scientific Echo Sounder</b></td>
      <td>
        Mirrored feed from Survey Techs displaying water column echograms, seafloor depth, and early warnings for incoming sand waves.
        <br><br>
        <div align="center">
        <img width="791" height="493" alt="EK80" src="https://github.com/user-attachments/assets/c8446f53-c1c9-4f32-beef-7187cb7b4ef4" />
        </div>
      </td>
    </tr>
    <tr>
      <td><b>Monitor 2</b></td>
      <td><b>Engineering GUI & Event Logger</b></td>
      <td>
        Live raw sensor feeds (AHRS, CTD, Oxygen, Fluorometer), GPS coordinates, fathometer depth, active file logging status, and event tagging.
        <br><br>
        <div align="center">
         <img width="779" height="583" alt="Engineering" src="https://github.com/user-attachments/assets/188c9b0a-f43e-4813-98d0-6843f1e072cc" />
        </div>
      </td>
    </tr>
    <tr>
      <td><b>Monitor 3</b></td>
      <td><b>Coastal Explorer Navigation</b></td>
      <td>
        Mirrored navigation software displaying planned tracklines, waypoints, vessel speed, and potential subsea hazards/wrecks.
        <br><br>
        <div align="center">
        <img width="776" height="468" alt="Coastal Explorer" src="https://github.com/user-attachments/assets/48d68f7b-5652-4b44-8576-4c04daa0250c" />
          </div>
      </td>
    </tr>
    <tr>
      <td><b>Monitor 4</b></td>
      <td><b>Image Viewer (`dsvimview`)</b></td>
      <td>
        Live stereo camera image waterfall; allows toggling port/starboard feeds, adjusting display rates, and checking camera trigger health.
        <br><br>
        <div align="center">
         <img width="776" height="582" alt="Image Viewer" src="https://github.com/user-attachments/assets/82b1563c-dd64-4e62-a724-7f7fb7ff1288" />
        </div>
      </td>
    </tr>
  </tbody>
</table>

<br>

<h5 id="sec-station-pilot">4. Pilot Station</h5>
<p>Positions the Pilot to the right of the Co-Pilot with direct access to the vehicle control joystick and hydraulic winch controls.</p>

<div align="center">
  <img width="624" height="468" alt="Pilot-Copilot Station" src="https://github.com/user-attachments/assets/edc685b3-6484-43a0-90a5-6c472f8e4a71" />
  <p><i>Pilot Workstation Overview & Controls</i></p>
</div>

<br>

<table width="100%" border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; text-align: left;">
  <thead>
    <tr bgcolor="#f2f2f2">
      <th width="20%">Monitor #</th>
      <th width="30%">Application / Display</th>
      <th width="50%">Operational Function & Image Placement</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Monitor 5</b></td>
      <td><b>Live Winch & Deck Video (`VxOpsCenter`)</b></td>
      <td>
        CCTV camera feeds monitoring the oceanographic winch drum, wire spooling, and aft deck operations.
        <br><br>
        <div align="center">
        <img width="776" height="400" alt="Live Winch Video" src="https://github.com/user-attachments/assets/1a9e97b7-d555-4a0d-b82c-fcb099fd84d6" />
        </div>
      </td>
    </tr>
    <tr>
      <td><b>Monitor 6</b></td>
      <td><b>Bottom Tracking (`dsvimview` / Dixon Screen)</b></td>
      <td>
        Real-time vehicle altitude, computed bottom profile, fish depth, and altimeter filtering for flight adjustments.
        <br><br>
        <div align="center">
        <img width="776" height="487" alt="Bottom Tracking" src="https://github.com/user-attachments/assets/cc31d27d-6b90-40d6-af40-e8c97fcbaaa6" />
          </div>
      </td>
    </tr>
    <tr>
      <td><b>Monitor 7</b></td>
      <td><b>BlueView Forward Sonar</b></td>
      <td>
        Acoustic sector sweep displaying subsea obstacles, boulders, and terrain relief ahead of the vehicle.
        <br><br>
        <div align="center">
         <img width="771" height="452" alt="Blueview" src="https://github.com/user-attachments/assets/faf1560b-5f96-4e49-b317-561f286bdb45" />
        </div>
      </td>
    </tr>
    <tr>
      <td><b>Monitor 8</b></td>
      <td><b>Pentagon Winch Control Display</b></td>
      <td>
        MacGregor / Rapp Marine interface displaying cable tension (tons), line speed (m/min), and paid-out cable length (m).
        <br><br>
        <div align="center">
        <img width="624" height="468" alt="Winch Control" src="https://github.com/user-attachments/assets/cb6f39f2-0f83-4e67-96f6-cfb30e784d47" />
          </div>
      </td>
    </tr>
  </tbody>
</table>

<br>

<h5 id="sec-station-auxiliary-labs">5. Annotation & Auxiliary Laboratory Stations</h5>
<p>Image processing, secondary scientific analysis, and physical sample handling are distributed across three auxiliary spaces:</p>

<ul style="text-align: left;">
  <li><b>Dry Lab:</b> Contains Annotation Station 1, Annotation Station 2, the Backup Annotation Station, and the primary timeserver rack.
    <br><br>
    <div align="center">
     <img width="1059" height="640" alt="Dry Lab" src="https://github.com/user-attachments/assets/1fa09e51-5fe0-4470-9aab-3e00c0ffe41d" />
    </div>
  </li>
  <li><b>Chemistry Lab:</b> Contains Annotation Station 3, Annotation Station 4, chemistry fume hood, and science freezers.
    <br><br>
    <div align="center">
     <img width="1009" height="616" alt="Chem Lab" src="https://github.com/user-attachments/assets/86111237-c3b2-441c-9b60-a564766beb3d" />
    </div>
  </li>
  <li><b>Cutting Room:</b> Dedicated HabCam workspace (Cutting Table 1) for physical biological sampling, sorting belt operations, and sample freezer access.
    <br><br>
    <div align="center">
     <img width="958" height="582" alt="Cutting Room" src="https://github.com/user-attachments/assets/f1750dc6-8862-40da-a30f-c614ff6d811c" />
     </div>
  </li>
</ul>

</div>

<h4 id="sec-staging-gpx-file">Bridge .GPX File & Station Transects</h4>
<p><i>[Insert details on assigning survey transects, saving/exporting the .GPX file, delivering tracklines to the captain/bridge, and protocols for modifying waypoints based on captain's feedback here]</i></p>

<h4 id="sec-staging-chanos">Chanos Sensor (pH, DIC, Total Alkalinity)</h4>
<p><i>[Insert details for Chanos sensor mounting, reagent preparation, fluidic connections, and calibration protocols here]</i></p>

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

<br>
