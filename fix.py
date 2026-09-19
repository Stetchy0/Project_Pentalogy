import os
import shutil
import json
import re
import random

# Target workspace directory tracks configurations matrices
repo_root = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy"
content_dir = os.path.join(repo_root, "content")
output_dir = os.path.join(repo_root, "prof")

print("Initializing Master Relational Architecture Overhaul...")
if os.path.exists(output_dir):
    try: shutil.rmtree(output_dir)
    except Exception: pass
os.makedirs(output_dir, exist_ok=True)

# LOCATE PRIVATE CONFIGURATION DIRECTORIES NATIVELY
private_data_dir = os.path.join(repo_root, "content", "Project Pentalogy", "private")
if not os.path.exists(private_data_dir): private_data_dir = os.path.join(repo_root, "content", "private")
os.makedirs(private_data_dir, exist_ok=True)

master_splash_txt_path = os.path.join(private_data_dir, "Vault Splash Text.txt")

# Generate standard default system fallback quotes array if file is absent from disk
splash_quotes_pool = ["SECURE DATABASE MAINBOARD", "ACCESS PROTOCOLS APPROVED", "DECRYPTING SYSTEM TRANSLATION LOGS..."]
if os.path.exists(master_splash_txt_path):
    with open(master_splash_txt_path, 'r', encoding='utf-8', errors='ignore') as sf:
        lines_pool = [l.strip() for l in sf.readlines() if l.strip()]
        if lines_pool: splash_quotes_pool = lines_pool
else:
    with open(master_splash_txt_path, 'w', encoding='utf-8') as sf:
        sf.write("\n".join(splash_quotes_pool) + "\n")

global_css = """
body { background-color: #f2ebd9; color: #3d2d1e; font-family: 'Courier Prime', Courier, monospace; margin: 0; padding: 0; line-height: 1.6; }
h1, h2, h3 { font-family: 'Special Elite', Georgia, serif; color: #2b1e13; border-bottom: 2px solid #dfd2b5; padding-bottom: 8px; }
a { color: #704829; text-decoration: none; font-weight: bold; }
a:hover { text-decoration: underline; }
.sidebar { position: fixed; left: 0; top: 0; bottom: 0; width: 300px; background: #dfd2b5; padding: 25px 15px; overflow-y: auto; border-right: 2px solid #a89470; box-sizing: border-box; }
.sidebar h2 { font-family: 'Special Elite', Georgia, serif; font-weight: 900; font-size: 1.5rem; margin-bottom: 5px; text-align: center; }
.tree-folder { cursor: pointer; user-select: none; font-weight: bold; color: #2b1e13; padding: 4px 0; display: block; font-family: 'Special Elite', serif; }
.tree-folder::before { content: "📁 "; display: inline-block; margin-right: 4px; }
.tree-nested-items { display: block; padding-left: 15px; border-left: 1px dashed #a89470; margin-left: 5px; }
.tree-file-link { padding: 3px 0; display: block; font-size: 0.9rem; font-weight: normal; color: #704829; }
.tree-file-link::before { content: "📄 "; margin-right: 4px; }
.main-content { margin-left: 330px; max-width: 850px; padding: 40px; box-sizing: border-box; }
.profile-header-box { display: flex; gap: 25px; align-items: stretch; margin-bottom: 30px; flex-wrap: wrap; }
.profile-thumbnail-panel { flex: 0 0 220px; display: flex; flex-direction: column; gap: 10px; align-items: center; }
.profile-badge-img { width: 100%; height: 250px; object-fit: cover; border-radius: 4px; border: 2px solid #dfd2b5; box-shadow: 0 4px 8px rgba(0,0,0,0.08); background: #faf9f6; }
.playlist-badge-link { display: inline-block; width: 100%; text-align: center; background: #704829; color: #f2ebd9 !important; padding: 8px 12px; border-radius: 4px; font-family: 'Special Elite', serif; font-size: 0.85rem; text-decoration: none !important; box-shadow: 0 2px 5px rgba(0,0,0,0.15); box-sizing: border-box; }
.playlist-badge-link:hover { background: #2b1e13; }
.profile-info-panel { flex: 1; min-width: 280px; display: flex; flex-direction: column; justify-content: center; }
.profile-info-panel ul { list-style-type: square; padding-left: 20px; margin: 0; }
.carousel-container { max-width: 100%; position: relative; margin: 15px auto 15px auto; border-radius: 8px; height: 560px; background: #1c1610; display: flex; align-items: center; justify-content: center; overflow: hidden; box-shadow: inset 0 0 20px rgba(0,0,0,0.8), 0 10px 25px rgba(0,0,0,0.3); }
.mySlides { display: none; position: absolute; width: auto; max-width: 85%; height: 90%; background: #f4edd3; border-radius: 2px; padding: 15px 15px 55px 15px; box-sizing: border-box; text-align: center; border: 1px solid #d4cbb3; box-shadow: 0 8px 20px rgba(0,0,0,0.4), 0 2px 5px rgba(0,0,0,0.3); transition: transform 0.5s ease; }
.mySlides img { height: 100%; max-width: 100%; object-fit: contain; border: 2px solid #2b1e13; }
.slide-caption { color: #3d2d1e; font-size: 0.7rem; font-weight: bold; margin-top: 12px; font-family: 'Courier Prime', monospace; }
.slide-out-back { animation: slideBack 0.55s ease forwards; }
@keyframes slideBack { 0% { transform: translateX(0) scale(1); z-index: 10; opacity: 1; } 50% { transform: translateX(-110%) scale(0.96); z-index: 10; opacity: 1; } 51% { z-index: 1; } 100% { transform: translateX(0) scale(0.92); z-index: 1; opacity: 0; } }
.active-card { display: block; z-index: 5; }
.background-card { display: block; z-index: 2; transform: scale(0.96) translateY(8px); opacity: 0.4; }
.carousel-btn { cursor: pointer; position: absolute; top: 50%; width: auto; padding: 16px; margin-top: -22px; color: #ebdcc8; font-weight: bold; font-size: 18px; background: rgba(43,30,19,0.7); border: none; z-index: 20; }
.prev-btn { left: 10px; } .next-btn { right: 10px; }
details { background: #dfd2b5; padding: 15px; border-radius: 6px; margin: 15px 0; border-left: 5px solid #704829; }
summary { font-weight: bold; cursor: pointer; font-size: 1.05rem; }
.graph-wrapper-box { position: relative; width: 100%; height: 420px; background: #1c1610; border-radius: 8px; border: 2px solid #a89470; margin-top: 15px; margin-bottom: 25px; overflow: hidden; }
#network-canvas { width: 100%; height: 100%; display: block; }
.node-tooltip-card { position: absolute; display: none; background: #fdfaf7; color: #3d2d1e; border: 2px solid #704829; border-radius: 6px; padding: 12px; font-size: 0.8rem; z-index: 100; width: 240px; box-shadow: 0 4px 15px rgba(0,0,0,0.25); }
.tooltip-flex-row { display: flex; gap: 12px; align-items: center; }
.tooltip-thumb { width: 60px; height: 75px; object-fit: cover; }
.dossier-table-grid { width: 100%; border-collapse: collapse; margin-top: 15px; margin-bottom: 25px; background: #dfd2b5; }
.dossier-table-grid th { background: #704829; color: #f2ebd9; font-family: 'Special Elite', sans-serif; padding: 12px; text-align: left; }
.dossier-table-grid td { padding: 12px; border-bottom: 1px solid #a89470; color: #3d2d1e; }
"""
with open(os.path.join(output_dir, "style.css"), "w", encoding="utf-8") as f: f.write(global_css)

def build_vault_tree_html(current_dir_path):
    folders_html, files_html = "", ""
    for item in sorted(os.listdir(current_dir_path)):
        full_path = os.path.join(current_dir_path, item)
        clean_item_name = os.path.splitext(item)
        if os.path.isdir(full_path):
            if item.lower() == "bios":
                folders_html += build_vault_tree_html(full_path)
                continue
            if item.startswith(".") or "templates" in item.lower() or "art" in item.lower() or "private" in item.lower(): continue
            sub_content = build_vault_tree_html(full_path)
            if sub_content.strip():
                folders_html += f'<div class="tree-folder" onclick="toggleFolderTree(this)">{item}</div>\n<div class="tree-nested-items" style="display:none;">{sub_content}</div>\n'
        elif item.endswith(".md"):
            is_in_characters = "characters" in current_dir_path.lower() or "bios" in current_dir_path.lower()
            # Fixed: Added clear index mapping [0] on clean_item_name tuple pairs to prevent sidebar crash
            url = "index.html" if clean_item_name[0].lower() == "index" else (f"{clean_item_name[0].lower()}.html" if is_in_characters else f"supp_{clean_item_name[0].lower()}.html")
            files_html += f'<a class="tree-file-link" href="{url}">{clean_item_name[0].capitalize()}</a>\n'
    return folders_html + files_html

vault_sidebar_tree_html = build_vault_tree_html(content_dir)

def scaffold_html(title, body):
    return f"""<!DOCTYPE html><html><head><title>{title}</title><link rel="stylesheet" href="style.css"><link href="https://googleapis.com" rel="stylesheet"></head>
<body><div class="sidebar"><h2 style="margin-top:0;"><a href="index.html" style="color:#2b1e13;">Project Pentalogy</a></h2>
<p id="dynamic-splash-box" style="font-size:0.75rem; color:#704829; text-align:center; font-weight:bold; margin-top:0; min-height:36px; padding:0 5px; font-family:'Special Elite', serif;"></p>
<div style="margin-top:20px;">{vault_sidebar_tree_html}</div></div>
<div class="main-content">{body}</div>
<script>
  function toggleFolderTree(el) {{
    let nested = el.nextElementSibling;
    if (nested && nested.classList.contains("tree-nested-items")) {{ nested.style.display = nested.style.display === "none" ? "block" : "none"; }}
  }}
  const pool = {json.dumps(splash_quotes_pool)};
  document.getElementById("dynamic-splash-box").innerText = pool[Math.floor(Math.random() * pool.length)].toUpperCase();
</script></body></html>"""
master_relationships_map = {}
master_traits_map = {}
all_bios_characters = []

master_data_note_path = os.path.join(private_data_dir, "Character Core Data.md")
master_rel_note_path = os.path.join(private_data_dir, "Character Relationships Data.md")

# GATHER EXISTING BIO FILES
bios_search_dir = os.path.join(repo_root, "content", "Project Pentalogy", "Characters", "Bios")
if not os.path.exists(bios_search_dir): bios_search_dir = os.path.join(repo_root, "content", "characters", "bios")

if os.path.exists(bios_search_dir):
    for f in os.listdir(bios_search_dir):
        if f.endswith(".md") and os.path.splitext(f)[0].lower() != "index":
            all_bios_characters.append(os.path.splitext(f)[0].capitalize())

# AUTOMATIC TABLE SYNCHRONIZATION WITH STRICT COLUMN INDEX TRACKING
registered_traits = set()
if os.path.exists(master_data_note_path):
    with open(master_data_note_path, 'r', encoding='utf-8') as f: trait_lines = f.readlines()
    for l in trait_lines:
        if l.strip().startswith("|") and l.count("|") >= 5:
            cells = [cell.strip() for cell in l.split("|") if cell.strip()]
            if cells and "character" not in cells[0].lower() and "---" not in cells[0]:
                registered_traits.add(cells[0].lower())
else:
    trait_lines = [
        "# CHARACTER CORE DATA MASTERLIST\n\n",
        "| Character | Age | Gender | Sexuality | Height | Trope | Motifs | First mentioned | First appearance | Present in | Playlist link |\n",
        "| --------- | --- | ------ | --------- | ------ | ----- | ------ | --------------- | ---------------- | ---------- | ------------- |\n"
    ]

updated_traits = False
for char in sorted(all_bios_characters):
    if char.lower() not in registered_traits:
        trait_lines.append(f"| {char} | | | | | | | | | | |\n")
        updated_traits = True
if updated_traits:
    with open(master_data_note_path, 'w', encoding='utf-8') as f: f.writelines(trait_lines)

# READ MASTER DATA AND PROCESS INTERNAL CELL OFFSET MAPPINGS CLEANLY
for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".md"):
            try:
                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f: lines = f.readlines()
                for line in lines:
                    if line.strip().startswith("|") and line.count("|") >= 4:
                        raw_cells = [cell.strip() for cell in line.replace("\n", "").split("|")]
                        if raw_cells[0] == "": raw_cells = raw_cells[1:]
                        if raw_cells and raw_cells[-1] == "": raw_cells = raw_cells[:-1]
                        
                        if raw_cells and "character" not in raw_cells[0].lower() and "---" not in raw_cells[0]:
                            if line.count("|") == 5 and len(raw_cells) == 4:
                                c1 = raw_cells[0].lower().strip()
                                r12 = raw_cells[1]
                                r21 = raw_cells[2]
                                c2 = raw_cells[3].lower().strip()
                                if c1 not in master_relationships_map: master_relationships_map[c1] = []
                                if c2 not in master_relationships_map: master_relationships_map[c2] = []
                                master_relationships_map[c1].append({"target": c2, "relation": r12, "thumb": f"Art/{c2}/thumbnail.png"})
                                master_relationships_map[c2].append({"target": c1, "relation": r21, "thumb": f"Art/{c1}/thumbnail.png"})
                            elif line.count("|") >= 12 and len(raw_cells) >= 10:
                                char_key = raw_cells[0].lower().strip()
                                master_traits_map[char_key] = {
                                    "age": raw_cells[1] if raw_cells[1] else "Classified",
                                    "gender": raw_cells[2] if raw_cells[2] else "Classified",
                                    "sexuality": raw_cells[3] if raw_cells[3] else "Classified",
                                    "height": raw_cells[4] if raw_cells[4] else "Classified",
                                    "trope": raw_cells[5] if raw_cells[5] else "Classified",
                                    "motifs": raw_cells[6] if raw_cells[6] else "Classified",
                                    "first_ment": raw_cells[7] if raw_cells[7] else "Unlogged",
                                    "first_app": raw_cells[8] if raw_cells[8] else "Unlogged",
                                    "present_in": raw_cells[9] if raw_cells[9] else "Unlogged",
                                    "playlist": raw_cells[10] if len(raw_cells) >= 11 and raw_cells[10] else ""
                                }
            except Exception: pass
for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".md"):
            if "private" in root.lower(): continue
            clean_f_name = os.path.splitext(file)[0]
            c_key_var = clean_f_name.lower().strip()
            is_char = "characters" in root.lower() or "bios" in root.lower()
            
            try:
                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f: text = f.read()
            except Exception: continue
            
            # Metadata Grabber: Dynamically reads internal metadata title properties to swap Index names
            display_title = clean_f_name.capitalize()
            title_match = re.search(r'^(?:title|name|#)\s*:\s*["\']?([^"\']+)["\']?', text, re.IGNORECASE | re.MULTILINE)
            if title_match: display_title = title_match.group(1).strip()
            elif text.startswith("# "): 
                display_title = text.split("\n")[0].replace("# ", "").strip()
            
            if text.startswith("---"): text = text.split("---", 2)[-1].strip()

            # REGEX WIKI NAVIGATOR: Convert [[Abaddon|The Scales]] -> <a href="abaddon.html">The Scales</a>
            text = re.sub(r'\[\[([^|\]\n#]+)\|([^\]]+)\]\]', r'<a href="\1.html">\2</a>', text)
            text = re.sub(r'\[\[([^\]\n#]+)\]\]', r'<a href="\1.html">\1</a>', text)
            text = re.sub(r'href="([^"]+)\.html"', lambda m: f'href="{m.group(1).lower().strip()}.html"', text)

            # EXCLUSIVE BLOCK SANITIZER: Scrubs layout templates out of paragraph text outputs completely
            clean_lines = []
            skip_script_block = False
            for l in text.split("\n"):
                l_strip = l.strip()
                if "function showslides" in l_strip.lower() or "let slideindex" in l_strip.lower():
                    skip_script_block = True
                if skip_script_block:
                    if "showslides();" in l_strip.lower() or "showslides(" in l_strip.lower(): skip_script_block = False
                    continue
                if any(x in l_strip.lower() for x in ["basic overview", "age:", "gender:", "sexuality:", "height:", "trope/s:", "similar characters", "general appearance:", "other info:", "motifs / symbols:", "relationship title", "target character", "reciprocal title", "character's playlist", "click here for long text", "first mentioned", "first appearance", "present in", "dossier", "character artwork", "backstory & details", "character connections", "details"]):
                    continue
                if l_strip.startswith(("|", "*", "---", "🔗", "^", "❮", "❯", "►", ">")) or "PLAYLIST_URL_HERE" in l_strip or "![[" in l_strip:
                    continue
                clean_lines.append(l)
            
            paragraphs = "".join([f"<p>{l.strip()}</p>\n" for l in clean_lines if l.strip()])
            brief_p = "<p>No primary summary logged inside this profile ledger index.</p>"
            for chunk in text.split("\n"):
                if any(x in chunk.lower() for x in ["brief:", "tldr:", "summary:"]):
                    brief_p = f"<p>{chunk.split(':', 1)[-1].strip()}</p>"; break

            if is_char and c_key_var != "index":
                char_art_folder = os.path.join(content_dir, "Project Pentalogy", "Characters", "Art", c_key_var)
                if not os.path.exists(char_art_folder): char_art_folder = os.path.join(content_dir, "characters", "art", c_key_var)
                
                slides_html, thumb_src = "", "https://placehold.co"
                if os.path.exists(char_art_folder) and os.path.isdir(char_art_folder):
                    imgs = os.listdir(char_art_folder)
                    os.makedirs(os.path.join(output_dir, "Art", c_key_var), exist_ok=True)
                    for img in imgs:
                        if img.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".gif")):
                            shutil.copy(os.path.join(char_art_folder, img), os.path.join(output_dir, "Art", c_key_var, img))
                            if os.path.splitext(img)[0].lower() == "thumbnail": thumb_src = f"Art/{c_key_var}/{img}"
                    slide_imgs = [i for i in imgs if i.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".gif")) and os.path.splitext(i)[0].lower() != "thumbnail"]
                    for img in slide_imgs: slides_html += f'<div class="mySlides"><img src="Art/{c_key_var}/{img}"><div class="slide-caption">{img}</div></div>\n'
                if not slides_html: slides_html = '<div class="mySlides" style="display:block;"><img src="https://placehold.co"><div class="slide-caption">Gallery Empty</div></div>'

                prim_rel = master_relationships_map.get(c_key_var, [])
                prim_t = [r["target"] for r in prim_rel]
                g_nodes = [{"id": c_key_var, "label": "", "thumb": thumb_src, "color": "#704829", "size": 24, "layer": 1, "isRoot": True}]
                g_edges, table_html = [], ""

                for rel in prim_rel:
                    g_nodes.append({"id": rel["target"], "label": rel["target"].capitalize(), "relation": rel["relation"], "thumb": rel["thumb"], "color": "#a89470", "size": 10, "layer": 1, "isRoot": False})
                    g_edges.append({"source": c_key_var, "target": rel["target"], "layer": 1})
                    table_html += f'<tr><td><b><a href="{rel["target"]}.html">{rel["target"].capitalize()}</a></b></td><td>"{rel["relation"]}"</td></tr>\n'
                if not table_html: table_html = '<tr><td colspan="2" style="text-align:center; opacity:0.6;">No direct relationships documented.</td></tr>\n'

                for rel in prim_rel:
                    for l2 in master_relationships_map.get(rel["target"], []):
                        if l2["target"] != c_key_var and l2["target"] not in prim_t:
                            if not any(n["id"] == l2["target"] for n in g_nodes):
                                g_nodes.append({"id": l2["target"], "label": l2["target"].capitalize(), "relation": l2["relation"] + f" (via {rel['target'].capitalize()})", "thumb": f"Art/{l2['target']}/thumbnail.png", "color": "rgba(168, 148, 112, 0.35)", "size": 7, "layer": 2, "isRoot": False})
                            g_edges.append({"source": rel["target"], "target": l2["target"], "layer": 2})

                traits = master_traits_map.get(c_key_var, {"age": "Classified", "gender": "Classified", "sexuality": "Classified", "height": "Classified", "trope": "Classified", "motifs": "Classified", "first_ment": "Unlogged", "first_app": "Unlogged", "present_in": "Unlogged", "playlist": ""})
                playlist_markup = f'<a href="{traits["playlist"]}" target="_blank" class="playlist-badge-link">🎵 Character Playlist</a>' if traits["playlist"] else ""

                dossier_appearance_table = f"""<table class="dossier-table-grid" style="margin-top:15px; margin-bottom:20px; background:#faf9f6;">
                  <tr><td style="width:40%; font-weight:bold; border-right:1px solid #dfd2b5; background:#dfd2b5;">First mentioned</td><td>{traits['first_ment']}</td></tr>
                  <tr><td style="font-weight:bold; border-right:1px solid #dfd2b5; background:#dfd2b5;">First appearance</td><td>{traits['first_app']}</td></tr>
                  <tr><td style="font-weight:bold; border-right:1px solid #dfd2b5; background:#dfd2b5;">Present in</td><td>{traits['present_in']}</td></tr>
                </table>"""

                js_template = """<script>
                  let currentIdx = 0; let cards = [];
                  function initCarousel() {
                    const allCards = document.getElementsByClassName("mySlides");
                    for(let i=0; i<allCards.length; i++) { cards.push(allCards[i]); }
                    if (cards.length === 0) return; updateCardStack();
                  }
                  function moveCard(direction) {
                    if (cards.length <= 1) return; let oldCard = cards[currentIdx];
                    if (direction === 1) { oldCard.classList.add("slide-out-back"); setTimeout(() => { oldCard.classList.remove("slide-out-back"); currentIdx = (currentIdx + 1) % cards.length; updateCardStack(); }, 500); }
                    else { currentIdx = (currentIdx - 1 + cards.length) % cards.length; updateCardStack(); }
                  }
                  function updateCardStack() {
                    for (let i = 0; i < cards.length; i++) { cards[i].className = "mySlides"; cards[i].style.display = "none"; }
                    cards[currentIdx].style.display = "block"; cards[currentIdx].classList.add("active-card");
                    if (cards.length > 1) { let nextIdx = (currentIdx + 1) % cards.length; cards[nextIdx].style.display = "block"; cards[nextIdx].classList.add("background-card"); }
                  }
                  initCarousel();
                  const canvas = document.getElementById("network-canvas"); const ctx = canvas.getContext("2d"); const tooltip = document.getElementById("tooltip-modal");
                  const nodes = NODE_PLACEHOLDER; const edges = EDGE_PLACEHOLDER;
                  
                  function resizeCanvas() {
                    const dpr = window.devicePixelRatio || 1;
                    const rect = canvas.parentElement.getBoundingClientRect();
                    canvas.width = rect.width * dpr;
                    canvas.height = rect.height * dpr;
                    canvas.style.width = rect.width + "px";
                    canvas.style.height = rect.height + "px";
                    ctx.scale(dpr, dpr);
                  }
                  resizeCanvas(); const rootImg = new Image(); rootImg.src = "THUMB_PLACEHOLDER";
                  nodes.forEach((node, idx) => {
                    const w = canvas.width / (window.devicePixelRatio || 1);
                    const w = canvas.width / (window.devicePixelRatio || 1);
                    const h = canvas.height / (window.devicePixelRatio || 1);
                    if (node.isRoot) { node.x = w / 2; node.y = h / 2; }
                    else { const angle = (idx * 2 * Math.PI) / (nodes.length - 1); const radius = node.layer === 2 ? 180 : 105; node.x = w / 2 + radius * Math.cos(angle); node.y = h / 2 + radius * Math.sin(angle); }
                  });

                  function drawGraph() {
                    const w = canvas.width / (window.devicePixelRatio || 1);
                    const h = canvas.height / (window.devicePixelRatio || 1);
                    ctx.clearRect(0, 0, w, h);
                    edges.forEach(edge => {
                      const srcNode = nodes.find(n => n.id === edge.source); const tgtNode = nodes.find(n => n.id === edge.target);
                      if (srcNode && tgtNode) { ctx.beginPath(); ctx.moveTo(srcNode.x, srcNode.y); ctx.lineTo(tgtNode.x, tgtNode.y); ctx.strokeStyle = edge.layer === 2 ? "rgba(168, 148, 112, 0.12)" : "rgba(168, 148, 112, 0.45)"; ctx.lineWidth = edge.layer === 2 ? 1 : 2; ctx.stroke(); }
                    });
                    nodes.forEach(node => {
                      ctx.beginPath();
                      if (node.isRoot) { ctx.save(); ctx.arc(node.x, node.y, node.size, 0, 2 * Math.PI); ctx.clip(); try { ctx.drawImage(rootImg, node.x - node.size, node.y - node.size, node.size * 2, node.size * 2); } catch(e) { ctx.fillStyle = node.color; ctx.fill(); } ctx.restore(); }
                      else { ctx.arc(node.x, node.y, node.size, 0, 2 * Math.PI); ctx.fillStyle = node.color; ctx.fill(); }
                      ctx.strokeStyle = node.layer === 2 ? "rgba(28, 22, 16, 0.3)" : "#1c1610"; ctx.lineWidth = 2; ctx.stroke();
                      if (!node.isRoot) { ctx.fillStyle = node.layer === 2 ? "rgba(222, 208, 191, 0.45)" : "#ded0bf"; ctx.font = node.layer === 2 ? "9px 'Courier Prime', monospace" : "bold 11px 'Courier Prime', monospace"; ctx.textAlign = "center"; ctx.fillText(node.label, node.x, node.y - node.size - 6); }
                    });
                  }
                  canvas.addEventListener("mousemove", (e) => {
                    const rect = canvas.getBoundingClientRect(); const mouseX = e.clientX - rect.left; const mouseY = e.clientY - rect.top; let hoveredNode = null;
                    nodes.forEach(node => { const dist = Math.sqrt((mouseX - node.x)**2 + (mouseY - node.y)**2); if (dist <= node.size + 4) { hoveredNode = node; } });
                    if (hoveredNode && !hoveredNode.isRoot) {
                      tooltip.style.display = "block"; tooltip.style.left = (mouseX + 15) + "px"; tooltip.style.top = (mouseY + 15) + "px";
                      tooltip.innerHTML = `<div class="tooltip-flex-row"><img src="${hoveredNode.thumb}" class="tooltip-thumb" onerror="this.src='https://placehold.co'"><div class="tooltip-info"><h4 class="tooltip-title">${hoveredNode.label}</h4><p style="margin:0; font-size:0.75rem; color:#704829;"><b>RELATION:</b></p><p style="margin:0; font-size:0.75rem; font-style:italic;">"${hoveredNode.relation}"</p></div></div>`;
                    } else { tooltip.style.display = "none"; }
                  });
                  rootImg.onload = drawGraph; canvas.addEventListener("mouseleave", () => { tooltip.style.display = "none"; }); window.addEventListener("resize", () => { resizeCanvas(); drawGraph(); }); drawGraph();
                </script>"""
                js_rendered = js_template.replace("NODE_PLACEHOLDER", json.dumps(g_nodes)).replace("EDGE_PLACEHOLDER", json.dumps(g_edges)).replace("THUMB_PLACEHOLDER", thumb_src)
                
                char_html = f"""<h1>{display_title.upper()}</h1>
                <div class="profile-header-box">
                  <div class="profile-thumbnail-panel">
                    <img src="{thumb_src}" class="profile-badge-img" onerror="this.src='https://placehold.co'">
                    {playlist_markup}
                  </div>
                  <div class="profile-info-panel">
                    <h3>Basic Overview</h3>
                    <ul style="padding-left:15px; margin:0;">
                      <li><b>Age:</b> {traits['age']}</li>
                      <li><b>Gender:</b> {traits['gender']}</li>
                      <li><b>Sexuality:</b> {traits['sexuality']}</li>
                      <li><b>Height:</b> {traits['height']}</li>
                      <li><b>Trope/s:</b> {traits['trope']}</li>
                      <li><b>Motifs:</b> {traits['motifs']}</li>
                    </ul>
                  </div>
                </div>
                <div class="carousel-container">
                  <button class="carousel-btn prev-btn" onclick="moveCard(-1)">&#10094;</button>
                  {slides_html}
                  <button class="carousel-btn next-btn" onclick="moveCard(1)">&#10095;</button>
                </div>
                {dossier_appearance_table}
                <details><summary>Brief</summary><div style="padding:10px 5px 5px 5px;">{brief_p}</div></details>
                <details open><summary>Dossier</summary><div style="padding:15px; background:rgba(255,255,255,0.2); border-radius:4px;">{paragraphs}</div></details>
                <div class="graph-wrapper-box"><canvas id="network-canvas"></canvas><div id="tooltip-modal" class="node-tooltip-card"></div></div>
                <table class="dossier-table-grid">
                  <thead>
                    <tr>
                      <th style="width:35%;">Character</th>
                      <th>Relationship to {display_title}</th>
                    </tr>
                  </thead>
                  <tbody>{table_html}</tbody>
                </table>
                {js_rendered}"""
                
                with open(os.path.join(output_dir, f"{c_key_var}.html"), "w", encoding="utf-8") as f: f.write(scaffold_html(display_title, char_html))
            else:
                out_filename = "index.html" if c_key_var == "index" else f"supp_{c_key_var}.html"
                supp_html = f"<h1>{display_title.upper()}</h1><div style='margin-top:20px; background:rgba(255,255,255,0.15); padding:25px; border-radius:6px; border:1px solid #dfd2b5;'>{paragraphs if paragraphs else '<p>Archival log database record entry.</p>'}</div>"
                with open(os.path.join(output_dir, out_filename), "w", encoding="utf-8") as f: f.write(scaffold_html(display_title, supp_html))

print("\nCompilation Complete! Splash text and link routing modules successfully deployed.")
