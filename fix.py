import os
import shutil

# Target directory paths
repo_root = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy"
bios_dir = os.path.join(repo_root, "content", "Project Pentalogy", "Characters", "Bios")
art_dir = os.path.join(repo_root, "content", "Project Pentalogy", "Characters", "Art")
output_dir = os.path.join(repo_root, "prof") # Matches your target site output folder name

print("Initializing Pure Python Static Compilation Pass...")

if not os.path.exists(bios_dir):
    # Fallback to flattened content structure if moved
    bios_dir = os.path.join(repo_root, "content", "characters", "bios")
    art_dir = os.path.join(repo_root, "content", "characters", "art")

if not os.path.exists(bios_dir):
    print("Error: Could not locate your character files directory.")
    exit()

# Refresh the compiled output directory
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)

# Generate global style variables mapping your vintage beige manila folder theme
global_css = """
body {
  background-color: #f2ebd9;
  color: #3d2d1e;
  font-family: 'Courier Prime', Courier, monospace;
  margin: 0;
  padding: 40px;
  line-height: 1.6;
}
h1, h2, h3 {
  font-family: 'Special Elite', Impact, sans-serif;
  color: #2b1e13;
  border-bottom: 2px solid #dfd2b5;
  padding-bottom: 8px;
}
a { color: #704829; text-decoration: none; font-weight: bold; }
a:hover { text-decoration: underline; }
.profile-header-box { display: flex; gap: 25px; align-items: stretch; margin-bottom: 30px; flex-wrap: wrap; }
.profile-thumbnail-panel { flex: 0 0 220px; display: flex; }
.profile-badge-img { width: 100%; height: 250px; object-fit: cover; border-radius: 6px; border: 2px solid #dfd2b5; box-shadow: 0 4px 8px rgba(0,0,0,0.08); background: #faf9f6; }
.profile-info-panel { flex: 1; min-width: 280px; display: flex; flex-direction: column; justify-content: center; }
.profile-info-panel ul { list-style-type: square; padding-left: 20px; margin: 0; }
.slideshow-container { max-width: 100%; position: relative; margin: 30px auto; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.15); background: #1c1610; text-align: center; }
.mySlides { display: none; padding: 10px; }
.mySlides img { max-height: 500px; max-width: 100%; object-fit: contain; }
.fade { animation-name: fade; animation-duration: 1.5s; }
@keyframes fade { from {opacity: .4} to {opacity: 1} }
details { background: #dfd2b5; padding: 15px; border-radius: 6px; margin: 20px 0; border-left: 5px solid #704829; }
summary { font-weight: bold; cursor: pointer; }
.sidebar { position: fixed; left: 0; top: 0; bottom: 0; width: 260px; background: #dfd2b5; padding: 20px; overflow-y: auto; border-right: 2px solid #a89470; }
.main-content { margin-left: 290px; max-width: 800px; }
"""

# Copy style sheets down
with open(os.path.join(output_dir, "style.css"), "w", encoding="utf-8") as f:
    f.write(global_css)

# Gather character listings to build your automated Explorer sidebar menu list natively
character_files = [f for f in os.listdir(bios_dir) if f.endswith(".md")]
sidebar_links_html = ""
for char_file in sorted(character_files):
    char_name = os.path.splitext(char_file)[0].capitalize() # Fixed: Grab first element of the tuple
    html_link_name = os.path.splitext(char_file)[0] + ".html"
    sidebar_links_html += f'<li><a href="{html_link_name}">{char_name}</a></li>\n'

print(f"Compiling {len(character_files)} Case Files into responsive HTML layouts...")

# Process each note card
for file in character_files:
    file_path = os.path.join(bios_dir, file)
    character_key = os.path.splitext(file)[0].lower()
    character_title = os.path.splitext(file)[0].capitalize()
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            body_content = f.read()
    except Exception:
        with open(file_path, 'r', encoding='cp1252') as f:
            body_content = f.read()
            
    # Scrub frontmatter tags safely
    if body_content.startswith("---"):
        parts = body_content.split("---", 2)
        if len(parts) >= 3:
            body_content = parts[2].strip()

    # Track thumbnails and gallery components inside the local hard drive folders
    char_art_folder = os.path.join(art_dir, character_key)
    image_slides_html = ""
    thumbnail_src = "https://placehold.co"
    
    if os.path.exists(char_art_folder) and os.path.isdir(char_art_folder):
        valid_extensions = (".png", ".jpg", ".jpeg", ".webp", ".gif")
        all_files = os.listdir(char_art_folder)
        
        # Copy the physical images over to the output directory so the browser can see them
        target_art_dest = os.path.join(output_dir, "Art", character_key)
        os.makedirs(target_art_dest, exist_ok=True)
        for img in all_files:
            if img.lower().endswith(valid_extensions):
                shutil.copy(os.path.join(char_art_folder, img), os.path.join(target_art_dest, img))
        
        for f_name in all_files:
            if os.path.splitext(f_name)[0].lower() == "thumbnail" and f_name.lower().endswith(valid_extensions):
                thumbnail_src = f"Art/{character_key}/{f_name}"
                break
                
        images = [img for img in all_files if img.lower().endswith(valid_extensions) and not os.path.splitext(img)[0].lower() == "thumbnail"]
        for idx, img_name in enumerate(images):
            image_slides_html += f'<div class="mySlides fade"><img src="Art/{character_key}/{img_name}"></div>\n'

    if not image_slides_html:
        image_slides_html = '<div class="mySlides fade" style="display:block; color:#ebdcc8; padding: 40px;"><p>No archive gallery items uploaded.</p></div>'

    # Format line breaks to display as paragraph blocks cleanly
    formatted_paragraphs = ""
    for line in body_content.split("\n"):
        if line.strip().startswith("*"):
            continue # Skip default stats template lines as they are handled in the badge panel
        if line.strip():
            formatted_paragraphs += f"<p>{line.strip()}</p>\n"

    # Assemble your beautiful complete old dossier document screen blueprint
    html_blueprint = f"""<!DOCTYPE html>
<html>
<head>
  <title>{character_title} - Archive File</title>
  <link rel="stylesheet" href="style.css">
  <link href="https://googleapis.com" rel="stylesheet">
</head>
<body>

<div class="sidebar">
  <h2 style="margin-top:0;">Project Pentalogy</h2>
  <p style="font-size:0.8rem; color:#704829;"><b>ARCHIVAL RECORDS</b></p>
  <ul style="padding-left:15px; line-height:1.8;">
    {sidebar_links_html}
  </ul>
</div>

<div class="main-content">
  <h1>FILE RECORD: {character_title.upper()}</h1>
  
  <div class="profile-header-box">
    <div class="profile-thumbnail-panel">
      <img src="{thumbnail_src}" class="profile-badge-img" onerror="this.src='https://placehold.co'">
    </div>
    <div class="profile-info-panel">
      <h3>Basic Overview</h3>
      <ul>
        <li><b>Age:</b> Case File Record Locked</li>
        <li><b>Gender:</b> Classified</li>
        <li><b>Sexuality:</b> Documented</li>
        <li><b>Height:</b> Measured</li>
        <li><b>Trope/s:</b> Logged</li>
        <li><b>Motifs / Symbols:</b> Filed</li>
      </ul>
    </div>
  </div>

  <h3>Character Artwork</h3>
  <div class="slideshow-container">
    {image_slides_html}
  </div>

  <h3>Backstory & Log Details</h3>
  <details open>
    <summary><b>Dossier Transcript Body Text</b></summary>
    {formatted_paragraphs}
  </details>
</div>

<script>
  let slideIndex = 0;
  function showSlides() {{
    let slides = document.getElementsByClassName("mySlides");
    if (slides.length === 0) return;
    for (let i = 0; i < slides.length; i++) {{ slides[i].style.display = "none"; }}
    slideIndex++;
    if (slideIndex > slides.length) {{slideIndex = 1}}    
    slides[slideIndex-1].style.display = "block";  
    setTimeout(showSlides, 3000);
  }}
  showSlides();
</script>

</body>
</html>
"""
    
    # Save the polished HTML page directly out
    output_html_path = os.path.join(output_dir, f"{character_key}.html")
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html_blueprint)

# Generate an elegant master landing file index page automatically from the first sorted entry
first_char_key = os.path.splitext(sorted(character_files)[0])[0].lower()
shutil.copy(os.path.join(output_dir, f"{first_char_key}.html"), os.path.join(output_dir, "index.html"))

print(f"\nCompilation Success! Open your local folder path to view your completed website: {output_dir}")
