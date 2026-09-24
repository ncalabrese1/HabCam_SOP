<!-- TEAM MEMBERS SECTION -->
<style>
  .team-container {
    max-width: 900px;
    margin: 0 auto;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1a202c;
  }
  .team-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 32px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
  }
  .team-header {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-start;
    gap: 20px;
    border-bottom: 1px solid #edf2f7;
    padding-bottom: 16px;
    margin-bottom: 16px;
  }
  .team-avatar {
    width: 140px;
    height: 140px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid #005a9c;
    flex-shrink: 0;
  }
  .team-name {
    margin: 0 0 6px 0;
    font-size: 1.5rem;
    color: #003366;
  }
  .team-title {
    margin: 0 0 8px 0;
    font-weight: 600;
    color: #2b6cb0;
    font-size: 1.05rem;
  }
  .team-dept-badge {
    display: inline-block;
    background: #ebf8ff;
    color: #2b6cb0;
    font-size: 0.75rem;
    padding: 3px 8px;
    border-radius: 4px;
    margin-right: 4px;
    margin-bottom: 4px;
    font-weight: 500;
  }
  .team-bio {
    line-height: 1.6;
    color: #4a5568;
    margin-bottom: 16px;
  }
  .team-meta {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 16px;
    background: #f7fafc;
    padding: 16px;
    border-radius: 8px;
  }
  .team-contact h4, .team-links h4 {
    margin: 0 0 8px 0;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #718096;
  }
  .team-contact p {
    margin: 4px 0;
    font-size: 0.9rem;
  }
  .link-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }
  .link-pill {
    display: inline-block;
    background: #edf2f7;
    color: #2d3748;
    padding: 4px 10px;
    border-radius: 6px;
    text-decoration: none;
    font-size: 0.85rem;
    font-weight: 500;
    transition: background 0.2s ease;
  }
  .link-pill:hover {
    background: #005a9c;
    color: #ffffff;
  }
  @media (max-width: 600px) {
    .team-header {
      flex-direction: column-reverse;
      align-items: center;
      text-align: center;
    }
  }
</style>

<div class="team-container">
  <h1>Team Members</h1>

  <!-- MEMBER 1 -->
  <div class="team-card">
    <div class="team-header">
      <div>
        <h2 class="team-name">M. Conor McManus, Ph.D.</h2>
        <div class="team-title">Supervisory Research Fish Biologist</div>
        <div>
          <span class="team-dept-badge">Population & Ecosystems Monitoring & Analysis Division</span>
          <span class="team-dept-badge">Ecosystems Surveys Branch</span>
          <span class="team-dept-badge">Marine Development & Advanced Technology Program</span>
        </div>
      </div>
      <img class="team-avatar" src="https://github.com/user-attachments/assets/7fd56b3b-f876-42fd-acc5-b4a96002c9cf" alt="M. Conor McManus" />
    </div>
    <div class="team-bio">
      <p>Conor earned a BA in Marine Science from Boston University, and a MS and PhD in Oceanography from the University of Rhode Island’s Graduate School of Oceanography. Previously, Conor worked for Applied Science Associates, and then the Rhode Island Department of Environmental Management’s Division of Marine Fisheries.</p>
      <p>Conor joined the NEFSC in 2024 and leads the Marine Development and Advanced Technology Program, which has several aims including modernizing surveys using advanced technologies and analytics, developing survey mitigation strategies that can support continued data acquisition in the face of various survey challenges, and understanding the interaction between marine development and marine ecosystems. Conor’s research interests are in the fields of fisheries oceanography, population and ecosystem dynamics, survey design, and fisheries management.</p>
    </div>
    <div class="team-meta">
      <div class="team-contact">
        <h4>Contact</h4>
        <p><strong>Office:</strong> (401) 859-3404</p>
        <p><strong>Email:</strong> <a href="mailto:michael.conor.mcmanus@noaa.gov">michael.conor.mcmanus@noaa.gov</a></p>
      </div>
      <div class="team-links">
        <h4>Relevant Links</h4>
        <div class="link-pills">
          <a class="link-pill" href="https://scholar.google.com/citations?view_op=list_works&hl=en&user=0lPpwIcAAAAJ" target="_blank" rel="noopener">Google Scholar</a>
        </div>
      </div>
    </div>
  </div>

  <!-- MEMBER 2 -->
  <div class="team-card">
    <div class="team-header">
      <div>
        <h2 class="team-name">Cameron Fairclough</h2>
        <div class="team-title">Advanced Technology Specialist</div>
        <div>
          <span class="team-dept-badge">Population & Ecosystems Monitoring & Analysis Division</span>
          <span class="team-dept-badge">Ecosystems Surveys Branch</span>
          <span class="team-dept-badge">Marine Development & Advanced Technology Program</span>
        </div>
      </div>
      <img class="team-avatar" src="https://github.com/user-attachments/assets/06019c5f-e82d-478c-8e63-da5d24a1bd91" alt="Cameron Fairclough" />
    </div>
    <div class="team-bio">
      <p>Cameron earned a BA in Marine Biology from Roger Williams University in 2019. Previously, Cameron worked for Woods Hole Oceanographic Institution in various roles in the Biology and Applied Ocean Physics and Engineering departments.</p>
      <p>Cameron joined the NEFSC in 2022 as an Electronics Engineer contractor before transitioning to an Advanced Technology Specialist in 2024. Within the Advanced Technology Group, Cameron develops and implements advanced technologies for ecosystem surveys including towed benthic imaging systems and autonomous underwater vehicles (AUVs). He also supports fishery-independent resource survey operations through at-sea data collection, storage, analysis, and research.</p>
    </div>
    <div class="team-meta">
      <div class="team-contact">
        <h4>Contact</h4>
        <p><strong>Office:</strong> (774) 704-2274</p>
        <p><strong>Email:</strong> <a href="mailto:cameron.fairclough@noaa.gov">cameron.fairclough@noaa.gov</a></p>
      </div>
    </div>
  </div>

  <!-- MEMBER 3 -->
  <div class="team-card">
    <div class="team-header">
      <div>
        <h2 class="team-name">Nicholas M. Calabrese, Ph.D.</h2>
        <div class="team-title">Fish Biologist</div>
        <div>
          <span class="team-dept-badge">Population & Ecosystems Monitoring & Analysis Division</span>
          <span class="team-dept-badge">Ecosystems Surveys Branch</span>
          <span class="team-dept-badge">Marine Development & Advanced Technology Program</span>
        </div>
      </div>
      <img class="team-avatar" src="https://github.com/user-attachments/assets/43316965-20e2-40a4-960b-05b1ebe6050a" alt="Nicholas M. Calabrese" />
    </div>
    <div class="team-bio">
      <p>Nicholas Calabrese is a fisheries scientist specializing in the development and application of advanced technologies for fisheries-independent surveys. His research focuses on integrating optical imaging systems, artificial intelligence, and innovative sampling approaches to improve the accuracy, efficiency, and sustainability of marine resource assessments.</p>
      <p>Prior to joining NOAA, Nicholas led the development of optical video trawl systems and other optical survey technologies at UMass Dartmouth's School for Marine Science and Technology (SMAST).</p>
      <p><strong>Education:</strong> B.S. Marine Biology (Roger Williams University), M.S. & Ph.D. Living Marine Resource Science and Management (UMass Dartmouth SMAST).</p>
    </div>
    <div class="team-meta">
      <div class="team-contact">
        <h4>Contact</h4>
        <p><strong>Office:</strong> (401) 307-1599</p>
        <p><strong>Email:</strong> <a href="mailto:nicholas.calabrese@noaa.gov">nicholas.calabrese@noaa.gov</a></p>
      </div>
      <div class="team-links">
        <h4>Relevant Links</h4>
        <div class="link-pills">
          <a class="link-pill" href="https://www.linkedin.com/in/nicholas-calabrese-95996b164" target="_blank" rel="noopener">LinkedIn</a>
          <a class="link-pill" href="https://www.researchgate.net/profile/Nicholas-Calabrese" target="_blank" rel="noopener">ResearchGate</a>
          <a class="link-pill" href="https://orcid.org/0000-0001-6798-8584" target="_blank" rel="noopener">ORCID</a>
          <a class="link-pill" href="https://scholar.google.com/citations?user=YbjulGsAAAAJ&hl=en" target="_blank" rel="noopener">Google Scholar</a>
        </div>
      </div>
    </div>
  </div>

  <!-- MEMBER 4 -->
  <div class="team-card">
    <div class="team-header">
      <div>
        <h2 class="team-name">Shannen M. Allen</h2>
        <div class="team-title">Biological Technician III (Affiliate)</div>
        <div>
          <span class="team-dept-badge">Population & Ecosystems Monitoring & Analysis Division</span>
          <span class="team-dept-badge">Ecosystems Surveys Branch</span>
          <span class="team-dept-badge">Marine Development & Advanced Technology Program</span>
        </div>
      </div>
      <img class="team-avatar" src="https://github.com/user-attachments/assets/ae8bc355-f36e-4853-bdca-d1f1c71669be" alt="Shannen M. Allen" />
    </div>
    <div class="team-bio">
      <p>Shannen earned a BS in Marine Science, Safety, and Environmental Protection from Massachusetts Maritime Academy in 2023. Prior to joining NEFSC, Shannen worked as a Hydrographer and Marine Scientist supporting NOAA’s Office of Coast Survey.</p>
      <p>Shannen joined the NEFSC program in 2026 as a Biological Technician III Affiliate. She supports fisheries-independent survey operations through the deployment and operation of advanced survey technologies including HabCam imaging systems, CTD rosettes, and sonar systems.</p>
    </div>
    <div class="team-meta">
      <div class="team-contact">
        <h4>Contact</h4>
        <p><strong>Office:</strong> (508) 645-6731</p>
        <p><strong>Email:</strong> <a href="mailto:shannen.allen@noaa.gov">shannen.allen@noaa.gov</a></p>
      </div>
      <div class="team-links">
        <h4>Relevant Links</h4>
        <div class="link-pills">
          <a class="link-pill" href="https://www.linkedin.com/in/shannen-allen" target="_blank" rel="noopener">LinkedIn</a>
        </div>
      </div>
    </div>
  </div>

  <!-- MEMBER 5 -->
  <div class="team-card">
    <div class="team-header">
      <div>
        <h2 class="team-name">Jeremy F. Jenrette, Ph.D.</h2>
        <div class="team-title">Data Scientist (Affiliate)</div>
        <div>
          <span class="team-dept-badge">Population & Ecosystems Monitoring & Analysis Division</span>
          <span class="team-dept-badge">Ecosystems Surveys Branch</span>
          <span class="team-dept-badge">Marine Development & Advanced Technology Program</span>
        </div>
      </div>
      <img class="team-avatar" src="https://github.com/user-attachments/assets/fff7511b-b182-4389-9991-4dc6da1c2a62" alt="Jeremy F. Jenrette" />
    </div>
    <div class="team-bio">
      <p>Jeremy earned a BS in Biochemistry in 2018 and a PhD in Fish and Wildlife Conservation from Virginia Tech in 2025 focusing on machine learning applications for monitoring shark and ray populations. In 2026, Jeremy began working for NOAA’s Advanced Technology Program developing image-recognition software to automatically assess sea scallop populations from Habitat Camera Trawl Surveys.</p>
    </div>
    <div class="team-meta">
      <div class="team-contact">
        <h4>Contact</h4>
        <p><strong>Office:</strong> (540) 577-6500</p>
        <p><strong>Email:</strong> <a href="mailto:jeremy.jenrette@noaa.gov">jeremy.jenrette@noaa.gov</a></p>
      </div>
      <div class="team-links">
        <h4>Relevant Links</h4>
        <div class="link-pills">
          <a class="link-pill" href="https://www.linkedin.com/in/jeremy-jenrette-5579a4105/" target="_blank" rel="noopener">LinkedIn</a>
          <a class="link-pill" href="https://www.researchgate.net/profile/Jeremy-Jenrette" target="_blank" rel="noopener">ResearchGate</a>
          <a class="link-pill" href="https://orcid.org/0000-0003-2511-9334" target="_blank" rel="noopener">ORCID</a>
          <a class="link-pill" href="https://scholar.google.com/citations?hl=en&user=IgYt-j0AAAAJ" target="_blank" rel="noopener">Google Scholar</a>
          <a class="link-pill" href="https://jeremyjenrette.weebly.com/" target="_blank" rel="noopener">Personal Website</a>
        </div>
      </div>
    </div>
  </div>

  <!-- MEMBER 6 -->
  <div class="team-card">
    <div class="team-header">
      <div>
        <h2 class="team-name">Dana Morton, Ph.D.</h2>
        <div class="team-title">Fishery Biologist</div>
        <div>
          <span class="team-dept-badge">Population & Ecosystems Monitoring & Analysis Division</span>
          <span class="team-dept-badge">Ecosystems Surveys Branch</span>
          <span class="team-dept-badge">Shellfish Survey Program</span>
        </div>
      </div>
      <img class="team-avatar" src="https://github.com/user-attachments/assets/7cefab01-d689-4623-b3d5-2024e3c6faa3" alt="Dana Morton" />
    </div>
    <div class="team-bio">
      <p>Dana is a marine ecologist with research interests in shellfish biology, invertebrate zoology, food webs, parasite ecology, and spatial ecology. Dana earned a Ph.D. in Ecology, Evolution, and Marine Biology from UC Santa Barbara, an M.Sc. from San Diego State University, and a B.S. from UC Santa Cruz. She joined NOAA in 2023.</p>
    </div>
    <div class="team-meta">
      <div class="team-contact">
        <h4>Contact</h4>
        <p><strong>Office:</strong> (774) 238-7424</p>
        <p><strong>Email:</strong> <a href="mailto:dana.morton@noaa.gov">dana.morton@noaa.gov</a></p>
      </div>
      <div class="team-links">
        <h4>Relevant Links</h4>
        <div class="link-pills">
          <a class="link-pill" href="https://scholar.google.com/citations?user=GUCJgkwAAAAJ&hl=en" target="_blank" rel="noopener">Google Scholar</a>
        </div>
      </div>
    </div>
  </div>

  <!-- MEMBER 7 -->
  <div class="team-card">
    <div class="team-header">
      <div>
        <h2 class="team-name">Zachary Fyke</h2>
        <div class="team-title">Biological Science Technician</div>
        <div>
          <span class="team-dept-badge">Population & Ecosystems Monitoring & Analysis Division</span>
          <span class="team-dept-badge">Ecosystems Surveys Branch</span>
          <span class="team-dept-badge">Shellfish Survey Program</span>
        </div>
      </div>
      <img class="team-avatar" src="https://github.com/user-attachments/assets/02b14935-c5e9-4273-a6f3-d649f4740916" alt="Zachary Fyke" />
    </div>
    <div class="team-bio">
      <p>Zachary graduated from Michigan State University with a B.S. in Fisheries and Wildlife in 2017. As part of ESB, Zachary primarily works on Shellfish Surveys including Atlantic Sea Scallop, Northern Shrimp, Ocean Quahog, and Atlantic Surfclam.</p>
    </div>
    <div class="team-meta">
      <div class="team-contact">
        <h4>Contact</h4>
        <p><strong>Office:</strong> (508) 495-2002</p>
        <p><strong>Email:</strong> <a href="mailto:zachary.fyke@noaa.gov">zachary.fyke@noaa.gov</a></p>
      </div>
    </div>
  </div>

  <!-- MEMBER 8 -->
  <div class="team-card">
    <div class="team-header">
      <div>
        <h2 class="team-name">Jonathan Duquette</h2>
        <div class="team-title">Biological Science Technician</div>
        <div>
          <span class="team-dept-badge">Population & Ecosystems Monitoring & Analysis Division</span>
          <span class="team-dept-badge">Ecosystems Surveys Branch</span>
          <span class="team-dept-badge">Shellfish Survey Program</span>
        </div>
      </div>
      <img class="team-avatar" src="https://github.com/user-attachments/assets/c20df02d-b212-48b9-a2f3-c91e587a2067" alt="Jonathan Duquette" />
    </div>
    <div class="team-bio">
      <p>Jonathan specializes in fisheries science and marine data collection, playing an integral role in the high-resolution HabCam and sea scallop dredge surveys. He graduated with a BS in Marine Biology from the University of New England and joined the Ecosystems Surveys Branch in 2003.</p>
    </div>
    <div class="team-meta">
      <div class="team-contact">
        <h4>Contact</h4>
        <p><strong>Office:</strong> (508) 495-2034</p>
        <p><strong>Email:</strong> <a href="mailto:jonathan.duquette@noaa.gov">jonathan.duquette@noaa.gov</a></p>
      </div>
    </div>
  </div>

  <!-- MEMBER 9 -->
  <div class="team-card">
    <div class="team-header">
      <div>
        <h2 class="team-name">Dvora Hart, Ph.D.</h2>
        <div class="team-title">Operations Research Analyst</div>
        <div>
          <span class="team-dept-badge">Resource Evaluation & Assessment Division</span>
          <span class="team-dept-badge">Populations Dynamics Branch</span>
          <span class="team-dept-badge">Stock Assessment Methods Task Program</span>
        </div>
      </div>
      <img class="team-avatar" src="https://github.com/user-attachments/assets/e523b7b4-70d9-41b3-8f12-8183409c477d" alt="Dvora Hart" />
    </div>
    <div class="team-bio">
      <p>Dvora is the lead assessment scientist for Atlantic sea scallops, and secondary for spiny dogfish. She developed length-based and spatial stock assessment methods (such as the SAMS model) and tools to analyze HabCam towed camera survey data.</p>
    </div>
    <div class="team-meta">
      <div class="team-contact">
        <h4>Contact</h4>
        <p><strong>Office:</strong> (508) 495-2369</p>
        <p><strong>Email:</strong> <a href="mailto:deborah.hart@noaa.gov">deborah.hart@noaa.gov</a></p>
      </div>
      <div class="team-links">
        <h4>Relevant Links</h4>
        <div class="link-pills">
          <a class="link-pill" href="https://www.researchgate.net/profile/Dvora-Hart" target="_blank" rel="noopener">ResearchGate</a>
          <a class="link-pill" href="https://www.scopus.com/authid/detail.uri?authorId=7402132627" target="_blank" rel="noopener">Scopus</a>
          <a class="link-pill" href="https://orcid.org/0000-0002-0406-0751" target="_blank" rel="noopener">ORCID</a>
        </div>
      </div>
    </div>
  </div>

  <!-- MEMBER 10 -->
  <div class="team-card">
    <div class="team-header">
      <div>
        <h2 class="team-name">Jui-Han Chang, Ph.D.</h2>
        <div class="team-title">Research Biologist (Affiliate)</div>
        <div>
          <span class="team-dept-badge">Resource Evaluation & Assessment Division</span>
          <span class="team-dept-badge">Populations Dynamics Branch</span>
          <span class="team-dept-badge">Stock Assessment Methods Task Program</span>
        </div>
      </div>
      <img class="team-avatar" src="https://github.com/user-attachments/assets/1e50cd9f-0d3e-4341-9496-b7d30f99bd43" alt="Jui-Han Chang" />
    </div>
    <div class="team-bio">
      <p><strong>Education:</strong></p>
      <ul>
        <li>Ph.D. Interdisciplinary (Marine Sciences, Statistics, and Resource Economics), University of Maine</li>
        <li>M.S. Marine Resource Assessment and Management, National Taiwan Ocean University</li>
        <li>B.B.A. International Trade, Aletheia University</li>
      </ul>
    </div>
    <div class="team-meta">
      <div class="team-contact">
        <h4>Contact</h4>
        <p><strong>Office:</strong> (508) 495-2052</p>
        <p><strong>Email:</strong> <a href="mailto:jui-han.chang@noaa.gov">jui-han.chang@noaa.gov</a></p>
      </div>
    </div>
  </div>

  <!-- MEMBER 11 -->
  <div class="team-card">
    <div class="team-header">
      <div>
        <h2 class="team-name">Alexander Hansell, Ph.D.</h2>
        <div class="team-title">Fish Biologist</div>
        <div>
          <span class="team-dept-badge">Resource Evaluation & Assessment Division</span>
          <span class="team-dept-badge">Populations Dynamics Branch</span>
          <span class="team-dept-badge">Stock Assessment Methods Task Program</span>
        </div>
      </div>
      <img class="team-avatar" src="https://github.com/user-attachments/assets/9465f3cf-2c5d-4762-a8a6-e0fbe7d065e8" alt="Alexander Hansell" />
    </div>
    <div class="team-bio">
      <p>Alex earned a BS in Biology from Northeastern University and a PhD in Fisheries Oceanography from the University of Massachusetts. Alex is the lead assessment scientist for Georges Bank yellowtail flounder, Georges Bank winter flounder, and Southern New England Cod.</p>
    </div>
    <div class="team-meta">
      <div class="team-contact">
        <h4>Contact</h4>
        <p><strong>Office:</strong> (508) 203-6894</p>
        <p><strong>Email:</strong> <a href="mailto:alex.hansell@noaa.gov">alex.hansell@noaa.gov</a></p>
      </div>
      <div class="team-links">
        <h4>Relevant Links</h4>
        <div class="link-pills">
          <a class="link-pill" href="https://scholar.google.com/citations?user=d8gvRasAAAAJ&hl=en" target="_blank" rel="noopener">Google Scholar</a>
        </div>
      </div>
    </div>
  </div>
</div>
