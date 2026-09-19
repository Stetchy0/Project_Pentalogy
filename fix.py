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

print("Initializing Relational Network Node Graph Code Update...")

# Deep refresh output directory structures safely
if os.path.exists(output_dir):
    try:
        shutil.rmtree(output_dir)
    except Exception:
        pass
os.makedirs(output_dir, exist_ok=True)

# Generate card stacking styling profiles with aged polaroid textures and canvas graphs
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
.carousel-container { max-width: 100%; position: relative; margin: 15px auto 30px auto; border-radius: 8px; height: 560px; background: #1c1610; display: flex; align-items: center; justify-content: center; overflow: hidden; box-shadow: inset 0 0 20px rgba(0,0,0,0.8), 0 10px 25px rgba(0,0,0,0.3); }

/* The Aged Polaroid Photograph Frame Box Element */
.mySlides { 
  display: none; 
  position: absolute; 
  width: auto;
  max-width: 85%;
  height: 90%; 
  background: #f4edd3; 
  border-radius: 2px; 
  padding: 15px 15px 55px 15px; 
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
  border: 2px solid #2b1e13; 
  box-sizing: border-box;
}

.slide-caption { 
  color: #3d2d1e; 
  font-size: 0.7rem; 
  font-weight: bold; 
  margin-top: 12px; 
  font-family: 'Courier Prime', monospace; 
  letter-spacing: 0.5px;
  opacity: 0.8;
  text-transform: lowercase;
}

.slide-out-back { animation: slideBack 0.55s cubic-bezier(0.25, 1, 0.5, 1) forwards; }
@keyframes slideBack {
  0% { transform: translateX(0) scale(1); z-index: 10; opacity: 1; }
  50% { transform: translateX(-110%) scale(0.96); z-index: 10; opacity: 1; }
  51% { z-index: 1; }
  100% { transform: translateX(0) scale(0.92); z-index: 1; opacity: 0; }
}
.active-card { display: block; z-index: 5; transform: scale(1); opacity: 1; }
.background-card { display: block; z-index: 2; transform: scale(0.96) translateY(8px); opacity: 0.4; }

.carousel-btn { cursor: pointer; position: absolute; top: 50%; width: auto; padding: 16px; margin-top: -22px; color: #ebdcc8; font-weight: bold; font-size: 18px; transition: 0.3s; border-radius: 4px; user-select: none; background: rgba(43,30,19,0.7); border: none; z-index: 20; }
.carousel-btn:hover { background-color: rgba(112,72,41,0.9); }
.prev-btn { left: 10px; }
.next-btn { right: 10px; }

/* Expanded Markdown Content Box Layout Variables */
details { background: #dfd2b5; padding: 15px; border-radius: 6px; margin: 15px 0; border-left: 5px solid #704829; }
summary { font-weight: bold; cursor: pointer; font-size: 1.05rem; }

/* Obsidian Node Graph Box Structures */
.graph-wrapper-box { position: relative; width: 100%; height: 400px; background: #1c1610; border-radius: 8px; border: 2px solid #a89470; margin-top: 30px; overflow: hidden; box-shadow: 0 6px 15px rgba(0,0,0,0.15); }
#network-canvas { width: 100%; height: 100%; cursor: grab; }
#network-canvas:active { cursor: grabbing; }

/* Relational Node Tooltip Floating Badges Styles */
.node-tooltip-card {
  position: absolute;
  display: none;
  background: #fdfaf7;
  color: #3d2d1e;
  border: 2px solid #704829;
  border-radius: 6px;
  padding: 12px;
  font-family: 'Courier Prime', monospace;
  font-size: 0.8rem;
  pointer-events: none;
  z-index: 100;
  box-shadow: 0 4px 15px rgba(0,0,0,0.25);
  width: 240px;
}
.tooltip-flex-row { display: flex; gap: 12px; align-items: center; }
.tooltip-thumb { width: 60px; height: 75px; object-fit: cover; border-radius: 3px; border: 1px solid #dfd2b5; background: #faf9f6; }
.tooltip-info { flex: 1; }
.tooltip-title { font-family: 'Special Elite', sans-serif; font-size: 0.95rem; margin: 0 0 4px 0; color: #2b1e13; border-bottom: 1px solid #dfd2b5; }
"""

with open(os.path.join(output_dir, "style.css"), "w", encoding="utf-8") as f:
    f.write(global_css)

# Generate sidebar listings
character_links_html = ""
character_files = [f for f in os.listdir(bios_dir) if f.endswith(".md")] if os.path.exists(bios_dir) else []
for char_file in sorted(character_files):
    c_name = os.path.splitext(char_file)[0]
    character_links_html += f'    <li><a href="{c_name.lower()}.html">{c_name.capitalize()}</a></li>\n'

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
                    supp_sections_html += f'    <li><a href="supp_{folder.lower()}_{sf_name.lower()}.html">{sf_name.capitalize()}</a></li>\n'
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
import json

# Master Relational Network Dataset Definition Dictionary Map Matrix
master_relationships_map = {
    "abaddon": [
        {"target": "alex", "relation": "Abaddon's torch", "thumb": "Art/alex/thumbnail.png"},
        {"target": "mephisto", "relation": "Opposing force", "thumb": "Art/mephisto/thumbnail.png"}
    ],
    "alex": [
        {"target": "abaddon", "relation": "Guiding light", "thumb": "Art/abaddon/thumbnail.png"}
    ],
    "mephisto": [
        {"target": "abaddon", "relation": "Opposing force", "thumb": "Art/abaddon/thumbnail.png"}
    ]
}

# Compile Subject Records
print(f"Compiling {len(character_files)} Character profiles into interactive node networks...")
for file in character_files:
    file_clean_name = os.path.splitext(file)[0]
    character_key = file_clean_name.lower()
    character_title = file_clean_name.capitalize()
    
    with open(os.path.join(bios_dir, file), 'r', encoding='utf-8', errors='ignore') as f:
        body = f.read()
        
    if body.startswith("---"):
        parts = body.split("---", 2)
        if len(parts) >= 3: body = parts[2].strip()

    # Image slider builder setup
    char_art_folder = os.path.join(art_dir, character_key)
    image_slides_html = ""
    thumbnail_src = "https://placehold.co"
    
    if os.path.exists(char_art_folder) and os.path.isdir(char_art_folder):
        valid_exts = (".png", ".jpg", ".jpeg", ".webp", ".gif")
        all_imgs = os.listdir(char_art_folder)
        target_art_dest = os.path.join(output_dir, "Art", character_key)
        os.makedirs(target_art_dest, exist_ok=True)
        
        for img in all_imgs:
            if img.lower().endswith(valid_exts):
                shutil.copy(os.path.join(char_art_folder, img), os.path.join(target_art_dest, img))
                if os.path.splitext(img)[0].lower() == "thumbnail":
                    thumbnail_src = f"Art/{character_key}/{img}"
                    
        slide_imgs = [i for i in all_imgs if i.lower().endswith(valid_exts) and os.path.splitext(i)[0].lower() != "thumbnail"]
        for idx, img_name in enumerate(slide_imgs):
            image_slides_html += f'    <div class="mySlides"><img src="Art/{character_key}/{img_name}"><div class="slide-caption">{img_name}</div></div>\\n'

    if not image_slides_html:
        image_slides_html = '    <div class="mySlides" style="display:block;"><p style="padding:40px; color:#3d2d1e;">No archive photograph attachments cataloged.</p></div>'

    # Extends lines to load inside your new Brief tldr blocks
    brief_paragraphs = "<p>No primary summary logged inside this profile ledger index.</p>"
    lines = body.split("\\n")
    for idx, line in enumerate(lines):
        if "tldr" in line.lower() or "summary" in line.lower() or "brief" in line.lower():
            if idx + 1 < len(lines) and lines[idx+1].strip():
                brief_paragraphs = f"<p>{lines[idx+1].strip()}</p>"
                break

    # Extract relational graph payload nodes specifically matching current target entity profile context
    local_relations = master_relationships_map.get(character_key, [])
    
    # Establish graph dataset structures to pass straight into JavaScript layer canvas renderers
    graph_nodes = [{"id": character_key, "label": character_title, "color": "#704829", "size": 14, "isRoot": True}]
    graph_edges = []
    
    for rel in local_relations:
        graph_nodes.append({
            "id": rel["target"],
            "label": rel["target"].capitalize(),
            "relation": rel["relation"],
            "thumb": rel["thumb"],
            "color": "#a89470",
            "size": 9,
            "isRoot": False
        })
        graph_edges.append({"source": character_key, "target": rel["target"]})
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

  <div class="carousel-container">
    <button class="carousel-btn prev-btn" onclick="moveCard(-1)">&#10094;</button>
{image_slides_html}    <button class="carousel-btn next-btn" onclick="moveCard(1)">&#10095;</button>
  </div>

  <details>
    <summary>Brief</summary>
    <div style="padding:10px 5px 5px 5px;">
      {brief_paragraphs}
    </div>
  </details>

  <details open>
    <summary>Dossier</summary>
    <div style="padding:10px 5px 5px 5px;">
      <p>Dossier logs recorded inside local character file templates structure.</p>
    </div>
  </details>

  <h3>Relational Connection Network (Obsidian Mode)</h3>
  <div class="graph-wrapper-box">
    <canvas id="network-canvas"></canvas>
    <div id="tooltip-modal" class="node-tooltip-card"></div>
  </div>

<script>
  let currentIdx = 0;
  let cards = [];
  
  function initCarousel() {{
    const allCards = document.getElementsByClassName("mySlides");
    for(let i=0; i<allCards.length; i++) {{ cards.push(allCards[i]); }}
    if (cards.length === 0) return;
    updateCardStack();
  }}
  
  function moveCard(direction) {{
    if (cards.length <= 1) return;
    let oldCard = cards[currentIdx];
    if (direction === 1) {{
      oldCard.classList.add("slide-out-back");
      setTimeout(() => {{
        oldCard.classList.remove("slide-out-back");
        currentIdx = (currentIdx + 1) % cards.length;
        updateCardStack();
      }}, 500);
    }} else {{
      currentIdx = (currentIdx - 1 + cards.length) % cards.length;
      updateCardStack();
    }}
  }}
  
  function updateCardStack() {{
    for (let i = 0; i < cards.length; i++) {{
      cards[i].className = "mySlides";
      cards[i].style.display = "none";
    }}
    cards[currentIdx].style.display = "block";
    cards[currentIdx].classList.add("active-card");
    if (cards.length > 1) {{
      let nextIdx = (currentIdx + 1) % cards.length;
      cards[nextIdx].style.display = "block";
      cards[nextIdx].classList.add("background-card");
    }}
  }}
  initCarousel();

  const canvas = document.getElementById("network-canvas");
  const ctx = canvas.getContext("2d");
  const tooltip = document.getElementById("tooltip-modal");
  
  const nodes = {json.dumps(graph_nodes)};
  const edges = {json.dumps(graph_edges)};
  
  function resizeCanvas() {{
    canvas.width = canvas.parentElement.clientWidth;
    canvas.height = canvas.parentElement.clientHeight;
  }}
  resizeCanvas();

  nodes.forEach((node, idx) => {{
    if (node.isRoot) {{
      node.x = canvas.width / 2;
      node.y = canvas.height / 2;
    }} else {{
      const angle = (idx * 2 * Math.PI) / (nodes.length - 1);
      node.x = canvas.width / 2 + 130 * Math.cos(angle);
      node.y = canvas.height / 2 + 130 * Math.sin(angle);
    }}
  }});

  function drawGraph() {{
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.strokeStyle = "rgba(168, 148, 112, 0.4)";
    ctx.lineWidth = 1.5;
    edges.forEach(edge => {{
      const srcNode = nodes.find(n => n.id === edge.source);
      const tgtNode = nodes.find(n => n.id === edge.target);
      if (srcNode && tgtNode) {{
        ctx.beginPath();
        ctx.moveTo(srcNode.x, srcNode.y);
        ctx.lineTo(tgtNode.x, tgtNode.y);
        ctx.stroke();
      }}
    }});

    nodes.forEach(node => {{
      ctx.beginPath();
      ctx.arc(node.x, node.y, node.size, 0, 2 * Math.PI);
      ctx.fillStyle = node.color;
      ctx.fill();
      ctx.strokeStyle = "#1c1610";
      ctx.lineWidth = 2;
      ctx.stroke();
      
      ctx.fillStyle = "#ded0bf";
      ctx.font = "bold 11px 'Courier Prime', monospace";
      ctx.textAlign = "center";
      ctx.fillText(node.label, node.x, node.y - node.size - 6);
    }});
  }}

  canvas.addEventListener("mousemove", (e) => {{
    const rect = canvas.getBoundingClientRect();
    const mouseX = e.clientX - rect.left;
    const mouseY = e.clientY - rect.top;
    let hoveredNode = null;

    nodes.forEach(node => {{
      const dist = Math.sqrt((mouseX - node.x)**2 + (mouseY - node.y)**2);
      if (dist <= node.size + 4) {{ hoveredNode = node; }}
    }});

    if (hoveredNode && !hoveredNode.isRoot) {{
      tooltip.style.display = "block";
      tooltip.style.left = (mouseX + 15) + "px";
      tooltip.style.top = (mouseY + 15) + "px";
      tooltip.innerHTML = `
        <div class="tooltip-flex-row">
          <img src="${{hoveredNode.thumb}}" class="tooltip-thumb" onerror="this.src='https://placehold.co'">
          <div class="tooltip-info">
            <h4 class="tooltip-title">${{hoveredNode.label}}</h4>
            <p style="margin:0; font-size:0.75rem; color:#704829;"><b>RELATION:</b></p>
            <p style="margin:0; font-size:0.75rem; font-style:italic;">"${{hoveredNode.relation}}"</p>
          </div>
        </div>
      `;
    }} else {{
      tooltip.style.display = "none";
    }}
  }});

  canvas.addEventListener("mouseleave", () => {{ tooltip.style.display = "none"; }});
  window.addEventListener("resize", () => {{ resizeCanvas(); drawGraph(); }});
  drawGraph();
</script>
"""
    full_char_page = generate_html_scaffold(character_title, char_content_html, character_links_html, supp_sections_html)
    with open(os.path.join(output_dir, f"{character_key}.html"), "w", encoding="utf-8") as f:
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
                    
                    s_paragraphs = "".join([f"  <p>{line.strip()}</p>\\n" for line in s_body.split("\\n") if line.strip() and not line.strip().startswith("---")])
                    supp_content_html = f"  <h1>{sf_clean.upper()}</h1>\\n  <h3>Archive Reference: {folder.upper()}</h3>\\n  <div style='margin-top:20px;'>\\n{s_paragraphs}  </div>"
                    full_supp_page = generate_html_scaffold(sf_clean, supp_content_html, character_links_html, supp_sections_html)
                    with open(os.path.join(output_dir, f"supp_{folder.lower()}_{sf_clean.lower()}.html"), "w", encoding="utf-8") as f:
                        f.write(full_supp_page)

# Generate master index page setup
if character_files:
    first_char_name = os.path.splitext(sorted(character_files)[0])[0].lower()
    shutil.copy(os.path.join(output_dir, f"{first_char_name}.html"), os.path.join(output_dir, "index.html"))

print("\\nCompilation Complete! Cleaned files saved out successfully.")
