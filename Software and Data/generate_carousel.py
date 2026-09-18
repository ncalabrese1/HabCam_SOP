# Set your slide folder, total count, and file extension (.png or .jpg)
output_folder = "training-slides"
total_slides = 100
file_extension = "png"  # Change to "jpg" if your files use .jpg

items = []
for i in range(1, total_slides + 1):
    active = " active" if i == 1 else ""
    items.append(
        f'<div class="carousel-item{active}">\n'
        f'<img src="{output_folder}/slide-{i:02d}.{file_extension}" class="d-block w-100" alt="Slide {i}">\n'
        f'</div>'
    )

html_content = f"""<style>
#habcamSlideCarousel {{
position: relative;
max-width: 850px;
margin: 0 auto;
border: 1px solid #ddd;
border-radius: 8px;
padding: 10px;
background: #f9f9f9;
}}
#habcamSlideCarousel:fullscreen,
#habcamSlideCarousel:-webkit-full-screen {{
width: 100vw !important;
height: 100vh !important;
max-width: 100% !important;
background-color: #000 !important;
padding: 0 !important;
border: none !important;
margin: 0 !important;
}}
#habcamSlideCarousel:fullscreen .carousel-item.active,
#habcamSlideCarousel:-webkit-full-screen .carousel-item.active {{
height: 100vh;
display: flex !important;
align-items: center;
justify-content: center;
}}
#habcamSlideCarousel:fullscreen .carousel-item img,
#habcamSlideCarousel:-webkit-full-screen .carousel-item img {{
max-height: 90vh;
max-width: 95vw;
width: auto !important;
height: auto !important;
object-fit: contain;
}}
.fullscreen-toggle-btn {{
position: absolute;
top: 15px;
right: 15px;
z-index: 100;
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

<div id="habcamSlideCarousel" class="carousel slide" data-bs-ride="false">
<button type="button" class="fullscreen-toggle-btn" onclick="toggleCarouselFullscreen()">
⛶ Fullscreen
</button>
<div class="carousel-inner">
{"\n".join(items)}
</div>
<button class="carousel-control-prev" type="button" data-bs-target="#habcamSlideCarousel" data-bs-slide="prev">
<span class="carousel-control-prev-icon" aria-hidden="true" style="filter: invert(1);"></span>
<span class="visually-hidden">Previous</span>
</button>
<button class="carousel-control-next" type="button" data-bs-target="#habcamSlideCarousel" data-bs-slide="next">
<span class="carousel-control-next-icon" aria-hidden="true" style="filter: invert(1);"></span>
<span class="visually-hidden">Next</span>
</button>
</div>

<script>
function toggleCarouselFullscreen() {{
const carousel = document.getElementById('habcamSlideCarousel');
if (!document.fullscreenElement && !document.webkitFullscreenElement) {{
if (carousel.requestFullscreen) {{
carousel.requestFullscreen();
}} else if (carousel.webkitRequestFullscreen) {{
carousel.webkitRequestFullscreen();
}}
}} else {{
if (document.exitFullscreen) {{
document.exitFullscreen();
}} else if (document.webkitExitFullscreen) {{
document.webkitExitFullscreen();
}}
}}
}}
</script>"""

with open("training-carousel.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Created 'training-carousel.html' with 0 indentation spaces!")
