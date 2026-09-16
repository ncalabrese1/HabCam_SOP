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

<h3 id="chk-6-months" style="color: #2e7d32; text-align: left;">
  <a href="#sec-6-months" style="color: #2e7d32; text-decoration: underline;">6 Months out: ~ November</a>
</h3>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Confirm ship time and set cruise date</li>
  <li><input type="checkbox"> Send Seabird 37, Seabird 49 CTDs and Wetlabs ecotriplet puck to Washington for Calibrations [Return to Manufacturer Authorization (RMA) form]</li>
  <li><input type="checkbox"> Begin ordering equipment and supplies needed before upcoming cruise [itemized ordering guide here]</li>
  <li><input type="checkbox"> Send out any equipment that was damaged from last survey</li>
</ul>

<h3 id="chk-15-weeks" style="color: #2e7d32; text-align: left;">
  <a href="#sec-15-weeks" style="color: #2e7d32; text-decoration: underline;">15 Weeks out:</a>
</h3>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> If ITD hasn't reached out to have computer software security added to machines prior to surveys (i.e. patched), check-in</li>
</ul>

<h3 id="chk-12-weeks" style="color: #2e7d32; text-align: left;">
  <a href="#sec-12-weeks" style="color: #2e7d32; text-decoration: underline;">12 Weeks out:</a>
</h3>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Set up all servers with 2026 software directories and GUIs</li>
  <li><input type="checkbox"> Collect flashdrive from POPDY and Install R packages on annotation machines</li>
  <li><input type="checkbox"> Verify that IP address can be changed on annotation machines</li>
  <li><input type="checkbox"> Ensure sonar software and coastal explorer are installed on 2 field laptops</li>
</ul>

<h3 id="chk-10-weeks" style="color: #2e7d32; text-align: left;">
  <a href="#sec-10-weeks" style="color: #2e7d32; text-decoration: underline;">10 Weeks out:</a>
</h3>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Hand-off Clevis to Shellfish group to have the epoxy burned out at Reidar's in New Bedford</li>
  <li><input type="checkbox"> Ensure Seabird 37, Seabird 49 and Wetlabs ecotriplet puck have returned from Washington</li>
  <li><input type="checkbox"> Ensure any damaged equipment sent for repairs has been returned</li>
  <li><input type="checkbox"> Create a new HABCAM database on Postgres servers</li>
  <li><input type="checkbox"> Confirm previous years data has been offloaded</li>
  <li><input type="checkbox"> Clear server drives</li>
  <li><input type="checkbox"> Reformat back-up drives</li>
</ul>

<h3 id="chk-8-weeks" style="color: #2e7d32; text-align: left;">
  <a href="#sec-8-weeks" style="color: #2e7d32; text-decoration: underline;">8 Weeks out:</a>
</h3>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Prepare HABCAM for WHOI Sundance Tank Calibration Test</li>
  <li><input type="checkbox"> Pack supply kit for WHOI sundance tank calibration test</li>
  <li><input type="checkbox"> If applicable, install chanos onto tow sled</li>
  <li><input type="checkbox"> Science center staffing call</li>
</ul>

<h3 id="chk-6-weeks" style="color: #2e7d32; text-align: left;">
  <a href="#sec-6-weeks" style="color: #2e7d32; text-decoration: underline;">6 Weeks out:</a>
</h3>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Take vehicles to WHOI sea water tank test to calibrate equipment (<a href="https://example.com" target="_blank">Camera calibrations for dummies</a>)</li>
  <li><input type="checkbox"> Repair or Resolve any issues that came up during the WHOI tank test</li>
  <li><input type="checkbox"> Store Vehicle at netloft until staging</li>
  <li><input type="checkbox"> Replace batteries in Pinger (Benthos UAT 376 acoustic transponder)</li>
</ul>

<h3 id="chk-5-weeks" style="color: #2e7d32; text-align: left;">
  <a href="#sec-5-weeks" style="color: #2e7d32; text-decoration: underline;">5 Weeks out:</a>
</h3>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Send “You are scheduled Email” notifying staff they have been selected for the survey. Include:</li>
  <li><input type="checkbox"> Notify watch chiefs that they will be sailing in leadership positions</li>
  <li><input type="checkbox"> Create balanced watches with cruise personnel list</li>
  <li><input type="checkbox"> Assign berthing</li>
</ul>

<h3 id="chk-1-week" style="color: #2e7d32; text-align: left;">
  <a href="#sec-1-week" style="color: #2e7d32; text-decoration: underline;">1 Week out:</a>
</h3>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Email the scientific party a few days prior to departure letting them know about...</li>
</ul>

<h3 id="chk-staging" style="color: #2e7d32; text-align: left;">
  <a href="#sec-staging" style="color: #2e7d32; text-decoration: underline;">Staging</a>
</h3>
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

<h3 id="chk-departure" style="color: #2e7d32; text-align: left;">
  <a href="#sec-day-of-departure" style="color: #2e7d32; text-decoration: underline;">Day of Departure:</a>
</h3>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> If leaving from WH store vehicle keys in the locker by the Survey refrigerator. Parking forms must be filled out and placed on the car dashboard.</li>
  <li><input type="checkbox"> When heading to Newport, RI, keep the ship informed about the science party’s arrival time.</li>
  <li><input type="checkbox"> Ensure all members of scientific party are aboard</li>
  <li><input type="checkbox"> Muster to bridge 30 min prior to departure time</li>
  <li><input type="checkbox"> Inspect underwater cables for damage and/or voltage leaks.</li>
  <li><input type="checkbox"> Host an on-board, pre-cruise meeting with scientific staff</li>
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

<div align="left" style="text-align: left !important;">

<h3 id="sec-day-of-departure" style="color: #2e7d32; text-align: left;">Day of Departure Protocols</h3>

<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> If leaving from WH store vehicle keys in the locker by the Survey refrigerator. Parking forms must be filled out and placed on the car dashboard.</li>
  <li><input type="checkbox"> When heading to Newport, RI, keep the ship informed about the science party’s arrival time.</li>
  <li><input type="checkbox"> Ensure all members of scientific party are aboard</li>
  <li><input type="checkbox"> Muster to bridge 30 min prior to departure time</li>
  <li><input type="checkbox"> Inspect underwater cables for damage and/or voltage leaks.</li>
  <li><input type="checkbox"> Host an on-board, pre-cruise meeting with scientific staff</li>
  <li><input type="checkbox"> Track federal employee time</li>
</ul>

<br>

<h4 id="sec-dayof-precruise-meeting">Host On-Board Pre-Cruise Meeting</h4>

<p style="margin-bottom: 4px;">Host the mandatory pre-cruise orientation meeting with all scientific staff prior to departure to establish shift leadership, review safety expectations, and outline initial survey logistics.</p>

<ul style="margin-top: 2px; margin-left: 25px; padding-left: 0; text-align: left;">
  <li>Perform Introductions; Thank everyone for participating</li>
  <li><span style="background-color: #ffff00; color: #000000; padding: 2px 4px;"><b>Identify Watch Chief for first shift; they must be listened to concerning FSCS procedures</b></span></li>
  <li>Announce area of operation, general cruise direction, and ETA to first station, and sequence of events at station</li>
  <li>Emphasize importance of ‘Safety First’ (i.e. hard hats and safety vests)</li>
  <li>Go over protocols for injuries</li>
  <li>Relieve other watch 10 mins early</li>
  <li>Remind Scientific Staff to notify Watch Chief and Chef of any food allergies</li>
  <li>Ensure watch times on day of departure/arrival are divided equally for pay purposes</li>
</ul>

<h5 id="sec-dayof-sequence-of-events">Sequence of Events at Station</h5>
<p><i>[Insert detailed sequence of events at station here, including vehicle deployment steps, logging initiation, recovery protocols, and watch handover procedures]</i></p>

<h5 id="sec-dayof-safety-protocols">Safety Protocols</h5>
<p><i>[Insert detailed safety protocols here, including mandatory personal protective equipment (PPE) requirements such as hard hats, safety vests, steel-toe boots, and deck safety rules]</i></p>

<h5 id="sec-dayof-injury-protocols">Injury Protocols</h5>
<p><i>[Insert detailed injury protocols here, including immediate medical response steps, notifying the Chief Scientist and Vessel Medical Officer, and completing official incident documentation]</i></p>

<br>

<h4 id="sec-dayof-track-federal-time">Track Federal Employee Time</h4>
<p><i>[Insert detailed instructions on how to track federal employee time here, including daily timekeeping accounting, agency codes, sea pay/overtime rules, and pay period submission protocols]</i></p>

</div>

<div align="left" style="text-align: left !important;">

<h4 id="sec-staging-setup-stations">Setup Stations</h4>

<h2 id="field-team-roles-table">4. Field Team Roles Table</h2>

<p><b>Cruise Manning Structure & Shift Operations:</b> The HabCam scientific party typically consists of 9 to 10 personnel operating on 24-hour continuous sea trials divided into two 12-hour watch rotations (e.g., 11:30 AM to 11:30 PM and 11:30 PM to 11:30 AM)[cite: 5]. Each shift is managed by a Watch Chief and includes a rotating team of Pilots, Co-Pilots, and Annotators who cycle stations every 30 to 60 minutes to prevent screen fatigue[cite: 5]. The Chief Scientist maintains active oversight across both watches (6 AM to 6 PM baseline plus as-needed response)[cite: 5].</p>

<table width="100%" border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; text-align: left;">
  <thead>
    <tr bgcolor="#f2f2f2">
      <th width="20%">Role</th>
      <th width="15%">Manning / Shift</th>
      <th width="65%">Primary High-Level Responsibilities</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Chief Scientist</b></td>
      <td>1 Person (Floating / Day)</td>
      <td>Primary liaison between scientific party, vessel crew, and shore support; leads survey trackline design, staffing, daily safety briefings, and on-the-spot decision making.</td>
    </tr>
    <tr>
      <td><b>HabCam Lead</b></td>
      <td>1 Person (Technical Lead)</td>
      <td>Technical authority for hardware, fiberoptic terminations, server configuration, GPS time syncing, navigation integration, light maps, and data redundancy.</td>
    </tr>
    <tr>
      <td><b>Watch Chief</b></td>
      <td>2 People (1 per 12-hr shift)</td>
      <td>Direct shift supervisor; manages station role rotations, controls core flight software startup/shutdown, trains new scientists, and conducts shift QA/QC.</td>
    </tr>
    <tr>
      <td><b>Pilot</b></td>
      <td>Rotating (30–60 min blocks)</td>
      <td>Actively flies vehicle via hydraulic winch joystick; maintains target altitude above seafloor using live camera feeds, flight GUI, and forward-looking sonar.</td>
    </tr>
    <tr>
      <td><b>Co-Pilot</b></td>
      <td>Rotating (30–60 min blocks)</td>
      <td>Second pair of eyes for Pilot; monitors dual camera feeds, telemetry, and sonar for sand waves/boulders; optimizes camera/sonar settings; mitigates software glitches.</td>
    </tr>
    <tr>
      <td><b>Annotator</b></td>
      <td>Rotating (30–60 min blocks)</td>
      <td>Frontline image processor; logs primary targets (scallops/fish) and secondary substrate/habitat data from incoming 10-minute image batches.</td>
    </tr>
    <tr>
      <td><b>QA/QC Lead</b></td>
      <td>1 Person / PopDyn</td>
      <td>Hosts pre-cruise training, maintains identification guides, instructs scientists on protocols, and audits/certifies ~30 baseline images per annotator.</td>
    </tr>
    <tr>
      <td><b>Population Dynamics</b></td>
      <td>1–2 People</td>
      <td>Quantitative scientist; collaborates on trackline design, executes camera calibrations, verifies altimeter confidence, and synthesizes population data.</td>
    </tr>
  </tbody>
</table>

<br>
<hr>
<br>

<h2 id="field-team-roles-overview">5. Field Team Roles Overview</h2>

<div align="left" style="text-align: left !important;">

<h3 id="role-chief-scientist" style="color: #2e7d32;">Chief Scientist</h3>
<p>Acts as the primary liaison between the scientific party, the vessel's crew, and shore-based support. Responsible for overall cruise execution, safety, trackline planning, and maintaining an open-door policy.</p>

<ul style="text-align: left;">
  <li><b>Submit Ship Time Requests:</b> Draft and submit formal administrative requests to secure vessel availability aligned with scientific objectives.</li>
  <li><b>Plan the Survey and Tracklines:</b> Lead overarching scientific design, mapping out geographical scope and adjusting routes dynamically for weather or bathymetry.</li>
  <li><b>Personnel Selection and Staffing:</b> Recruit and assemble a balanced scientific team with the necessary technical and watchstanding expertise.</li>
  <li><b>Cruise Plan Updates:</b> Finalize operational schedules and delegate updates to co-leads for uninterrupted operational continuity.</li>
  <li><b>Inter-Crew Communication & Captain Liaison:</b> Facilitate daily communication with the Captain and ship's command regarding navigation, weather, and safety.</li>
  <li><b>Brief Watch Chiefs & Shift Transitions:</b> Proactively update shift leaders on scientific priorities, altered tracklines, and operational changes prior to watch changes.</li>
  <li><b>Active Oversight & Daily Safety Briefings:</b> Maintain active presence for at least half of every watch shift and lead mandatory daily safety meetings at sea.</li>
</ul>

<br>

<h3 id="role-habcam-lead" style="color: #2e7d32;">HabCam Lead</h3>
<p>The primary technical authority responsible for vehicle hardware deployment, data integrity, and subsea/shipboard IT infrastructure.</p>

<ul style="text-align: left;">
  <li><b>Execute Fiberoptic Termination:</b> Perform precise fiberoptic splicing and clevis termination through the hydraulic winch line to guarantee low-loss telemetry.</li>
  <li><b>Configure IT Infrastructure & Servers:</b> Set up main HabCam servers, control stations, annotation computers, and local network switches.</li>
  <li><b>Install GPS Time Server & Navigation Integration:</b> Configure master GPS time synchronization and link shipboard GPS/fathometer feeds to vehicle logging systems.</li>
  <li><b>Server Maintenance & Data Monitoring:</b> Verify storage drive mounting, Apache web server status, and real-time raw image/sensor data writes.</li>
  <li><b>Build Light Maps & Oversee Image Pipeline:</b> Generate illumination correction maps and verify processed images serve smoothly to annotation workstations.</li>
  <li><b>Metadata QA/QC & Continuous Data Backups:</b> Verify PostgreSQL database integrity and execute automated redundant backups onto spare drives.</li>
  <li><b>Vehicle Pre-Dive Checks & Troubleshooting:</b> Lead pre-deployment deck inspections and rapidly resolve electrical, mechanical, or software faults.</li>
</ul>

<br>

<h3 id="role-watch-chief" style="color: #2e7d32;">Watch Chief</h3>
<p>Direct shift supervisor managing personnel, flight software operations, and biological data collection during assigned 12-hour rotations.</p>

<ul style="text-align: left;">
  <li><b>Manage 12-Hour Operational Shifts:</b> Command continuous watch shifts and execute thorough handovers with the counterpart Watch Chief.</li>
  <li><b>Assign Station Rotations:</b> Create and enforce station schedules (Pilot, Co-Pilot, Annotator) rotating personnel every 30–60 minutes to manage fatigue.</li>
  <li><b>Control Flight Software Systems:</b> Safely launch, monitor, and shut down pilot and co-pilot control software and logging interfaces.</li>
  <li><b>Train & Onboard Scientific Staff:</b> Conduct standardized training for new annotators and flight standers using reference slide decks.</li>
  <li><b>Integrate into Active Rotation:</b> Lead by example by taking regular turns at pilot, co-pilot, and annotation stations.</li>
  <li><b>Shift Data QA/QC:</b> Review logged species identifications and habitat classifications to correct entry errors before shift sign-off.</li>
</ul>

<br>

<h3 id="role-pilot" style="color: #2e7d32;">Pilot</h3>
<p>Responsible for the active, real-time underwater navigation and altitude control of the HabCam vehicle above the seabed.</p>

<ul style="text-align: left;">
  <li><b>Execute Timed Rotations (30–60 Minutes):</b> Operate in short, high-concentration blocks to maintain sharp reflexes and situational awareness.</li>
  <li><b>Maintain Safe Seafloor Altitude:</b> Continuously adjust winch controls to keep the vehicle at the target photographic altitude (typically ~2m) above bottom.</li>
  <li><b>Operate Winch Joystick:</b> Command vertical vehicle movement using the physical winch joystick to pay out or haul in tow cable.</li>
  <li><b>Monitor Telemetry & Forward Sonar:</b> Synthesize live camera video, flight GUI metrics (pitch, roll, tension), and forward-looking sonar to detect and avoid subsea hazards (boulders, wrecks, drop-offs).</li>
</ul>

<br>

<h3 id="role-copilot" style="color: #2e7d32;">Co-Pilot</h3>
<p>Acts as the technical support partner and second pair of eyes for the Pilot to ensure flight safety and sensor data quality.</p>

<ul style="text-align: left;">
  <li><b>Execute Timed Rotations (30–60 Minutes):</b> Rotate alongside the Pilot to maintain continuous vigilance across telemetry displays.</li>
  <li><b>Monitor Dual Cameras & Sensor Telemetry:</b> Verify camera lighting, exposure, and continuous data logging across all environmental sensors (CTD, Oxygen, Fluorometer).</li>
  <li><b>Sonar Hazard & Topography Analysis:</b> Interpret sonar displays for upcoming hazards and terrain changes (e.g., sand waves) requiring rhythmic winch adjustments.</li>
  <li><b>Pilot Verbal Communication:</b> Maintain clear, concise verbal alerts to notify the Pilot immediately of upcoming obstacles or depth changes.</li>
  <li><b>Real-Time Instrument Optimization & Software Mitigation:</b> Adjust camera frame rates, sonar ranges, and winch settings; immediately troubleshoot station software freezes or network glitches.</li>
</ul>

<br>

<h3 id="role-annotator" style="color: #2e7d32;">Annotator</h3>
<p>Frontline scientific data processor responsible for identifying, counting, and recording biological and habitat targets from incoming imagery.</p>

<ul style="text-align: left;">
  <li><b>Execute Timed Rotations (30–60 Minutes):</b> Process imagery in focused blocks alongside co-annotators to maintain high visual accuracy.</li>
  <li><b>Process Image Assignments:</b> Rapidly review 10-minute image batches, logging primary targets (commercial species/fish) and secondary environmental parameters (substrate, encrusting organisms).</li>
  <li><b>Complete Mandatory Protocol Training:</b> Complete pre-cruise or under-sail identification training to align species classification standards with project guidelines.</li>
</ul>

<br>

<h3 id="role-qaqc-lead" style="color: #2e7d32;">QA/QC Lead</h3>
<p>Primary auditor and educator guarding scientific data integrity across the annotation team.</p>

<ul style="text-align: left;">
  <li><b>Host Pre-Cruise Training Overview:</b> Lead mandatory orientation outlining data quality standards, species identification guides, and target priorities.</li>
  <li><b>Instruct Standardized Protocols:</b> Teach exact identification criteria, substrate classifications, and efficient software operation.</li>
  <li><b>Audit & Certify Annotators:</b> Review, grade, and verify a baseline sample set of ~30 images for every annotator to calibrate accuracy before independent logging.</li>
</ul>

<br>

<h3 id="role-population-dynamics" style="color: #2e7d32;">Population Dynamics Specialist</h3>
<p>Lead quantitative scientist linking field data acquisition with statistical modeling, stock assessment, and spatial analysis.</p>

<ul style="text-align: left;">
  <li><b>Strategic Trackline Planning & Dynamic Routing:</b> Collaborate with Chief Scientist to design survey routes based on depth stratification and historical distribution, updating lines dynamically for weather or time constraints.</li>
  <li><b>Integrate into Operational Watch Rotation:</b> Stand regular shifts as Pilot, Co-Pilot, and Annotator to maintain direct understanding of data collection conditions.</li>
  <li><b>Camera Calibrations & Altimeter Verification:</b> Oversee tank/field camera calibrations, calculate altimeter confidence intervals, and determine exact swept-area scale metrics.</li>
  <li><b>Data Synthesis & Reporting:</b> Aggregate biological annotations, identify spatial coverage gaps, summarize population trends, and present preliminary statistical findings to leadership.</li>
</ul>

<br>

</div>

<h2 id="field-team-roles-full-spec">6. Detailed Field Team Roles and Expectations</h2>

<div align="left" style="text-align: left !important;">

<h3 id="spec-chief-scientist" style="color: #2e7d32;">CHIEF SCIENTIST</h3>

<p>As the Chief Scientist, you act as the primary liaison between the scientific party, the vessel's crew, and shore-based support. You must be prepared to make decisive, on-the-spot decisions at any time of day or night to ensure the success and safety of the mission. Maintaining an open-door policy is essential to foster a communicative and supportive environment.</p>

<p>In addition to these duties, you are responsible for:</p>

<ul style="text-align: left;">
  <li><b>Submit Ship Time Requests:</b> Take charge of the administrative process required to secure vessel availability. This involves drafting and submitting formal requests to the appropriate scheduling bodies or funding, ensuring that the requested dates align with the mission's scientific objectives and seasonal requirements.</li>
  <li><b>Plan the Survey and Decide on Tracklines:</b> Lead the overarching scientific design of the survey. You will map out the geographical scope of the survey, establish precise tracklines (routes) for data collection, and determine the most efficient deployment of instruments. You must also be ready to adapt these plans dynamically in response to weather, sea conditions, or preliminary findings.</li>
  <li><b>Personnel Selection and Staffing:</b> Assemble a highly capable scientific team. You are responsible for identifying, recruiting, and selecting qualified researchers, technicians, and watchstanders, ensuring the team possesses a balanced mix of skills, experience, and expertise necessary to achieve the cruise's specific goals.</li>
  <li><b>Complete and Delegate Cruise Plan Updates:</b> Maintain the official cruise plan as a living document. You will finalize all operational schedules, scientific protocols, and logistical details, keeping the document updated as parameters change. You must pass these updates onto your co-lead to ensure uninterrupted operational continuity and shared leadership.</li>
  <li><b>Facilitate Communications Between Crews:</b> Serve as the central communication hub. You must bridge the gap between the scientific party and the maritime professionals operating the vessel, ensuring that both groups understand each other's needs, limitations, and daily objectives to maintain a harmonious and productive working environment.</li>
  <li><b>Interact with the Vessel Captain and Crew:</b> Cultivate a strong, collaborative relationship with the ship's command. This requires regular, professional meetings with the Captain and senior crew to discuss navigation, logistical feasibility, impending weather systems, and the safe execution of complex scientific operations.</li>
  <li><b>Update Watch Chiefs:</b> Empower your shift leaders. You are responsible for consistently briefing the Watch Chiefs on the broader scientific objectives, current equipment status, and any deviations from the primary plan, ensuring they have the information required to effectively manage their respective teams.</li>
  <li><b>Communicate Changes for the Upcoming Watch:</b> Guarantee smooth shift transitions. Before a new watch takes over, you must proactively communicate any immediate shifts in strategy, altered tracklines, weather-related delays, or new scientific priorities so the oncoming team can hit the ground running without confusion.</li>
  <li><b>Maintain Active Oversight During Watches:</b> Provide hands-on leadership and support. You are expected to be awake, physically present, and actively engaged for at least half of every single watch shift (day and night). This ensures you are available to troubleshoot equipment, guide data collection, and make immediate judgment calls.</li>
  <li><b>Conduct Daily Safety Briefings at Sea:</b> Champion a culture of safety. You will lead mandatory daily meetings with the scientific team to review general emergency protocols, address specific operational hazards anticipated for that day's operations, and ensure that all personnel remain vigilant and secure while at sea.</li>
</ul>

<br>

<h3 id="spec-habcam-lead" style="color: #2e7d32;">HABCAM LEAD</h3>

<p>As the HABCAM Lead, you are the primary technical authority responsible for the deployment, operation, and data integrity of the imaging system. You manage both the physical hardware of the vehicle and the IT infrastructure required to process its data.</p>

<p>Your responsibilities include:</p>

<ul style="text-align: left;">
  <li><b>Perform Fiberoptic Termination:</b> Execute precise fiberoptic splicing and termination through the hydraulic winch line to ensure high-speed data transmission between the underwater HABCAM vehicle and the shipboard servers. This requires minimizing signal loss to guarantee reliable, real-time communication and video feeds.</li>
  <li><b>Configure HABCAM IT Infrastructure:</b> Lead the setup of all specialized hardware and networking. This includes deploying and configuring the main HABCAM servers, pilot and co-pilot control stations, and annotation machines, ensuring seamless network integration and communication across the entire system.</li>
  <li><b>Install and Calibrate the GPS Time Server:</b> Configure the dedicated GPS used for the network's time server. This guarantees that all scientific data, images, and metadata collected by the HABCAM are precisely time-stamped and synchronized to a single, highly accurate master clock.</li>
  <li><b>Integrate Shipboard Navigation Systems:</b> Establish stable, reliable connections between the HABCAM system and the vessel's primary navigation instruments, specifically the ship's GPS and fathometer (depth sounder). This integration is crucial for accurate geographical and depth referencing of all collected imagery.</li>
  <li><b>Maintain Server Operations:</b> Verify that all essential server infrastructure is fully operational at all times. This requires routinely checking that all necessary storage drives are correctly mounted and ensuring the Apache web server is running smoothly to host and distribute data to the science team without interruption.</li>
  <li><b>Monitor Raw Data Acquisition:</b> Monitor the data pipeline to confirm that all raw imagery and sensor telemetry captured by the HABCAM are being successfully and continuously written to the primary storage servers, preventing any loss of data.</li>
  <li><b>Build and Optimize Light Maps:</b> Generate and implement accurate light maps for the underwater camera systems. This calibration process corrects for uneven illumination caused by the strobes, ensuring consistent exposure and quality, evenly lit visuals for accurate scientific analysis and annotation.</li>
  <li><b>Oversee Image Processing Workflow:</b> Supervise the real time image processing. You must verify that incoming raw images are being correctly processed, formatted, and reliably served to the annotation machines so that the scientific team can seamlessly identify and log marine life and habitats.</li>
  <li><b>Perform Quality Assurance on Metadata:</b> Conduct quality control checks within the PostgreSQL database. This involves regularly verifying the accuracy, completeness, and integrity of all metadata (e.g., timestamps, location coordinates, altitude, depth) associated with the HABCAM imagery to ensure the final dataset is scientifically valid.</li>
  <li><b>Execute Continuous Data Backups:</b> Implement and oversee a data redundancy protocol. You are responsible for continuously backing up all raw data, processed images, and database records onto spare, secure drives to safeguard against hardware failure, data corruption, or loss during the survey.</li>
  <li><b>Conduct Pre-Deployment Vehicle Checks and Troubleshooting:</b> Lead the pre-dive inspection of the physical HABCAM vehicle. You must test all mechanical and electronic systems on deck, quickly identify potential faults, and troubleshoot any electrical or software issues before deployment to ensure a safe, successful, and uninterrupted dive.</li>
</ul>

<br>

<h3 id="spec-watch-chief" style="color: #2e7d32;">WATCH CHIEF</h3>

<p>As a Watch Chief, you are the direct shift supervisor responsible for managing the personnel, operations, and data collection during your assigned rotation. You ensure that the scientific objectives set by the Chief Scientist are executed safely and efficiently while maintaining the standards required for accurate data logging.</p>

<p>Your responsibilities include:</p>

<ul style="text-align: left;">
  <li><b>Manage 12-Hour Operational Shifts:</b> As one of exactly two Watch Chiefs assigned to the cruise, you are responsible for commanding a continuous 12-hour shift. You must maintain operational efficiency during your watch and ensure a seamless, detailed handover of information and system status to your counterpart during shift changes.</li>
  <li><b>Assign and Manage Rotating Station Roles:</b> Orchestrate the team's workflow to maximize focus and prevent fatigue. You will create and enforce a schedule, rotating your assigned scientific personnel through the active stations (Pilot, co-pilot, and image annotator). You are also responsible for verifying that all team members are present, rested, and prepared for their assigned blocks.</li>
  <li><b>Control Core Operational Software:</b> Serve as the gatekeeper for the vehicle's flight systems. You hold the direct responsibility for properly and securely starting up, monitoring, and shutting down the specialized pilot and co-pilot software systems used to fly and monitor the HABCAM, ensuring all programs are stable and communicating correctly with the hardware.</li>
  <li><b>Train and Onboard New Scientists:</b> Act as the primary shift educator. You will conduct comprehensive training sessions for new or inexperienced scientists using standardized materials, such as the annotation PowerPoint. You must ensure they thoroughly understand the established protocols for identifying marine life, geological features, and logging accurate metadata.</li>
  <li><b>Actively Participate in the Operational Cycle:</b> Lead by example. Rather than solely acting in a supervisory capacity, you are expected to fully integrate into the active rotation schedule. You will regularly take your turn at the pilot, co-pilot, and annotator stations, bearing a portion of the continuous operational workload alongside your team.</li>
  <li><b>Perform Quality Assurance and Quality Control (QA/QC):</b> Safeguard the integrity of the scientific data. You will actively review the biological and habitat annotations logged by your team members during the shift. This involves cross checking complex species identifications, identifying and correcting entry errors, and ensuring that the data collected under your watch meets the survey's scientific standards.</li>
</ul>

<br>

<h3 id="spec-pilot" style="color: #2e7d32;">PILOT</h3>

<p>You are directly responsible for the safe, precise, and active underwater navigation of the HABCAM vehicle. Because this role requires intense concentration and quick reflexes to protect scientific equipment, you operate in short, focused intervals.</p>

<p>Your responsibilities include:</p>

<ul style="text-align: left;">
  <li><b>Execute Rotational Shifts (30 to 60 Minutes):</b> Maintain concentration and prevent operational fatigue. Because flying the vehicle requires uninterrupted attention, you will rotate into the pilot's seat for strictly timed blocks of 30 minutes to one hour. This rotation ensures your reflexes and situational awareness remain sharp during your entire time at the helm.</li>
  <li><b>Maintain Safe Altitude Over the Seafloor:</b> Safeguard the physical integrity of the HABCAM vehicle. Your primary, overriding objective is to "fly" the vehicle at the optimal target altitude for photography (typically just a few meters above the bottom). You must constantly adjust to sudden changes in bathymetry to prevent catastrophic impacts with the seabed or entanglement in benthic structures.</li>
  <li><b>Operate the Ship's Winch System via Joystick:</b> Manually control the vertical movement of the towed vehicle. Utilizing a specialized joystick interface, you will directly command the heavy machinery of the ship's winch. You must actively pay out or haul in the tow cable, making precise, real time micro-adjustments to the HABCAM's depth as the vessel moves forward through the water column.</li>
  <li><b>Monitor Live Camera Feeds and Flight Telemetry (GUI):</b> Maintain constant visual and data awareness. You must continuously process multiple streams of information simultaneously, keeping your eyes locked on both the real time, downward-facing video feed from the HABCAM and the graphical user interface (GUI) of the winch flight software. This allows you to react to both visual terrain cues and telemetry data, such as cable tension, vehicle pitch, and exact depth.</li>
  <li><b>Scan Forward-Looking Sonar for Obstacle Avoidance:</b> Anticipate and evade underwater hazards before they become a threat. Because visibility is limited underwater, you will continuously read and interpret the forward-looking sonar display to detect upcoming obstacles. Such as steep drop-offs, large boulders, shipwrecks, or abandoned fishing gear; well before they enter the camera's field of view, allowing you to proactively haul in the winch and avoid a collision.</li>
</ul>

<br>

<h3 id="spec-copilot" style="color: #2e7d32;">CO-PILOT</h3>

<p>As the Co-Pilot, you act as the essential second pair of eyes and primary technical support for the active Pilot. While the Pilot focuses entirely on the physical maneuvering of the vehicle, you are responsible for comprehensive situational awareness, system optimization, and hazard detection to ensure both the safety of the HABCAM and the quality of the scientific data.</p>

<p>Your responsibilities include:</p>

<ul style="text-align: left;">
  <li><b>Execute Rotational Shifts (30 to 60 Minutes):</b> Maintain vigilance as part of a synchronized team. Just like the Pilot, you will rotate into the Co-Pilot station for short, focused intervals of 30 minutes to one hour. This frequent rotation prevents screen fatigue and ensures you remain sharply attuned to subtle changes in sensor data and visual feeds.</li>
  <li><b>Monitor Dual Camera Feeds and Sensor Telemetry:</b> Oversee the vehicle's diagnostic health. You are tasked with continuously watching the live video streams from multiple cameras to ensure clear visibility and proper illumination. Simultaneously, you must verify that all onboard environmental sensors (such as temperature, depth, and altimeters) are actively logging and transmitting accurate, uninterrupted data back to the ship.</li>
  <li><b>Analyze Sonar for Obstacles and Topographical Shifts:</b> Serve as the early warning system for navigational hazards. You will actively interpret the sonar displays to map out the terrain ahead. This includes not only spotting immediate, dangerous obstacles (like boulders or wrecks) but also identifying complex seafloor topography, such as rolling sand waves, which require the Pilot to make continuous, rhythmic depth adjustments.</li>
  <li><b>Communicate Critical Concerns to the Pilot:</b> Facilitate seamless, high-stress teamwork. You must maintain clear, constant, and concise verbal communication with the Pilot. If you detect an upcoming obstacle on the sonar or notice a sudden drop in sensor performance, you are responsible for immediately alerting the Pilot so they have the maximum possible time to react and adjust the winch.</li>
  <li><b>Optimize Hardware and Software Settings in Real-Time:</b> Manage the configuration of the HABCAM's instruments. As environmental conditions change, you will actively fine tune the system's parameters. This includes adjusting sonar ranges for better resolution, modifying camera frame rates to match the vehicle's speed and altitude, and tweaking settings within the winch flight software to ensure smooth data capture.</li>
  <li><b>Troubleshoot and Mitigate Station Software Issues:</b> Act as the immediate first line of defense for control station stability. If the pilot/co-pilot software freezes, an application crashes, or a localized networking glitch occurs, you must diagnose and resolve the issue on the fly. Your mitigation prevents operational downtime and ensures the Pilot does not lose control or visibility of the vehicle.</li>
</ul>

<br>

<h3 id="spec-annotator" style="color: #2e7d32;">ANNOTATOR</h3>

<p>As an Annotator, you are the frontline data processor of the scientific survey. Your primary responsibility is to translate the raw visual imagery captured by the underwater HABCAM into quantifiable, actionable scientific records. Because this requires sharp visual acuity and rapid decision making, you operate within a fast paced, collaborative workflow.</p>

<p>Your responsibilities include:</p>

<ul style="text-align: left;">
  <li><b>Execute Rotational Shifts (30 to 60 Minutes):</b> Maintain visual sharpness and combat screen fatigue. Accurately identifying camouflaged marine life and complex benthic habitats requires continuous concentration. To ensure the highest data quality, you will rotate through the annotation station in 30- to 60-minute intervals. You will frequently work concurrently alongside several other annotators to divide the workload and maintain a steady processing speed.</li>
  <li><b>Process Primary and Secondary Image Assignments:</b> Analyze a rapid, continuous stream of visual data. You are tasked with reviewing batches of newly captured seafloor images, which are automatically pushed to your workstation every 10 minutes. You must swiftly and accurately log specific targets according to your assigned priorities; this typically involves identifying and counting primary species of interest (such as specific fish or scallops) while also recording secondary environmental details, like substrate types and other invertebrate life.</li>
  <li><b>Complete Mandatory Identification and Protocol Training:</b> Guarantee standardized data collection and scientific validity. Before taking on active shifts, you must complete a specialized training program, conducted either prior to departure or while the vessel is under sail to the survey site. This essential onboarding ensures your identification skills are calibrated with the rest of the scientific party, and that you are fully proficient in utilizing the survey's specific annotation software and classification guidelines.</li>
</ul>

<br>

<h3 id="spec-qaqc-lead" style="color: #2e7d32;">QA/QC LEAD</h3>

<p>As the QA/QC lead, you are the primary guardian of data integrity for the survey. Your main objective is to ensure that all visual data processed by the scientific team is highly accurate, consistent, and scientifically sound. You act as both an educator and auditor for the annotation team.</p>

<p>Your responsibilities include:</p>

<ul style="text-align: left;">
  <li><b>Host the Comprehensive Pre-Cruise Training Overview:</b> Organize and lead the foundational orientation for the scientific party. Before the vessel departs or active data collection begins, you will host a mandatory, large-scale training session. This overview sets the baseline expectations for data quality, distributes visual reference guides, and aligns the entire team on the specific biological and ecological targets of the upcoming survey.</li>
  <li><b>Train Annotators on Standardized Protocols:</b> Serve as the primary, ongoing educator for the data processing team. You are responsible for thoroughly instructing all annotators on the exact, standardized protocols required for the mission. This includes teaching precise species identification criteria, benthic habitat classification, and the correct, efficient operation of the customized annotation software to ensure absolute consistency across all shifts.</li>
  <li><b>Audit and Confirm Baseline Annotation Accuracy:</b> Conduct targeted quality control checks on individual performance. For every annotator on the team, you will review, grade, and verify a sample set of approximately 30 assigned images. This initial audit allows you to catch individual misidentifications early, provide constructive, one-on-one feedback, and officially certify that each annotator is fully calibrated and ready to process large volumes of data independently.</li>
</ul>

<br>

<h3 id="spec-population-dynamics" style="color: #2e7d32;">POPULATION DYNAMICS</h3>

<p>As the Population Dynamics specialist, you are the lead quantitative scientist for the survey. Your primary role is to ensure that the data collected is statistically robust and biologically meaningful for stock assessments and ecological modeling. You bridge the gap between active field operations and high level data analysis.</p>

<p>Your responsibilities include:</p>

<ul style="text-align: left;">
  <li><b>Assist in Strategic Trackline Planning and Dynamic Routing:</b> Collaborate directly with the Chief Scientist to design mathematically sound survey routes. You provide input based on statistical requirements, historical population distributions, and depth stratifications. During the cruise, you actively participate in real-time decision-making, recalculating and updating tracklines on the fly when the team faces severe weather, time constraints, or unexpected biological discoveries.</li>
  <li><b>Actively Participate in the Operational Cycle:</b> Maintain a hands-on connection to the raw data collection process. Rather than solely working on backend analysis, you are expected to fully integrate into the rotating shift schedule. You will take regular turns functioning as a HABCAM Pilot, Co-Pilot, and Annotator alongside the rest of the scientific party, ensuring you intimately understand the operational conditions and visual complexities of the data you will later analyze.</li>
  <li><b>Execute System Calibrations and Altimeter Verification:</b> Guarantee the spatial accuracy of the survey's visual data. You will oversee camera calibration procedures and analyze the resulting calibration annotation data. You must calculate the statistical confidence of the altimeter's positioning to ensure that the exact scale of the images is known, which allows for precise measurements of organism density and total seafloor area swept. You will leverage these metrics to continually assist cruise planners in developing efficient tracklines for each leg of the journey.</li>
  <li><b>Analyze Data, Identify Gaps, and Synthesize Results:</b> Serve as the central hub for data synthesis. You are responsible for aggregating and mathematically analyzing the massive volume of biological and habitat annotations generated by the shift teams. This requires meticulously auditing the dataset to identify any spatial or temporal gaps in coverage, summarizing population trends, and formally presenting these preliminary statistical results to leadership for ongoing survey adjustments and future stock assessments.</li>
</ul>

<br>

</div>

<h2 id="habcam-pre-deployment">7. HabCam Pre-Deployment Procedures</h2>

<div align="left" style="text-align: left !important;">

<p>Complete the following procedural checklist prior to deploying the HabCam vehicle into the water:</p>

<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> <b>Vehicle Checklist:</b> Complete the Pre-Deployment Vehicle Checklist.
    <br><i>[Fill out details for pre-deployment vehicle checklist procedures here]</i>
  </li>
  <li><input type="checkbox"> <b>Power Inverter Activation:</b> Power up the vehicle via the power inverter located at the Watch Chief Station.
    <ul style="list-style-type: none; padding-left: 20px;">
      <li><input type="checkbox"> Flip the <b>Right switch</b> first, then flip the <b>Left switch</b>[cite: 6].</li>
    </ul>
  </li>
  <li><input type="checkbox"> <b>Image Viewer Configuration:</b> Open two image viewers, minimize one, and drag it over to the Pilot Station display:
    <ul style="list-style-type: none; padding-left: 20px;">
      <li><input type="checkbox"> Adjust frame rate to <b>6.00 Hz</b>.</li>
      <li><input type="checkbox"> Set gain to <i>[Fill out details for gain setting]</i>.</li>
    </ul>
  </li>
  <li><input type="checkbox"> <b>Stereo Acquisition Launch:</b> Click stereo acquisition to start real-time image processing.
    <ul style="list-style-type: none; padding-left: 20px;">
      <li><input type="checkbox"> Verify that a small black terminal window opens on the Co-Pilot's left monitor displaying the live data feed.</li>
      <li><input type="checkbox"> <i>Troubleshooting:</i> If the image viewer freezes, verify `runVimCam` status or click <b>Stereo Acquisition</b> to relaunch.</li>
    </ul>
  </li>
</ul>

<br>

<p><i>[Fill out details for additional pre-deployment checks, sensor verifications, and deck communications here]</i></p>

</div>

<h2 id="after-cruise-checklist">8. After-Cruise Checklist</h2>

<div align="left" style="text-align: left !important;">

<h3 id="sec-destaging-day" style="color: #2e7d32;">Day of Destaging</h3>

<br>

<h4 id="sec-destage-data-backup">Data Backup</h4>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Verify with the HabCam lead that HabCam survey data is backed up</li>
  <li><input type="checkbox"> Ensure the ship data is copied onto a USB drive and given to Chief Scientist
    <ul style="list-style-type: none; padding-left: 20px;">
      <li><input type="checkbox"> Copy to <code>FSCS_RAWDATA</code>, following completion of the cruise.</li>
    </ul>
  </li>
  <li><input type="checkbox"> If CTDs were performed, the crew will provide the CTD Logs for Oceanography.</li>
  <li><input type="checkbox"> Make sure all special requests samples are taken off the ship at the completion of the cruise, coordinate pick-up of samples from researchers (this may be done pre-cruise; check with Advanced Tech lead or previous leg’s CS).</li>
</ul>

<br>
<p><i>[Insert details on data offload verification, server network paths, external drive formatting protocols, and photos of backup storage setups here]</i></p>
<br>

<h4 id="sec-destage-habcam">HabCam Vehicle Teardown</h4>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Cut tow cable one foot before termination (prior to black boot)</li>
  <li><input type="checkbox"> Drain junction box</li>
  <li><input type="checkbox"> Rinse down HabCam with freshwater</li>
  <li><input type="checkbox"> Detach tail piece while HabCam is still on the vessel.</li>
  <li><input type="checkbox"> Detach clevis [Will need to be taken to Reidar’s Manufacturing in New Bedford to break down the socket lock]</li>
  <li><input type="checkbox"> Disconnect and take the power converter.</li>
</ul>

<br>
<p><i>[Insert details on freshwater washdown procedures, junction box oil draining, clevis transport logistics to Reidar's, and photos of vehicle disassembly here]</i></p>
<br>

<h4 id="sec-destage-workstations">Workstations Breakdown</h4>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Break down monitors and put in tote bags
    <ul style="list-style-type: none; padding-left: 20px;">
      <li><input type="checkbox"> Put cables in designated boxes</li>
    </ul>
  </li>
  <li><input type="checkbox"> Break down the server.</li>
  <li><input type="checkbox"> Place computers into designated pelican cases.</li>
  <li><input type="checkbox"> Disconnect GPS puck from flying bridge.</li>
  <li><input type="checkbox"> Place ethernet cables into Ethernet tote.</li>
  <li><input type="checkbox"> Remove and consolidate plywood.</li>
</ul>

<br>
<p><i>[Insert details on server rack dismounting, cable packing inventories, flying bridge access procedures, and photos of packed Pelican cases/totes here]</i></p>
<br>

<h4 id="sec-destage-foul-weather-gear">Foul Weather Gear</h4>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Place NMFS labeled gear back into mesh bags</li>
  <li><input type="checkbox"> Place PFD’s into a long black tote.</li>
</ul>

<br>
<p><i>[Insert details on gear laundering, safety inspection, drying guidelines, and photos of storage totes here]</i></p>
<br>

<h4 id="sec-destage-transportation">Transportation & Logistics</h4>
<ul style="list-style-type: none; padding-left: 0; margin-left: 0; text-align: left;">
  <li><input type="checkbox"> Ensure everyone (including volunteers and Teachers at-Sea) have proper travel arrangements following completion of cruise.</li>
  <li><input type="checkbox"> If needed, work with onshore support staff/branch chief to ensure a vehicle is available for a provision run in between cruise legs.</li>
  <li><input type="checkbox"> Divide vans for what is going to Woods Hole (keep WHOI and NMFS stuff separate) and what is going to Netloft</li>
</ul>

<br>
<p><i>[Insert details on shoreside transport routes, Woods Hole vs. Netloft unloading schedules, equipment segregation rules, and photos of van staging here]</i></p>

<br>

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
