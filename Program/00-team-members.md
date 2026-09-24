<!-- NOAA FISHERIES STYLE TEAM DIRECTORY -->
<style>
  .noaa-container {
    max-width: 900px;
    margin: 0 auto;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #222222;
  }
  .noaa-card {
    background: #ffffff;
    border: 1px solid #d1d5db;
    border-radius: 8px;
    padding: 28px;
    margin-bottom: 36px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
  }
  .noaa-header {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-start;
    gap: 24px;
    border-bottom: 2px solid #005a9c; /* NOAA Blue accent line */
    padding-bottom: 18px;
    margin-bottom: 20px;
  }
  .noaa-header-info {
    flex: 1;
  }
  .noaa-name {
    margin: 0 0 6px 0;
    font-size: 1.65rem;
    font-weight: 700;
    color: #002244; /* NOAA Dark Blue */
    line-height: 1.2;
  }
  /* BOLD JOB TITLE */
  .noaa-title {
    margin: 0 0 10px 0;
    font-size: 1.15rem;
    font-weight: 700; /* Bolded */
    color: #005a9c;
  }
  .noaa-hierarchy {
    font-size: 0.85rem;
    color: #555555;
    line-height: 1.4;
  }
  .noaa-hierarchy span {
    display: block;
  }
  /* CIRCULAR PROFILE PHOTO */
  .noaa-avatar {
    width: 150px;
    height: 150px;
    border-radius: 50%; /* Makes image a circle */
    object-fit: cover;
    border: 3px solid #005a9c;
    flex-shrink: 0;
    box-shadow: 0 3px 6px rgba(0,0,0,0.1);
  }
  .noaa-bio {
    font-size: 0.95rem;
    line-height: 1.6;
    color: #333333;
    margin-bottom: 20px;
  }
  .noaa-bio p {
    margin: 0 0 12px 0;
  }
  .noaa-bio ul {
    margin: 0 0 12px 0;
    padding-left: 20px;
  }
  .noaa-bio li {
    margin-bottom: 4px;
  }
  .noaa-meta-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 16px;
    background: #f4f7f9;
    padding: 16px;
    border-radius: 6px;
    border-left: 4px solid #005a9c;
  }
  .noaa-section-title {
    margin: 0 0 8px 0;
    font-size: 0.8rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #555555;
  }
  .noaa-contact p {
    margin: 4px 0;
    font-size: 0.9rem;
  }
  .noaa-contact a {
    color: #005a9c;
    text-decoration: underline;
  }
  .noaa-links-list {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }
  .noaa-link-btn {
    display: inline-block;
    background: #ffffff;
    color: #005a9c;
    border: 1px solid #005a9c;
    padding: 4px 12px;
    border-radius: 20px;
    text-decoration: none;
    font-size: 0.82rem;
    font-weight: 600;
    transition: all 0.2s ease-in-out;
  }
  .noaa-link-btn:hover {
    background: #005a9c;
    color: #ffffff;
  }
  
  @media (max-width: 640px) {
    .noaa-header {
      flex-direction: column-reverse;
      align-items: center;
      text-align: center;
    }
  }
</style>

<div class="noaa-container">
  <h1>Team Directory</h1>

  <!-- MEMBER 1 -->
  <div class="noaa-card">
    <div class="noaa-header">
      <div class="noaa-header-info">
        <h2 class="noaa-name">M. Conor McManus, Ph.D.</h2>
        <div class="noaa-title">Supervisory Research Fish Biologist</div>
        <div class="noaa-hierarchy">
          <span>Population & Ecosystems Monitoring & Analysis Division</span>
          <span>Ecosystems Surveys Branch</span>
          <span>Marine Development & Advanced Technology Program</span>
        </div>
      </div>
      <img class="noaa-avatar" src="https://github.com/user-attachments/assets/7fd56b3b-f876-42fd-acc5-b4a96002c9cf" alt="M. Conor McManus" />
    </div>
    <div class="noaa-bio">
      <p>Conor earned a BA in Marine Science from Boston University, and a MS and PhD in Oceanography from the University of Rhode Island’s Graduate School of Oceanography. Previously, Conor worked for Applied Science Associates, and then the Rhode Island Department of Environmental Management’s Division of Marine Fisheries.</p>
      <p>Conor joined the NEFSC in 2024 and leads the Marine Development and Advanced Technology Program, which has several aims including modernizing surveys using advanced technologies and analytics, developing survey mitigation strategies that can support continued data acquisition in the face of various survey challenges, and understanding the interaction between marine development and marine ecosystems. Conor’s research interests are in the fields of fisheries oceanography, population and ecosystem dynamics, survey design, and fisheries management.</p>
    </div>
    <div class="noaa-meta-grid">
      <div class="noaa-contact">
        <div class="noaa-section-title">Contact</div>
        <p><strong>Office:</strong> (401) 859-3404</p>
        <p><strong>Email:</strong> <a href="mailto:michael.conor.mcmanus@noaa.gov">michael.conor.mcmanus@noaa.gov</a></p>
      </div>
      <div class="noaa-links">
        <div class="noaa-section-title">Profiles & Links</div>
        <div class="noaa-links-list">
          <a class="noaa-link-btn" href="https://scholar.google.com/citations?view_op=list_works&hl=en&user=0lPpwIcAAAAJ" target="_blank" rel="noopener">Google Scholar</a>
        </div>
      </div>
    </div>
  </div>

  <!-- MEMBER 2 -->
  <div class="noaa-card">
    <div class="noaa-header">
      <div class="noaa-header-info">
        <h2 class="noaa-name">Cameron Fairclough</h2>
        <div class="noaa-title">Advanced Technology Specialist</div>
        <div class="noaa-hierarchy">
          <span>Population & Ecosystems Monitoring & Analysis Division</span>
          <span>Ecosystems Surveys Branch</span>
          <span>Marine Development & Advanced Technology Program</span>
        </div>
      </div>
      <img class="noaa-avatar" src="https://github.com/user-attachments/assets/06019c5f-e82d-478c-8e63-da5d24a1bd91" alt="Cameron Fairclough" />
    </div>
    <div class="noaa-bio">
      <p>Cameron earned a BA in Marine Biology from Roger Williams University in 2019. Previously, Cameron worked for Woods Hole Oceanographic Institution in various roles in the Biology and Applied Ocean Physics and Engineering departments.</p>
      <p>Cameron joined the NEFSC in 2022 as an Electronics Engineer contractor before transitioning to an Advanced Technology Specialist in 2024. Within the Advanced Technology Group, Cameron develops and implements advanced technologies for ecosystem surveys including towed benthic imaging systems and autonomous underwater vehicles (AUVs). He also supports fishery-independent resource survey operations through at-sea data collection, storage, analysis, and research.</p>
    </div>
    <div class="noaa-meta-grid">
      <div class="noaa-contact">
        <div class="noaa-section-title">Contact</div>
        <p><strong>Office:</strong> (774) 704-2274</p>
        <p><strong>Email:</strong> <a href="mailto:cameron.fairclough@noaa.gov">cameron.fairclough@noaa.gov</a></p>
      </div>
    </div>
  </div>

  <!-- MEMBER 3 -->
  <div class="noaa-card">
    <div class="noaa-header">
      <div class="noaa-header-info">
        <h2 class="noaa-name">Nicholas M. Calabrese, Ph.D.</h2>
        <div class="noaa-title">Fish Biologist</div>
        <div class="noaa-hierarchy">
          <span>Population & Ecosystems Monitoring & Analysis Division</span>
          <span>Ecosystems Surveys Branch</span>
          <span>Marine Development & Advanced Technology Program</span>
        </div>
      </div>
      <img class="noaa-avatar" src="https://github.com/user-attachments/assets/43316965-20e2-40a4-960b-05b1ebe6050a" alt="Nicholas M. Calabrese" />
    </div>
    <div class="noaa-bio">
      <p>Nicholas Calabrese is a fisheries scientist specializing in the development and application of advanced technologies for fisheries-independent surveys. His research focuses on integrating optical imaging systems, artificial intelligence, and innovative sampling approaches to improve the accuracy, efficiency, and sustainability of marine resource assessments.</p>
      <p>Prior to joining NOAA, Nicholas led the development of optical video trawl systems and other optical survey technologies at the University of Massachusetts Dartmouth's School for Marine Science and Technology (SMAST).</p>
      <p>At the Northeast Fisheries Science Center, Nicholas conducts fisheries-independent surveys aboard NOAA research vessels and supports the development, evaluation, and implementation of emerging survey technologies.</p>
      <p><strong>Education:</strong></p>
      <ul>
        <li>B.S. Marine Biology, Roger Williams University, RI</li>
        <li>M.S. Living Marine Resource Science and Management, UMass Dartmouth SMAST, MA</li>
        <li>Ph.D. Living Marine Resource Science and Management, UMass Dartmouth SMAST, MA</li>
      </ul>
    </div>
    <div class="noaa-meta-grid">
      <div class="noaa-contact">
        <div class="noaa-section-title">Contact</div>
        <p><strong>Office:</strong> (401) 307-1599</p>
        <p><strong>Email:</strong> <a href="mailto:nicholas.calabrese@noaa.gov">nicholas.calabrese@noaa.gov</a></p>
      </div>
      <div class="noaa-links">
        <div class="noaa-section-title">Profiles & Links</div>
        <div class="noaa-links-list">
          <a class="noaa-link-btn" href="https://www.linkedin.com/in/nicholas-calabrese-95996b164" target="_blank" rel="noopener">LinkedIn</a>
          <a class="noaa-link-btn" href="https://www.researchgate.net/profile/Nicholas-Calabrese" target="_blank" rel="noopener">ResearchGate</a>
          <a class="noaa-link-btn" href="https://orcid.org/0000-0001-6798-8584" target="_blank" rel="noopener">ORCID</a>
          <a class="noaa-link-btn" href="https://scholar.google.com/citations?user=YbjulGsAAAAJ&hl=en" target="_blank" rel="noopener">Google Scholar</a>
        </div>
      </div>
    </div>
  </div>

  <!-- MEMBER 4 -->
  <div class="noaa-card">
    <div class="noaa-header">
      <div class="noaa-header-info">
        <h2 class="noaa-name">Shannen M. Allen</h2>
        <div class="noaa-title">Biological Technician III (Affiliate)</div>
        <div class="noaa-hierarchy">
          <span>Population & Ecosystems Monitoring & Analysis Division</span>
          <span>Ecosystems Surveys Branch</span>
          <span>Marine Development & Advanced Technology Program</span>
        </div>
      </div>
      <img class="noaa-avatar" src="https://github.com/user-attachments/assets/ae8bc355-f36e-4853-bdca-d1f1c71669be" alt="Shannen M. Allen" />
    </div>
    <div class="noaa-bio">
      <p>Shannen earned a BS in Marine Science, Safety, and Environmental Protection with a concentration in Marine Biology from Massachusetts Maritime Academy in 2023. Prior to joining the Northeast Fisheries Science Center, Shannen worked as a Hydrographer and Marine Scientist supporting NOAA’s Office of Coast Survey.</p>
      <p>Shannen joined the NEFSC Advanced Technology and Marine Development Program in 2026 as a Biological Technician III Affiliate. Within the Advanced Technology Group, she supports fisheries-independent survey operations through the deployment and operation of advanced survey technologies, including HabCam imaging systems, CTD rosettes, multibeam and single-beam sonar systems, and other oceanographic instrumentation.</p>
    </div>
    <div class="noaa-meta-grid">
      <div class="noaa-contact">
        <div class="noaa-section-title">Contact</div>
        <p><strong>Office:</strong> (508) 645-6731</p>
        <p><strong>Email:</strong> <a href="mailto:shannen.allen@noaa.gov">shannen.allen@noaa.gov</a></p>
      </div>
      <div class="noaa-links">
        <div class="noaa-section-title">Profiles & Links</div>
        <div class="noaa-links-list">
          <a class="noaa-link-btn" href="https://www.linkedin.com/in/shannen-allen" target="_blank" rel="noopener">LinkedIn</a>
        </div>
      </div>
    </div>
  </div>

  <!-- MEMBER 5 -->
  <div class="noaa-card">
    <div class="noaa-header">
      <div class="noaa-header-info">
        <h2 class="noaa-name">Jeremy F. Jenrette, Ph.D.</h2>
        <div class="noaa-title">Data Scientist (Affiliate)</div>
        <div class="noaa-hierarchy">
          <span>Population & Ecosystems Monitoring & Analysis Division</span>
          <span>Ecosystems Surveys Branch</span>
          <span>Marine Development & Advanced Technology Program</span>
        </div>
      </div>
      <img class="noaa-avatar" src="https://github.com/user-attachments/assets/fff7511b-b182-4389-9991-4dc6da1c2a62" alt="Jeremy F. Jenrette" />
    </div>
    <div class="noaa-bio">
      <p>Jeremy earned a BS in Biochemistry in 2018 and a PhD in Fish and Wildlife Conservation from Virginia Tech in 2025. As a graduate student, he focused on data science and machine learning applications for monitoring global shark and ray populations. In 2026, Jeremy began working for NOAA’s Advanced Technology Program at the Northeast Fisheries Science Center developing image-recognition software for assessing sea scallop populations from the Habitat Camera Trawl Surveys.</p>
    </div>
    <div class="noaa-meta-grid">
      <div class="noaa-contact">
        <div class="noaa-section-title">Contact</div>
        <p><strong>Office:</strong> (540) 577-6500</p>
        <p><strong>Email:</strong> <a href="mailto:jeremy.jenrette@noaa.gov">jeremy.jenrette@noaa.gov</a></p>
      </div>
      <div class="noaa-links">
        <div class="noaa-section-title">Profiles & Links</div>
        <div class="noaa-links-list">
          <a class="noaa-link-btn" href="https://www.linkedin.com/in/jeremy-jenrette-5579a4105/" target="_blank" rel="noopener">LinkedIn</a>
          <a class="noaa-link-btn" href="https://www.researchgate.net/profile/Jeremy-Jenrette" target="_blank" rel="noopener">ResearchGate</a>
          <a class="noaa-link-btn" href="https://orcid.org/0000-0003-2511-9334" target="_blank" rel="noopener">ORCID</a>
          <a class="noaa-link-btn" href="https://scholar.google.com/citations?hl=en&user=IgYt-j0AAAAJ" target="_blank" rel="noopener">Google Scholar</a>
          <a class="noaa-link-btn" href="https://jeremyjenrette.weebly.com/" target="_blank" rel="noopener">Website</a>
        </div>
      </div>
    </div>
  </div>

  <!-- MEMBER 6 -->
  <div class="noaa-card">
    <div class="noaa-header">
      <div class="noaa-header-info">
        <h2 class="noaa-name">Dana Morton, Ph.D.</h2>
        <div class="noaa-title">Fishery Biologist</div>
        <div class="noaa-hierarchy">
          <span>Population & Ecosystems Monitoring & Analysis Division</span>
          <span>Ecosystems Surveys Branch</span>
          <span>Shellfish Survey Program</span>
        </div>
      </div>
      <img class="noaa-avatar" src="https://github.com/user-attachments/assets/7cefab01-d689-4623-b3d5-2024e3c6faa3" alt="Dana Morton" />
    </div>
    <div class="noaa-bio">
      <p>Dana is a marine ecologist with research interests in shellfish biology, invertebrate zoology, food webs, parasite ecology, and spatial ecology. Her work uses a combination of quantitative approaches and natural history to gain mechanistic understanding of ecosystem processes and inform management issues. Dana earned a Ph.D. in Ecology, Evolution, and Marine Biology from University of California, Santa Barbara, an M.Sc. in Ecology from San Diego State University, and a B.S. in Marine Biology from University of California, Santa Cruz. She began working at NOAA in 2023 following a postdoctoral fellowship at Colby College.</p>
    </div>
    <div class="noaa-meta-grid">
      <div class="noaa-contact">
        <div class="noaa-section-title">Contact</div>
        <p><strong>Office:</strong> (774) 238-7424</p>
        <p><strong>Email:</strong> <a href="mailto:dana.morton@noaa.gov">dana.morton@noaa.gov</a></p>
      </div>
      <div class="noaa-links">
        <div class="noaa-section-title">Profiles & Links</div>
        <div class="noaa-links-list">
          <a class="noaa-link-btn" href="https://scholar.google.com/citations?user=GUCJgkwAAAAJ&hl=en" target="_blank" rel="noopener">Google Scholar</a>
        </div>
      </div>
    </div>
  </div>

  <!-- MEMBER 7 -->
  <div class="noaa-card">
    <div class="noaa-header">
      <div class="noaa-header-info">
        <h2 class="noaa-name">Zachary Fyke</h2>
        <div class="noaa-title">Biological Science Technician</div>
        <div class="noaa-hierarchy">
          <span>Population & Ecosystems Monitoring & Analysis Division</span>
          <span>Ecosystems Surveys Branch</span>
          <span>Shellfish Survey Program</span>
        </div>
      </div>
      <img class="noaa-avatar" src="https://github.com/user-attachments/assets/02b14935-c5e9-4273-a6f3-d649f4740916" alt="Zachary Fyke" />
    </div>
    <div class="noaa-bio">
      <p>Zachary graduated from Michigan State University with a Bachelor of Science in Fisheries and Wildlife in June of 2017. He started his career in Marine Science as a fisheries observer, based out of Point Judith, Rhode Island. After two years of observing, he came in-house to work at the Northeast Fisheries Observer Training Center in North Falmouth, Massachusetts. After a year working as the observer compliance liaison, Zachary started a federal position with NOAA Office of Law Enforcement. As part of ESB, Zachary primarily works on Shellfish Surveys including Atlantic Sea Scallop, Northern Shrimp, Ocean Quahog, and Atlantic Surfclam.</p>
    </div>
    <div class="noaa-meta-grid">
      <div class="noaa-contact">
        <div class="noaa-section-title">Contact</div>
        <p><strong>Office:</strong> (508) 495-2002</p>
        <p><strong>Email:</strong> <a href="mailto:zachary.fyke@noaa.gov">zachary.fyke@noaa.gov</a></p>
      </div>
    </div>
  </div>

  <!-- MEMBER 8 -->
  <div class="noaa-card">
    <div class="noaa-header">
      <div class="noaa-header-info">
        <h2 class="noaa-name">Jonathan Duquette</h2>
        <div class="noaa-title">Biological Science Technician</div>
        <div class="noaa-hierarchy">
          <span>Population & Ecosystems Monitoring & Analysis Division</span>
          <span>Ecosystems Surveys Branch</span>
          <span>Shellfish Survey Program</span>
        </div>
      </div>
      <img class="noaa-avatar" src="https://github.com/user-attachments/assets/c20df02d-b212-48b9-a2f3-c91e587a2067" alt="Jonathan Duquette" />
    </div>
    <div class="noaa-bio">
      <p>Jonathan Duquette is a Biological Science Technician with the Ecosystems Surveys Branch at the Northeast Fisheries Science Center. Specializing in fisheries science and marine data collection, Jonathan plays an integral role in critical research initiatives, including the high-resolution HabCam (Habitat Camera Array) and sea scallop dredge surveys.</p>
      <p>After graduating with a BS in Marine Biology from the University of New England, Jonathan became a fisheries observer, collecting data on fishing vessels in Alaska. In 2003, Jonathan joined the Ecosystems Surveys Branch as a Biological Science Technician.</p>
    </div>
    <div class="noaa-meta-grid">
      <div class="noaa-contact">
        <div class="noaa-section-title">Contact</div>
        <p><strong>Office:</strong> (508) 495-2034</p>
        <p><strong>Email:</strong> <a href="mailto:jonathan.duquette@noaa.gov">jonathan.duquette@noaa.gov</a></p>
      </div>
    </div>
  </div>

  <!-- MEMBER 9 -->
  <div class="noaa-card">
    <div class="noaa-header">
      <div class="noaa-header-info">
        <h2 class="noaa-name">Dvora Hart, Ph.D.</h2>
        <div class="noaa-title">Operations Research Analyst</div>
        <div class="noaa-hierarchy">
          <span>Resource Evaluation & Assessment Division</span>
          <span>Populations Dynamics Branch</span>
          <span>Stock Assessment Methods Task Program</span>
        </div>
      </div>
      <img class="noaa-avatar" src="https://github.com/user-attachments/assets/e523b7b4-70d9-41b3-8f12-8183409c477d" alt="Dvora Hart" />
    </div>
    <div class="noaa-bio">
      <p>Dvora is the lead assessment scientist for Atlantic sea scallops, and secondary for spiny dogfish. She is a member of Automated Image Analysis Strategic Initiative Committee, ICES Stock Assessment Methods Working Group, and the NEFMC Sea Scallop PDT.</p>
      <p>At NEFSC, she, together with colleagues, has developed length-based and spatial stock assessment methods that are in particular applicable to the sea scallop fishery. The spatial SAMS model that she began developing soon after arriving at NEFSC is the primary forecasting tool used by the New England Fishery Management Council to aid in management of sea scallops.</p>
    </div>
    <div class="noaa-meta-grid">
      <div class="noaa-contact">
        <div class="noaa-section-title">Contact</div>
        <p><strong>Office:</strong> (508) 495-2369</p>
        <p><strong>Email:</strong> <a href="mailto:deborah.hart@noaa.gov">deborah.hart@noaa.gov</a></p>
      </div>
      <div class="noaa-links">
        <div class="noaa-section-title">Profiles & Links</div>
        <div class="noaa-links-list">
          <a class="noaa-link-btn" href="https://www.researchgate.net/profile/Dvora-Hart" target="_blank" rel="noopener">ResearchGate</a>
          <a class="noaa-link-btn" href="https://www.scopus.com/authid/detail.uri?authorId=7402132627" target="_blank" rel="noopener">Scopus</a>
          <a class="noaa-link-btn" href="https://orcid.org/0000-0002-0406-0751" target="_blank" rel="noopener">ORCID</a>
        </div>
      </div>
    </div>
  </div>

  <!-- MEMBER 10 -->
  <div class="noaa-card">
    <div class="noaa-header">
      <div class="noaa-header-info">
        <h2 class="noaa-name">Jui-Han Chang, Ph.D.</h2>
        <div class="noaa-title">Research Biologist (Affiliate)</div>
        <div class="noaa-hierarchy">
          <span>Resource Evaluation & Assessment Division</span>
          <span>Populations Dynamics Branch</span>
          <span>Stock Assessment Methods Task Program</span>
        </div>
      </div>
      <img class="noaa-avatar" src="https://github.com/user-attachments/assets/1e50cd9f-0d3e-4341-9496-b7d30f99bd43" alt="Jui-Han Chang" />
    </div>
    <div class="noaa-bio">
      <p><strong>Education:</strong></p>
      <ul>
        <li>Ph.D. Interdisciplinary (Marine Sciences, Statistics, and Resource Economics), University of Maine</li>
        <li>M.S. Marine Resource Assessment and Management, National Taiwan Ocean University</li>
        <li>B.B.A. International Trade, Aletheia University</li>
      </ul>
    </div>
    <div class="noaa-meta-grid">
      <div class="noaa-contact">
        <div class="noaa-section-title">Contact</div>
        <p><strong>Office:</strong> (508) 495-2052</p>
        <p><strong>Email:</strong> <a href="mailto:jui-han.chang@noaa.gov">jui-han.chang@noaa.gov</a></p>
      </div>
    </div>
  </div>

  <!-- MEMBER 11 -->
  <div class="noaa-card">
    <div class="noaa-header">
      <div class="noaa-header-info">
        <h2 class="noaa-name">Alexander Hansell, Ph.D.</h2>
        <div class="noaa-title">Fish Biologist</div>
        <div class="noaa-hierarchy">
          <span>Resource Evaluation & Assessment Division</span>
          <span>Populations Dynamics Branch</span>
          <span>Stock Assessment Methods Task Program</span>
        </div>
      </div>
      <img class="noaa-avatar" src="https://github.com/user-attachments/assets/9465f3cf-2c5d-4762-a8a6-e0fbe7d065e8" alt="Alexander Hansell" />
    </div>
    <div class="noaa-bio">
      <p>Alex earned a BS in Biology from Northeastern University and a PhD in Fisheries Oceanography from the University of Massachusetts. Alex is the lead assessment scientist for Georges Bank yellowtail flounder, Georges Bank winter flounder and Southern New England Cod.</p>
    </div>
    <div class="noaa-meta-grid">
      <div class="noaa-contact">
        <div class="noaa-section-title">Contact</div>
        <p><strong>Office:</strong> (508) 203-6894</p>
        <p><strong>Email:</strong> <a href="mailto:alex.hansell@noaa.gov">alex.hansell@noaa.gov</a></p>
      </div>
      <div class="noaa-links">
        <div class="noaa-section-title">Profiles & Links</div>
        <div class="noaa-links-list">
          <a class="noaa-link-btn" href="https://scholar.google.com/citations?user=d8gvRasAAAAJ&hl=en" target="_blank" rel="noopener">Google Scholar</a>
        </div>
      </div>
    </div>
  </div>
</div>
