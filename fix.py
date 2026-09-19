import os
import shutil

# Target workspace directory paths configuration matrices
repo_root = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy"
content_dir = os.path.join(repo_root, "content")
output_dir = os.path.join(repo_root, "prof")

# Subdirectory tracks mapper profiles
bios_dir = os.path.join(content_dir, "Project Pentalogy", "Characters", "Bios")
art_dir = os.path.join(content_dir, "Project Pentalogy", "Characters", "Art")
supp_dir = os.path.join(content_dir, "Project Pentalogy", "Supplementary Items")

# Fallback structure mappings check pass
if not os.path.exists(bios_dir):
    bios_dir = os.path.join(content_dir, "characters", "bios")
    art_dir = os.path.join(content_dir, "characters", "art")
    supp_dir = os.path.join(content_dir, "Supplementary Items")
if not os.path.exists(supp_dir):
    supp_dir = os.path.join(content_dir, "supplementary items")

print("Initializing Upgraded Python Multi-Category Dossier Compiler Pass...")

# Deep refresh output directory structures
if os.path.exists(output_dir):
    try:
        shutil.rmtree(output_dir)
    except Exception:
        pass
os.makedirs(output_dir, exist_ok=True)

# Generate comprehensive style layout blocks mapping your typewriter ledger theme overrides
global_css = """
body {
  background-color: #f2ebd9;
  color: #3d2d1e;
  font-family: 'Courier Prime', Courier, monospace;
  margin: 0;
  padding: 0;
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
.sidebar { position: fixed; left: 0; top: 0; bottom: 0; width: 280px; background: #dfd2b5; padding: 25px; overflow-y: auto; border-right: 2px solid #a89470; box-sizing: border-box; }
.sidebar h2 { font-size: 1.4rem; margin-bottom: 5px; }
.sidebar h3 { font-size: 1rem; margin-top: 25px; margin-bottom: 10px; border-bottom: 1px solid #a89470; padding-bottom: 3px; color: #704829; }
.sidebar ul { padding-left: 15px; line-height: 1.8; list-style-type: square; margin-top: 5px; }
.main-content { margin-left: 320px; max-width: 850px; padding: 40px; box-sizing: border-box; }
.profile-header-box { display: flex; gap: 25px; align-items: stretch; margin-bottom: 30px; flex-wrap: wrap; }
.profile-thumbnail-panel { flex: 0 0 220px; display: flex; }
.profile-badge-img { width: 100%; height: 250px; object-fit: cover; border-radius: 6px; border: 2px solid #dfd2b5; box-shadow: 0 4px 8px rgba(0,0,0,0.08); background: #faf9f6; }
.profile-info-panel { flex: 1; min-width: 280px; display: flex; flex-direction: column; justify-content: center; }
.profile-info-panel ul { list-style-type: square; padding-left: 20px; margin: 0; }
.carousel-container { max-width: 100%; position: relative; margin: 30px auto; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.15); background: #1c1610; display: flex; align-items: center; justify-content: center; min-height: 350px; }
.mySlides { display: none; width: 100%; padding: 15px; box-sizing: border-box; text-align: center; }
.mySlides img { max-height: 500px; max-width: 100%; object-fit: contain; }
.carousel-btn { cursor: pointer; position: absolute; top: 50%; width: auto; padding: 16px; margin-top: -22px; color: #ebdcc8; font-weight: bold; font-size: 18px; transition: 0.6s ease; border-radius: 0 3px 3px 0; user-select: none; background: rgba(43,30,19,0.5); border: none; }
.carousel-btn:hover { background-color: rgba(112,72,41,0.8); }
.prev-btn { left: 0; border-radius: 3px 0 0 3px; }
.next-btn { right: 0; border-radius: 0 3px 3px 0; }
.slide-caption { color: #ebdcc8; font-size: 0.85rem; padding: 8px 12px; position: absolute; bottom: 0; left: 0; right: 0; background: rgba(0,0,0,0.6); }
details { background: #dfd2b5; padding: 15px; border-radius: 6px; margin: 20px 0; border-left: 5px solid #704829; }
summary { font-weight: bold; cursor: pointer; }
"""

with open(os.path.join(output_dir, "style.css"), "w", encoding="utf-8") as f:
    f.write(global_css)

# Natively map sidebar index components
character_links_html = ""
character_files = [f for f in os.listdir(bios_dir) if f.endswith(".md")] if os.path.exists(bios_dir) else []
for char_file in sorted(character_files):
    char_name = os.path.splitext(char_file)[0].capitalize()
    character_links_html += f'    <li><a href="{os.path.splitext(char_file)[0].lower()}.html">{char_name}</a></li>\\n'

supp_sections_html = ""
if os.path.exists(supp_dir):
    for folder in sorted(os.listdir(supp_dir)):
        folder_path = os.path.join(supp_dir, folder)
        if os.path.isdir(folder_path):
            supp_files = [f for f in os.listdir(folder_path) if f.endswith(".md")]
            if supp_files:
                supp_sections_html += f"  <h3>{folder.upper()}</h3>\\n  <ul>\\n"
                for s_file in sorted(supp_files):
                    file_clean_name = os.path.splitext(s_file)[0]
                    supp_sections_html += f'    <li><a href="supp_{folder.lower()}_{file_clean_name.lower()}.html">{file_clean_name.capitalize()}</a></li>\\n'
                supp_sections_html += "  </ul>\\n"

def generate_html_scaffold(title, body_content, sidebar_chars, sidebar_supp):
    return f"""<!DOCTYPE html>
<html>
<head>
  <title>{title} - Project Archive</title>
  <link rel="stylesheet" href="style.css">
  <link href="https://googleapis.com" rel="stylesheet">
</head>
<body>

<div class="sidebar">
  <h2 style="margin-top:0;"><a href="index.html" style="color:#2b1e13;">Project Pentalogy</a></h2>
  <p style="font-size:0.75rem; color:#704829; letter-spacing:1px; margin-top:0;"><b>SYSTEM DOSSIER LOCK</b></p>
  
  <h3>SUBJECT PROFILES</h3>
  <ul style="list-style-type: none; padding-left: 5px;">
{sidebar_chars}  </ul>
  
{sidebar_supp}</div>

<div class="main-content">
{body_content}</div>

</body>
</html>
"""
# Compile Subject Records
print(f"Compiling {len(character_files)} Character profiles into manual carousel formats...")
for file in character_files:
    file_clean_name = os.path.splitext(file)[0]
    character_title = file_clean_name.capitalize()
    
    with open(os.path.join(bios_dir, file), 'r', encoding='utf-8', errors='ignore') as f:
        body = f.read()
        
    if body.startswith("---"):
        parts = body.split("---", 2)
        if len(parts) >= 3: body = parts[2].strip()

    # Image slider builder setup
    char_art_folder = os.path.join(art_dir, file_clean_name.lower())
    image_slides_html = ""
    thumbnail_src = "https://placehold.co"
    
    if os.path.exists(char_art_folder) and os.path.isdir(char_art_folder):
        valid_exts = (".png", ".jpg", ".jpeg", ".webp", ".gif")
        all_imgs = os.listdir(char_art_folder)
        target_art_dest = os.path.join(output_dir, "Art", file_clean_name.lower())
        os.makedirs(target_art_dest, exist_ok=True)
        
        for img in all_imgs:
            if img.lower().endswith(valid_exts):
                shutil.copy(os.path.join(char_art_folder, img), os.path.join(target_art_dest, img))
                if os.path.splitext(img)[0].lower() == "thumbnail":
                    thumbnail_src = f"Art/{file_clean_name.lower()}/{img}"
                    
        slide_imgs = [i for i in all_imgs if i.lower().endswith(valid_exts) and os.path.splitext(i)[0].lower() != "thumbnail"]
        for idx, img_name in enumerate(slide_imgs):
            image_slides_html += f'    <div class="mySlides fade"><img src="Art/{file_clean_name.lower()}/{img_name}"><div class="slide-caption">DOCUMENT ATTACHMENT {idx+1}/{len(slide_imgs)}: {img_name}</div></div>\\n'

    if not image_slides_html:
        image_slides_html = '    <div class="mySlides fade" style="display:block; color:#ebdcc8;"><p style="padding:40px;">No supplementary visual evidence cataloged.</p></div>'

    # Filter out duplicate overview listings inside markdown strings
    clean_paragraphs = ""
    skip_mode = False
    for line in body.split("\n"):
        if "Basic Overview" in line or "### Overview" in line:
            skip_mode = True 
            continue
        if skip_mode and line.strip().startswith("#"):
            skip_mode = False 
        if not skip_mode and line.strip() and not line.strip().startswith("*"):
            clean_paragraphs += f"    <p>{line.strip()}</p>\\n"

    # Assemble your beautiful complete old dossier document screen blueprint
    char_content_html = f"""  <h1>{character_title.upper()}</h1>
  
  <div class="profile-header-box">
    <div class="profile-thumbnail-panel">
      <img src="{thumbnail_src}" class="profile-badge-img" onerror="this.src='https://placehold.co'">
    </div>
    <div class="profile-info-panel">
      <h3>Basic Overview</h3>
      <ul style="padding-left:15px; margin:0;">
        <li><b>Age:</b> Case File Record Locked</li>
        <li><b>Gender:</b> Classified</li>
        <li><b>Sexuality:</b> Documented</li>
        <li><b>Height:</b> Measured</li>
        <li><b>Trope/s:</b> Logged</li>
        <li><b>Motifs / Symbols:</b> Filed</li>
      </ul>
    </div>
  </div>

  <h3>Visual Evidence Gallery</h3>
  <div class="carousel-container">
    <button class="carousel-btn prev-btn" onclick="plusSlides(-1)">&#10094;</button>
    {image_slides_html}    <button class="carousel-btn next-btn" onclick="plusSlides(1)">&#10095;</button>
  </div>

  <h3>Dossier Logs & Transcripts</h3>
  <details open>
    <summary><b>Log Text Ledger</b></summary>
    <div style="padding-top:10px;">
{clean_paragraphs}    </div>
  </details>

<script>
  let slideIndex = 1;
  showSlides(slideIndex);
  function plusSlides(n) {{ showSlides(slideIndex += n); }}
  function showSlides(n) {{
    let i;
    let slides = document.getElementsByClassName("mySlides");
    if (slides.length === 0) return;
    if (n > slides.length) {{slideIndex = 1}}    
    if (n < 1) {{slideIndex = slides.length}}
    for (i = 0; i < slides.length; i++) {{ slides[i].style.display = "none"; }}
    slides[slideIndex-1].style.display = "block";  
  }}
</script>
"""
    full_char_page = generate_html_scaffold(character_title, char_content_html, character_links_html, supp_sections_html)
    with open(os.path.join(output_dir, f"{file_clean_name.lower()}.html"), "w", encoding="utf-8") as f:
        f.write(full_char_page)

# Compile Supplementary Case Files
if os.path.exists(supp_dir):
    print("Compiling supplementary world logs and text items...")
    for folder in os.listdir(supp_dir):
        folder_path = os.path.join(supp_dir, folder)
        if os.path.isdir(folder_path):
            for s_file in os.listdir(folder_path):
                if s_file.endswith(".md"):
                    file_clean = os.path.splitext(s_file)[0]
                    with open(os.path.join(folder_path, s_file), 'r', encoding='utf-8', errors='ignore') as f:
                        s_body = f.read()
                    if s_body.startswith("---"):
                        s_parts = s_body.split("---", 2)
                        if len(s_parts) >= 3: s_body = s_parts[2].strip()
                    
                    s_paragraphs = "".join([f"  <p>{line.strip()}</p>\\n" for line in s_body.split("\n") if line.strip()])
                    supp_content_html = f"  <h1>{file_clean.upper()}</h1>\\n  <h3>Archive Reference: {folder.upper()}</h3>\\n  <div style='margin-top:20px;'>\\n{s_paragraphs}  </div>"
                    full_supp_page = generate_html_scaffold(file_clean, supp_content_html, character_links_html, supp_sections_html)
                    with open(os.path.join(output_dir, f"supp_{folder.lower()}_{file_clean.lower()}.html"), "w", encoding="utf-8") as f:
                        f.write(full_supp_page)

# Generate automated master landing index file page configuration setups
if character_files:
    first_char_name = os.path.splitext(sorted(character_files)[0])[0].lower()
    shutil.copy(os.path.join(output_dir, f"{first_char_name}.html"), os.path.join(output_dir, "index.html"))

print("\\nCompilation Complete! Cleaned files saved out successfully.")
