<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Marine Development & Advanced Technology | NOAA Fisheries</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap" rel="stylesheet">
  
  <style>
    /* Official NOAA Color Palette & Styling */
    :root {
      --noaa-navy: #002b49;
      --noaa-blue: #005886;
      --noaa-light-blue: #0085ca;
      --noaa-teal: #00a3e0;
      --noaa-dark-text: #222222;
      --noaa-bg-light: #f4f6f8;
      --noaa-border: #d0d7de;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif; color: var(--noaa-dark-text); background-color: #ffffff; line-height: 1.6; }
    .container { max-width: 1180px; margin: 0 auto; padding: 0 20px; }

    /* USA Government Top Bar */
    .usa-banner { background-color: #f0f0f0; border-bottom: 1px solid var(--noaa-border); font-size: 0.75rem; padding: 4px 20px; color: #444; }
    .usa-banner-container { max-width: 1180px; margin: 0 auto; display: flex; align-items: center; gap: 10px; }
    .usa-banner-tech { margin-left: auto; font-weight: 600; color: var(--noaa-blue); }

    /* Header */
    .noaa-header { background-color: var(--noaa-navy); color: #ffffff; padding: 16px 0; }
    .header-container { max-width: 1180px; margin: 0 auto; padding: 0 20px; display: flex; justify-content: space-between; align-items: center; }
    .brand-group { display: flex; align-items: center; gap: 15px; }
    .noaa-emblem { width: 50px; height: 50px; }
    .agency-title { display: block; font-size: 1.3rem; font-weight: 800; letter-spacing: 0.5px; }
    .office-title { display: block; font-size: 0.85rem; color: #cce7f0; }

    /* Search Bar */
    .header-search { display: flex; }
    .header-search input { padding: 8px 12px; border: none; border-radius: 4px 0 0 4px; width: 220px; }
    .header-search button { background-color: var(--noaa-light-blue); color: white; border: none; padding: 8px 16px; border-radius: 0 4px 4px 0; cursor: pointer; font-weight: 600; }

    /* Navigation */
    .noaa-nav { background-color: var(--noaa-blue); border-bottom: 3px solid var(--noaa-teal); }
    .nav-container { max-width: 1180px; margin: 0 auto; padding: 0 20px; }
    .noaa-nav ul { display: flex; list-style: none; }
    .noaa-nav a { color: #ffffff; text-decoration: none; padding: 12px 18px; display: block; font-weight: 600; font-size: 0.95rem; }
    .noaa-nav a:hover { background-color: rgba(255, 255, 255, 0.15); }

    /* Breadcrumbs */
    .breadcrumb-bar { background-color: var(--noaa-bg-light); padding: 10px 0; border-bottom: 1px solid var(--noaa-border); font-size: 0.85rem; }
    .breadcrumbs { display: flex; list-style: none; gap: 8px; color: #555; }
    .breadcrumbs li::after { content: "/"; margin-left: 8px; color: #999; }
    .breadcrumbs li:last-child::after { content: ""; }
    .breadcrumbs a { color: var(--noaa-blue); text-decoration: none; }

    /* Hero Section */
    .hero-header { padding: 35px 0 25px; border-bottom: 1px solid var(--noaa-border); }
    .noaa-tag { background-color: var(--noaa-navy); color: #ffffff; font-size: 0.75rem; font-weight: 700; padding: 3px 8px; border-radius: 3px; margin-right: 6px; }
    .tag-secondary { background-color: var(--noaa-light-blue); }
    .hero-header h1 { font-size: 2.2rem; color: var(--noaa-navy); margin: 12px 0; }
    .hero-lead { font-size: 1.1rem; color: #444; max-width: 900px; }

    /* Layout Grid */
    .main-content { padding: 35px 0; }
    .layout-grid { display: grid; grid-template-columns: 2.7fr 1fr; gap: 40px; }
    .content-block { margin-bottom: 40px; }
    .section-title { font-size: 1.5rem; color: var(--noaa-navy); border-bottom: 2px solid var(--noaa-blue); padding-bottom: 6px; margin-bottom: 20px; }

    /* Callout & Cards */
    .mission-box { background-color: #f0f7fc; border-left: 4px solid var(--noaa-light-blue); padding: 18px 20px; margin-bottom: 20px; }
    .mission-box h3 { color: var(--noaa-navy); font-size: 1.1rem; margin-bottom: 6px; }

    .framework-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-top: 15px; }
    .step-card { background: var(--noaa-bg-light); border: 1px solid var(--noaa-border); border-radius: 4px; padding: 14px; }
    .step-num { background: var(--noaa-blue); color: white; width: 22px; height: 22px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: bold; margin-bottom: 6px; }
    .step-card h4 { font-size: 0.9rem; color: var(--noaa-navy); margin-bottom: 4px; }
    .step-card p { font-size: 0.82rem; color: #555; }

    /* Tech Cards */
    .tech-feature { border: 1px solid var(--noaa-border); border-radius: 4px; margin-bottom: 20px; }
    .tech-header { background-color: var(--noaa-bg-light); padding: 12px 18px; border-bottom: 1px solid var(--noaa-border); }
    .tech-type { font-size: 0.7rem; font-weight: 800; color: var(--noaa-light-blue); letter-spacing: 0.5px; }
    .tech-header h3 { font-size: 1.15rem; color: var(--noaa-navy); }
    .tech-body { padding: 18px; }
    .tech-body ul { padding-left: 20px; margin-top: 10px; }
    .tech-body li { margin-bottom: 6px; font-size: 0.92rem; }

    /* Accordion */
    .accordion-item { border: 1px solid var(--noaa-border); margin-bottom: 10px; border-radius: 4px; }
    .accordion-header { padding: 12px 18px; background-color: var(--noaa-bg-light); font-weight: 700; cursor: pointer; display: flex; justify-content: space-between; align-items: center; color: var(--noaa-navy); }
    .accordion-content { padding: 18px; display: none; border-top: 1px solid var(--noaa-border); background: white; }
    .accordion-item.active .accordion-content { display: block; }

    /* Sidebar */
    .sidebar-card { border: 1px solid var(--noaa-border); border-radius: 4px; padding: 18px; margin-bottom: 20px; background-color: #ffffff; }
    .highlight-card { background-color: var(--noaa-bg-light); border-top: 3px solid var(--noaa-blue); }
    .sidebar-card h3 { font-size: 1.05rem; color: var(--noaa-navy); margin-bottom: 10px; border-bottom: 1px solid var(--noaa-border); padding-bottom: 6px; }
    .sidebar-list { list-style: none; font-size: 0.88rem; }
    .sidebar-list li { margin-bottom: 8px; }

    /* Footer */
    .noaa-footer { background-color: var(--noaa-navy); color: white; margin-top: 40px; padding: 30px 0 15px; }
    .footer-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-bottom: 20px; }
    .footer-top h4 { margin-bottom: 10px; color: var(--noaa-teal); }
    .footer-top ul { list-style: none; }
    .footer-top a { color: #ccc; text-decoration: none; font-size: 0.85rem; display: block; margin-bottom: 5px; }
    .footer-bottom { text-align: center; font-size: 0.8rem; color: #aaa; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 15px; }

    @media (max-width: 850px) {
      .layout-grid { grid-template-columns: 1fr; }
      .header-container { flex-direction: column; gap: 15px; align-items: flex-start; }
    }
  </style>
</head>
<body>

  <!-- Government Top Banner -->
  <div class="usa-banner">
    <div class="usa-banner-container">
      <span>🇺🇸 An official website of the United States government</span>
      <span class="usa-banner-tech">NOAA Fisheries Program Portal</span>
    </div>
  </div>

  <!-- Main NOAA Header -->
  <header class="noaa-header">
    <div class="header-container">
      <div class="brand-group">
        <div class="noaa-emblem">
          <svg viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="48" fill="#003366" stroke="#ffffff" stroke-width="2"/>
            <path d="M20 55 C 35 40, 65 40, 80 55 C 65 70, 35 70, 20 55 Z" fill="#00a3e0" opacity="0.6"/>
            <path d="M15 65 Q 50 85 85 65 Q 50 95 15 65 Z" fill="#ffffff"/>
            <text x="50" y="32" font-family="sans-serif" font-weight="bold" font-size="12" fill="#ffffff" text-anchor="middle">NOAA</text>
            <text x="50" y="44" font-family="sans-serif" font-size="7" fill="#88d8c0" text-anchor="middle">FISHERIES</text>
          </svg>
        </div>
        <div class="brand-text">
          <span class="agency-title">NOAA FISHERIES</span>
          <span class="office-title">Northeast Fisheries Science Center</span>
        </div>
      </div>

      <div class="header-search">
        <input type="text" placeholder="Search NOAA Fisheries..." aria-label="Search" />
        <button type="button">Search</button>
      </div>
    </div>
  </header>

  <!-- Navigation -->
  <nav class="noaa-nav">
    <div class="nav-container">
      <ul>
        <li><a href="#mission">Mission & Strategy</a></li>
        <li><a href="#initiatives">Tech Initiatives</a></li>
        <li><a href="#admin">Admin & Future Directions</a></li>
      </ul>
    </div>
  </nav>

  <!-- Breadcrumb -->
  <div class="breadcrumb-bar">
    <div class="container">
      <ul class="breadcrumbs">
        <li><a href="#">Home</a></li>
        <li><a href="#">Science & Data</a></li>
        <li>Marine Development & Advanced Technology</li>
      </ul>
    </div>
  </div>

  <!-- Page Title / Hero -->
  <header class="hero-header">
    <div class="container">
      <div>
        <span class="noaa-tag">PROGRAM OVERVIEW</span>
        <span class="noaa-tag tag-secondary">OFFSHORE WIND & TECH</span>
      </div>
      <h1>Marine Development & Advanced Technology</h1>
      <p class="hero-lead">
        Developing surveys, advanced technologies, and analytical approaches to inform stock and ecosystem assessments.
      </p>
    </div>
  </header>

  <main class="main-content">
    <div class="container layout-grid">
      
      <!-- Left Content Column -->
      <div class="primary-column">
        
        <!-- SECTION 1: Core Mission & Strategy -->
        <section id="mission" class="content-block">
          <h2 class="section-title">Core Mission & Strategy</h2>
          
          <div class="mission-box">
            <h3>Mission</h3>
            <p>Develop surveys, advanced technologies, and analytical approaches to inform stock and ecosystem assessments.</p>
          </div>

          <h3 style="margin-bottom: 8px;">Interactions with Offshore Wind</h3>
          <p style="margin-bottom: 20px;">
            Offshore wind energy developments impact at least <strong>14 long-term scientific surveys</strong> in the U.S. Northeast region (e.g., bottom trawl, scallop, ecosystem monitoring) through preclusion, habitat change, and survey design disruptions.
          </p>

          <h3 style="margin-bottom: 10px;">6-Step Survey Mitigation Framework</h3>
          <div class="framework-grid">
            <div class="step-card">
              <span class="step-num">1</span>
              <h4>Evaluate Impacts</h4>
              <p>Assess spatial & statistical survey disruptions.</p>
            </div>
            <div class="step-card">
              <span class="step-num">2</span>
              <h4>Design Methods</h4>
              <p>Engineer new survey techniques for wind areas.</p>
            </div>
            <div class="step-card">
              <span class="step-num">3</span>
              <h4>Calibrate Surveys</h4>
              <p>Ensure data continuity between old and new methods.</p>
            </div>
            <div class="step-card">
              <span class="step-num">4</span>
              <h4>Bridge Solutions</h4>
              <p>Fill temporal sampling gaps during construction.</p>
            </div>
            <div class="step-card">
              <span class="step-num">5</span>
              <h4>Conduct Surveys</h4>
              <p>Execute long-term uncrewed and acoustic monitoring.</p>
            </div>
            <div class="step-card">
              <span class="step-num">6</span>
              <h4>Communicate Data</h4>
              <p>Share results with fishery managers and stakeholders.</p>
            </div>
          </div>
        </section>

        <!-- SECTION 2: Key Technological Initiatives -->
        <section id="initiatives" class="content-block">
          <h2 class="section-title">Key Technological Initiatives</h2>

          <!-- Initiative 1 -->
          <article class="tech-feature">
            <div class="tech-header">
              <span class="tech-type">AUTONOMOUS UNDERWATER VEHICLES</span>
              <h3>1. Long-Range AUV (LRAUV) Development</h3>
            </div>
            <div class="tech-body">
              <p><strong>Platform & Payload:</strong> Developed in collaboration with MBARI and WHOI, incorporating dual stereo camera payloads to mimic the Habitat Camera (HabCam) setup.</p>
              <ul>
                <li><strong>Objectives:</strong> Access wind farm lease areas and reduce total days at sea required for HabCam survey coverage.</li>
                <li><strong>2024 Deployments:</strong> Sampled over 200 nautical miles in May and June 2024. Calibrations with dredge and HabCam V4 showed no significant bias in scallop shell height measurements.</li>
                <li><strong>Nearshore & Offshore Operations:</strong> Successfully tested operating from small vessels nearshore (e.g., South Fork Wind Farm in November 2024).</li>
              </ul>
            </div>
          </article>

          <!-- Initiative 2 -->
          <article class="tech-feature">
            <div class="tech-header">
              <span class="tech-type">UNCREWED SURFACE VEHICLES</span>
              <h3>2. Uncrewed Surface Vehicles (USV - DriX)</h3>
            </div>
            <div class="tech-body">
              <p><strong>Operational Value:</strong> Designed to sample close (20–30 meters) to wind turbine structures, operate 24/7 safely, and maneuver efficiently around complex installations.</p>
              <ul>
                <li><strong>Missions:</strong> Conducted a 20-day survey covering three offshore wind areas (including Block Island, Cox Ledge, and Vineyard Wind) in late 2023. Continued sampling scheduled focusing on North Atlantic right whale forage habitat questions.</li>
              </ul>
            </div>
          </article>

          <!-- Initiative 3 (NEWLY ADDED) -->
          <article class="tech-feature">
            <div class="tech-header">
              <span class="tech-type">UNDERWATER IMAGING SYSTEMS</span>
              <h3>3. Habitat Camera (HabCam) Survey</h3>
            </div>
            <div class="tech-body">
              <p>The <strong>HABitat CAMera system (HABCAM)</strong> is a non-invasive, underwater imaging vehicle towed from the stern of research vessels approximately 2 meters above the seafloor, capturing high-resolution, overlapping stereo images.</p>
              <p style="margin-top: 10px;">The camera array is additionally equipped with a compass, CTD, sonar, and sensors that survey the seafloor, which can be used for estimates of species abundance, habitat characterization, and biodiversity—giving a holistic view of benthic taxa. This vehicle has been used extensively for surveying the sea scallop resource on Georges Bank and the Mid-Atlantic Bight, as well as collecting data on finfish and habitat.</p>
            </div>
          </article>

          <!-- Initiative 4 -->
          <article class="tech-feature">
            <div class="tech-header">
              <span class="tech-type">AI & OPTICAL ENHANCEMENTS</span>
              <h3>4. Machine Learning & Ocean Chemistry Enhancements</h3>
            </div>
            <div class="tech-body">
              <p><strong>Automated Processing:</strong> Developing machine learning tools (e.g., VIAME software) under the NOAA Inflation Reduction Act (IRA) Optical Strategic Initiative to automate scallop identification and measurements, replacing manual annotation.</p>
              <p style="margin-top: 10px;"><strong>Ocean Acidification Monitoring:</strong> Integrated a channelized optical system into HabCam in 2024 to measure bottom water dissolved inorganic carbon (DIC) and pCO<sub>2</sub>, pairing scallop biomass with ocean chemistry data.</p>
            </div>
          </article>

          <!-- Initiative 5 -->
          <article class="tech-feature">
            <div class="tech-header">
              <span class="tech-type">ACOUSTICS & COOPERATIVE RESEARCH</span>
              <h3>5. Active Acoustics & Cooperative Research</h3>
            </div>
            <div class="tech-body">
              <p><strong>Long-Term Data:</strong> Active acoustic data collected continuously since 1998 across multiple frequency bands (18, 38, 120 kHz).</p>
              <p style="margin-top: 10px;"><strong>Industry Collaboration:</strong> Partnering with commercial fishing vessels to evaluate catchability, study fish life history, and develop acoustic survey methods for species like Atlantic mackerel.</p>
            </div>
          </article>
        </section>

        <!-- SECTION 3: Administrative & Future Directions -->
        <section id="admin" class="content-block">
          <h2 class="section-title">Administrative & Future Directions</h2>

          <div class="accordion-item">
            <div class="accordion-header" onclick="toggleAcc(this)">
              <span>Proposals & Funding</span>
              <span class="icon">+</span>
            </div>
            <div class="accordion-content">
              <p>Submitted 7 proposals since May 2024 across VIAME machine learning, mackerel acoustics, oceanographic USV sampling, and AUV-ABIS development.</p>
            </div>
          </div>

          <div class="accordion-item">
            <div class="accordion-header" onclick="toggleAcc(this)">
              <span>Staffing Updates</span>
              <span class="icon">+</span>
            </div>
            <div class="accordion-content">
              <p>Hiring underway for a HabCam Scientist, Biological Science Technician, and Electronics Engineers.</p>
            </div>
          </div>

          <div class="accordion-item">
            <div class="accordion-header" onclick="toggleAcc(this)">
              <span>Future Work & Priorities</span>
              <span class="icon">+</span>
            </div>
            <div class="accordion-content">
              <ul>
                <li>Passive acoustics for groundfish (e.g., Atlantic cod, haddock).</li>
                <li>Expanding AUV optical applications to complementary technologies like eDNA.</li>
                <li>Model-based integration of traditional and advanced technology survey data.</li>
                <li>Directed catchability and mitigation studies for marine energy development.</li>
              </ul>
            </div>
          </div>
        </section>

      </div>

      <!-- Right Sidebar Column -->
      <aside class="sidebar-column">
        <div class="sidebar-card highlight-card">
          <h3>Quick Overview</h3>
          <ul class="sidebar-list">
            <li><strong>Impacted Surveys:</strong> 14+ Northeast Studies</li>
            <li><strong>Key Equipment:</strong> HabCam V4, LRAUV, DriX USV</li>
            <li><strong>Funding Source:</strong> NOAA IRA Optical Initiative</li>
            <li><strong>Partners:</strong> MBARI, WHOI, Commercial Fleets</li>
          </ul>
        </div>

        <div class="sidebar-card">
          <h3>Related Links</h3>
          <ul class="sidebar-list">
            <li><a href="#" style="color: var(--noaa-blue); text-decoration:none;">Northeast Fisheries Science Center</a></li>
            <li><a href="#" style="color: var(--noaa-blue); text-decoration:none;">Offshore Wind Energy Impact Studies</a></li>
            <li><a href="#" style="color: var(--noaa-blue); text-decoration:none;">HabCam Towed & AUV Systems</a></li>
          </ul>
        </div>
      </aside>

    </div>
  </main>

  <!-- NOAA Footer -->
  <footer class="noaa-footer">
    <div class="container footer-grid">
      <div>
        <h4>NOAA Fisheries</h4>
        <p style="font-size: 0.85rem; color: #ccc;">National Oceanic and Atmospheric Administration<br>U.S. Department of Commerce</p>
      </div>
      <div>
        <h4>Compliance & Policy</h4>
        <ul>
          <li><a href="#">Accessibility</a></li>
          <li><a href="#">FOIA Information</a></li>
          <li><a href="#">Privacy Policy</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>Science. Service. Stewardship.</p>
    </div>
  </footer>

  <script>
    function toggleAcc(el) {
      const item = el.parentElement;
      item.classList.toggle('active');
      el.querySelector('.icon').textContent = item.classList.contains('active') ? '−' : '+';
    }
  </script>
</body>
</html>
