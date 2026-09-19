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

print("Initializing Vintage Photograph Upgrade Pass...")

# Deep refresh output directory structures safely
if os.path.exists(output_dir):
    try:
        shutil.rmtree(output_dir)
    except Exception:
        pass
os.makedirs(output_dir, exist_ok=True)

# Generate card stacking styling profiles with aged polaroid textures
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
.profile-badge-img { width: 100%; height: 250px; object-fit: cover; border-radius: 4px; border: 2px solid #dfd2b5; box-shadow: 0 4px 8px rgba(0,0,0,0.08); background: #faf9f6; }
.profile-info-panel { flex: 1; min-width: 280px; display: flex; flex-direction: column; justify-content: center; }
.profile-info-panel ul { list-style-type: square; padding-left: 20px; margin: 0; }

/* The Dark File Case Background Wrapper Box */
.carousel-container { max-width: 100%; position: relative; margin: 30px auto; border-radius: 8px; height: 560px; background: #1c1610; display: flex; align-items: center; justify-content: center; overflow: hidden; box-shadow: inset 0 0 20px rgba(0,0,0,0.8), 0 10px 25px rgba(0,0,0,0.3); }

/* The Aged Polaroid Photograph Frame Box Element */
.mySlides { 
  display: none; 
  position: absolute; 
  width: auto;
  max-width: 85%;
  height: 90%; 
  background: #f4edd3; /* Aged photo paper cream color */
  border-radius: 2px; 
  padding: 15px 15px 55px 15px; /* Thicker bottom border padding for the polaroid signature shelf label */
  box-sizing: border-box; 
  text-align: center; 
  border: 1px solid #d4cbb3;
  box-shadow: 0 8px 20px rgba(0,0,0,0.4), 0 2px 5px rgba(0,0,0,0.3); 
  transition: transform 0.5s cubic-bezier(0.25, 1, 0.5, 1);
}
.mySlides img { 
  height: 100%; 
  max-width: 100%; 
  object-fit: contain; 
  border: 2px solid #2b1e13; /* Thin black border directly hugging the photograph edges */
  box-sizing: border-box;
}

/* Microscopic Typewriter Image File Name Captions Style */
.slide-caption { 
  color: #3d2d1e; 
  font-size: 0.7rem; /* Significantly shrunk to small text */
  font-weight: bold; 
  margin-top: 12px; 
  font-family: 'Courier Prime', monospace; 
  letter-spacing: 0.5px;
  opacity: 0.8;
  text-transform: lowercase;
}

/* Fixed Overlap Stack Sliding Animation Rules Mapping */
.slide-out-back { animation: slideBack 0.55s cubic-bezier(0.25, 1, 0.5, 1) forwards; }
@keyframes slideBack {
  0% { transform: translateX(0) scale(1); z-index: 10; opacity: 1; }
  50% { transform: translateX(-110%) scale(0.96); z-index: 10; opacity: 1; }
  51% { z-index: 1; }
  100% { transform: translateX(0) scale(0.92); z-index: 1; opacity: 0; } /* Completely fades out opacity at the end to prevent asset overlaps */
}
.active-card { display: block; z-index: 5; transform: scale(1); opacity: 1; }
.background-card { display: block; z-index: 2; transform: scale(0.96) translateY(8px); opacity: 0.4; } /* Keeps underlying cards faded out until active step takes over */

.carousel-btn { cursor: pointer; position: absolute; top: 50%; width: auto; padding: 16px; margin-top: -22px; color: #ebdcc8; font-weight: bold; font-size: 18px; transition: 0.3s; border-radius: 4px; user-select: none; background: rgba(43,30,19,0.7); border: none; z-index: 20; }
.carousel-btn:hover { background-color: rgba(112,72,41,0.9); }
.prev-btn { left: 10px; }
.next-btn { right: 10px; }
details { background: #dfd2b5; padding: 15px; border-radius: 6px; margin: 20px 0; border-left: 5px solid #704829; }
summary { font-weight: bold; cursor: pointer; }
"""

with open(os.path.join(output_dir, "style.css"), "w", encoding="utf-8") as f:
    f.write(global_css)

# Generate sidebar listings
character_links_html = ""
character_files = [f for f in os.listdir(bios_dir) if f.endswith(".md")] if os.path.exists(bios_dir) else []
for char_file in sorted(character_files):
    c_name = os.path.splitext(char_file)[0]
    character_links_html += f'    <li><a href="{c_name.lower()}.html">{c_name}</a></li>\n'

supp_sections_html = ""
if os.path.exists(supp_dir):
    for folder in sorted(os.listdir(supp_dir)):
        folder_path = os.path.join(supp_dir, folder)
        if os.path.isdir(folder_path):
            supp_files = [f for f in os.listdir(folder_path) if f.endswith(".md")]
            if supp_files:
                supp_sections_html += f"  <h3>{folder.upper()}</h3>\n  <ul>\n"
                for s_file in sorted(supp_files):
                    sf_name = os.path.splitext(s_file)[0]
                    supp_sections_html += f'    <li><a href="supp_{folder.lower()}_{sf_name.lower()}.html">{sf_name}</a></li>\n'
                supp_sections_html += "  </ul>\n"

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
  <ul style="list-style-type: none; padding-left: 5px; margin: 0;">
{sidebar_chars}  </ul>
  
{sidebar_supp}</div>

<div class="main-content">
{body_content}</div>

</body>
</html>
"""
# Compile Subject Records
print(f"Compiling {len(character_files)} Character profiles into polaroid stack models...")
for file in character_files:
    file_clean_name = os.path.splitext(file)[0]
    character_title = file_clean_name
    
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
            # Fixed: Truncated caption HTML string to strictly output your plain image filename in micro layout sizes
            image_slides_html += f'    <div class="mySlides"><img src="Art/{file_clean_name.lower()}/{img_name}"><div class="slide-caption">{img_name}</div></div>\n'

    if not image_slides_html:
        image_slides_html = '    <div class="mySlides" style="display:block;"><p style="padding:40px; color:#3d2d1e;">No archive photograph attachments cataloged.</p></div>'

    # Backstory Text Builder Loader Matrix Loop
    clean_paragraphs = ""
    for line in body.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("---") or stripped.startswith("*"):
            continue
        if "Basic Overview" in line or "### Overview" in line or "Character Artwork" in line or "###" in line:
            continue 
        clean_paragraphs += f"    <p>{stripped}</p>\n"

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

  <h3>Visual Evidence Gallery (Polaroid Stack Layout)</h3>
  <div class="carousel-container">
    <button class="carousel-btn prev-btn" onclick="moveCard(-1)">&#10094;</button>
{image_slides_html}    <button class="carousel-btn next-btn" onclick="moveCard(1)">&#10095;</button>
  </div>

  <h3>Dossier Logs & Transcripts</h3>
  <details open>
    <summary><b>Log Text Ledger</b></summary>
    <div style="padding:15px 5px 5px 5px;">
{clean_paragraphs}    </div>
  </details>

<script>
  let currentIdx = 0;
  let cards = [];
  
  function initCarousel() {{
    const allCards = document.getElementsByClassName("mySlides");
    // Filter out mock empty sliders if present
    for(let i=0; i<allCards.length; i++) {{ cards.push(allCards[i]); }}
    if (cards.length === 0) return;
    updateCardStack();
  }}
  
  function moveCard(direction) {{
    if (cards.length <= 1) return;
    
    let oldCard = cards[currentIdx];
    
    if (direction === 1) {{
      // Move to back card sliding effect animation
      oldCard.classList.add("slide-out-back");
      setTimeout(() => {{
        oldCard.classList.remove("slide-out-back");
        currentIdx = (currentIdx + 1) % cards.length;
        updateCardStack();
      }}, 500);
    }} else {{
      // Infinite reverse stack wrap pass loop
      currentIdx = (currentIdx - 1 + cards.length) % cards.length;
      updateCardStack();
    }}
  }}
  
  function updateCardStack() {{
    for (let i = 0; i < cards.length; i++) {{
      cards[i].className = "mySlides";
      cards[i].style.display = "none";
    }}
    
    // Core active presentation card assignment
    cards[currentIdx].style.display = "block";
    cards[currentIdx].classList.add("active-card");
    
    // Safe stack alignment depth check pass to overlay background layers perfectly
    if (cards.length > 1) {{
      let nextIdx = (currentIdx + 1) % cards.length;
      cards[nextIdx].style.display = "block";
      cards[nextIdx].classList.add("background-card");
    }}
  }}
  
  initCarousel();
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
                    sf_clean = os.path.splitext(s_file)[0]
                    with open(os.path.join(folder_path, s_file), 'r', encoding='utf-8', errors='ignore') as f:
                        s_body = f.read()
                    if s_body.startswith("---"):
                        s_parts = s_body.split("---", 2)
                        if len(s_parts) >= 3: s_body = s_parts[2].strip()
                    
                    s_paragraphs = "".join([f"  <p>{line.strip()}</p>\n" for line in s_body.split("\n") if line.strip() and not line.strip().startswith("---")])
                    supp_content_html = f"  <h1>{sf_clean.upper()}</h1>\n  <h3>Archive Reference: {folder.upper()}</h3>\n  <div style='margin-top:20px;'>\n{s_paragraphs}  </div>"
                    full_supp_page = generate_html_scaffold(sf_clean, supp_content_html, character_links_html, supp_sections_html)
                    with open(os.path.join(output_dir, f"supp_{folder.lower()}_{sf_clean.lower()}.html"), "w", encoding="utf-8") as f:
                        f.write(full_supp_page)

# Generate master index page setup from first character profile page map node
if character_files:
    first_char_name = os.path.splitext(sorted(character_files)[0])[0].lower()
    shutil.copy(os.path.join(output_dir, f"{first_char_name}.html"), os.path.join(output_dir, "index.html"))

print("\nCompilation Complete! Cleaned files saved out successfully.")
