import fitz  # PyMuPDF
import os
import glob

# 1. Automatically locate your system Downloads folder
downloads_path = os.path.expanduser("~/Downloads")
pdf_files = glob.glob(os.path.join(downloads_path, "*.pdf"))

if not pdf_files:
    print(f"No PDF files found in {downloads_path}")
    exit()

print(f"Found {len(pdf_files)} PDF(s) in Downloads folder. Processing...\n")

for pdf_path in pdf_files:
    raw_filename = os.path.basename(pdf_path)
    base_name = os.path.splitext(raw_filename)[0]
    
    # 2. Convert name to web-safe identifier (e.g., "Species Guide.pdf" -> "species-guide")
    deck_id = base_name.lower().replace(" ", "-").replace("(", "").replace(")", "")
    
    output_folder = f"slides-{deck_id}"
    html_file = f"carousel-{deck_id}.html"
    dom_id = f"carousel-{deck_id}"
    
    os.makedirs(output_folder, exist_ok=True)
    doc = fitz.open(pdf_path)
    
    # 3. Compress pages into lightweight JPEGs
    items = []
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=90)
        img_rel_path = f"{output_folder}/slide-{i+1:02d}.jpg"
        pix.save(img_rel_path, jpg_quality=75)
        
        active = " active" if i == 0 else ""
        items.append(
            f'<div class="carousel-item{active}">\n'
            f'<img src="{img_rel_path}" class="d-block w-100" alt="Slide {i+1}">\n'
            f'</div>'
        )
    
    # 4. Generate unindented HTML with unique DOM IDs
    html_content = f"""<style>
#{dom_id} {{
position: relative;
max-width: 850px;
margin: 0 auto;
border: 1px solid #ddd;
border-radius: 8px;
padding: 10px;
background: #f9f9f9;
}}
#{dom_id}:fullscreen,
#{dom_id}:-webkit-full-screen {{
width: 100vw !important;
height: 100vh !important;
max-width: 100% !important;
background-color: #000 !important;
padding: 0 !important;
border: none !important;
margin: 0 !important;
}}
#{dom_id}:fullscreen .carousel-inner,
#{dom_id}:-webkit-full-screen .carousel-inner {{
height: 100vh !important;
}}
#{dom_id}:fullscreen .carousel-item,
#{dom_id}:-webkit-full-screen .carousel-item {{
height: 100vh !important;
}}
#{dom_id}:fullscreen .carousel-item img,
#{dom_id}:-webkit-full-screen .carousel-item img {{
max-height: 100vh !important;
max-width: 100vw !important;
height: 100% !important;
width: 100% !important;
object-fit: contain !important;
margin: 0 auto;
}}
#{dom_id}:fullscreen .carousel-control-prev,
#{dom_id}:fullscreen .carousel-control-next,
#{dom_id}:-webkit-full-screen .carousel-control-prev,
#{dom_id}:-webkit-full-screen .carousel-control-next {{
z-index: 1050 !important;
width: 15%;
}}
.fullscreen-toggle-btn {{
position: absolute;
top: 15px;
right: 15px;
z-index: 1100;
background: rgba(0, 0, 0, 0.75);
color: #fff;
border: 1px solid rgba(255, 255, 255, 0.5);
border-radius: 4px;
padding: 6px 12px;
font-size: 13px;
cursor: pointer;
}}
.fullscreen-toggle-btn:hover {{
background: rgba(0, 0, 0, 0.95);
}}
</style>

<div id="{dom_id}" class="carousel slide" data-bs-ride="false">
<button type="button" class="fullscreen-toggle-btn" onclick="toggleFS('{dom_id}')">
⛶ Fullscreen
</button>
<div class="carousel-inner">
{"\n".join(items)}
</div>
<button class="carousel-control-prev" type="button" data-bs-target="#{dom_id}" data-bs-slide="prev">
<span class="carousel-control-prev-icon" aria-hidden="true" style="filter: invert(1);"></span>
<span class="visually-hidden">Previous</span>
</button>
<button class="carousel-control-next" type="button" data-bs-target="#{dom_id}" data-bs-slide="next">
<span class="carousel-control-next-icon" aria-hidden="true" style="filter: invert(1);"></span>
<span class="visually-hidden">Next</span>
</button>
</div>

<script>
if (typeof toggleFS !== 'function') {{
function toggleFS(id) {{
const elem = document.getElementById(id);
if (!document.fullscreenElement && !document.webkitFullscreenElement) {{
if (elem.requestFullscreen) elem.requestFullscreen();
else if (elem.webkitRequestFullscreen) elem.webkitRequestFullscreen();
}} else {{
if (document.exitFullscreen) document.exitFullscreen();
else if (document.webkitExitFullscreen) document.webkitExitFullscreen();
}}
}}
}}
</script>"""

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"✓ Created: '{html_file}' and '{output_folder}/' ({len(doc)} slides)")
