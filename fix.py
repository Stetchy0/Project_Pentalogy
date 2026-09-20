import os
import shutil
import json
import re
import random

repo_root = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy"
content_dir = os.path.join(repo_root, "content")
output_dir = os.path.join(repo_root, "prof")
templates_dir = os.path.join(repo_root, "compiler_templates")

print("Initializing Robust Relational Compilation Engine...")
if os.path.exists(output_dir):
    try: shutil.rmtree(output_dir)
    except Exception: pass
os.makedirs(output_dir, exist_ok=True)

# TARGET ACCURATE VERIFIED DIRECTORY CHANNELS FROM DIAGNOSTIC VAULT
private_data_dir = os.path.join(content_dir, "private")
if not os.path.exists(private_data_dir):
    private_data_dir = os.path.join(content_dir, "Project Pentalogy", "private")

master_splash_txt_path = os.path.join(private_data_dir, "Vault Splash Text.txt")
master_data_note_path = os.path.join(private_data_dir, "Character Core Data.md")

splash_quotes_pool = ["VAULT OF THE ARCHIVIST UNLOCKED"]
if os.path.exists(master_splash_txt_path):
    with open(master_splash_txt_path, 'r', encoding='utf-8-sig', errors='ignore') as sf:
        lines_pool = [l.strip() for l in sf.read().splitlines() if l.strip()]
        lines_pool = [l.replace('"', '').replace('|', '').strip() for l in lines_pool if not l.startswith('---')]
        if lines_pool: splash_quotes_pool = lines_pool

with open(os.path.join(templates_dir, "style.css.txt"), "r", encoding="utf-8") as f:
    global_css = f.read()
with open(os.path.join(templates_dir, "graph_carousel_engine.js.txt"), "r", encoding="utf-8") as f:
    js_raw_base = f.read()
with open(os.path.join(output_dir, "style.css"), "w", encoding="utf-8") as f:
    f.write(global_css)
# 1. PRE-SCAN DISK: Detect every single character biography note currently inside your vault folders
discovered_characters = set()
for root, dirs, files in os.walk(content_dir):
    dirs[:] = [d for d in dirs if not d.startswith('.') and d.lower() not in ['node_modules', 'venv', 'env', 'private', 'art']]
    for file in files:
        if file.endswith(".md") and file.lower() != "index.md":
            is_char_folder = "characters" in root.lower() or "bios" in root.lower()
            if is_char_folder:
                clean_name = os.path.splitext(file)[0]
                discovered_characters.add(clean_name.lower().strip())

# 2. RUNTIME MAINBOARD INJECTOR: Parse the master table and generate dynamic dictionaries
master_traits_map = {}
raw_spreadsheet_map = {}

if os.path.exists(master_data_note_path):
    with open(master_data_note_path, 'r', encoding='utf-8-sig', errors='ignore') as f:
        for line_raw in f.read().splitlines():
            line = line_raw.strip()
            if line.startswith("|"):
                cells = [c.strip() for c in line.split("|")]
                # Strip out the empty array positions created by outer table border fences
                if len(cells) > 1 and cells[0] == "": cells = cells[1:]
                if len(cells) > 0 and cells[-1] == "": cells = cells[:-1]
                
                if cells and len(cells) >= 1:
                    raw_char_name = cells[0]
                    if "character" not in raw_char_name.lower() and "---" not in raw_char_name:
                        c_key = raw_char_name.lower().strip()
                        raw_spreadsheet_map[c_key] = {
                            "age": cells[1] if len(cells) > 1 and cells[1] else "Classified",
                            "gender": cells[2] if len(cells) > 2 and cells[2] else "Classified",
                            "sexuality": cells[3] if len(cells) > 3 and cells[3] else "Classified",
                            "height": cells[4] if len(cells) > 4 and cells[4] else "Classified",
                            "trope": cells[5] if len(cells) > 5 and cells[5] else "Classified",
                            "motifs": cells[6] if len(cells) > 6 and cells[6] else "Classified",
                            "first_ment": cells[7] if len(cells) > 7 and cells[7] else "Unlogged",
                            "first_app": cells[8] if len(cells) > 8 and cells[8] else "Unlogged",
                            "playlist": cells[10] if len(cells) > 10 and cells[10] else ""
                        }

# 3. AUTO-TEMPLATE RESOLVER: Match disk vs spreadsheet and auto-generate safe temporary fallbacks
for char in discovered_characters:
    if char in raw_spreadsheet_map:
        master_traits_map[char] = raw_spreadsheet_map[char]
    else:
        master_traits_map[char] = {
            "age": "Classified", "gender": "Classified", "sexuality": "Classified",
            "height": "Classified", "trope": "Classified", "motifs": "Classified",
            "first_ment": "Unlogged", "first_app": "Unlogged", "playlist": ""
        }

def build_vault_tree_html(current_dir_path):
    folders_html, files_html = "", ""
    for item in sorted(os.listdir(current_dir_path)):
        full_path = os.path.join(current_dir_path, item)
        if os.path.isdir(full_path):
            if item.lower() in ["bios", "art"]:
                folders_html += build_vault_tree_html(full_path)
                continue
            if item.startswith(".") or "templates" in item.lower() or "private" in item.lower() or "node_modules" in item.lower():
                continue
            sub = build_vault_tree_html(full_path)
            if sub.strip():
                folders_html += f'<div class="tree-folder" onclick="toggleFolderTree(this)">{item}</div>\n<div class="tree-nested-items" style="display:none;">{sub}</div>\n'
        elif item.endswith(".md"):
            clean_name = os.path.splitext(item)[0]
            file_key = clean_name.lower().strip()
            is_char = "characters" in current_dir_path.lower() or "bios" in current_dir_path.lower()
            url = "index.html" if file_key == "index" else (f"{file_key}.html" if is_char else f"supp_{file_key}.html")
            files_html += f'<a class="tree-file-link" href="{url}">{clean_name.capitalize()}</a>\n'
    return folders_html + files_html

vault_sidebar_tree_html = build_vault_tree_html(content_dir)
def scaffold_html(title, body):
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>{title}</title><link rel="stylesheet" href="style.css"><link href="https://googleapis.com" rel="stylesheet"><style>h1 {{ font-size: 2.0rem !important; margin-bottom: 10px; font-family: 'Special Elite', serif; text-transform: uppercase; }} h2, h3 {{ font-size: 1.3rem !important; margin: 5px 0; font-family: 'Special Elite', serif; }} p, li, td, th, div, summary {{ font-size: 0.95rem !important; line-height: 1.6; font-family: 'Courier Prime', monospace; }} .tree-folder::before {{ content: "📂 "; font-family: sans-serif; }} .tree-file-link::before {{ content: "📄 "; font-family: sans-serif; }}</style></head>
<body><div class="sidebar"><h2 style="margin-top:0;"><a href="index.html" style="color:#2b1e13;">Project Pentalogy</a></h2>
<p id="dynamic-splash-box" style="font-size:0.75rem !important; color:#704829; text-align:center; font-weight:bold; margin-top:0; min-height:36px; padding:0 5px; font-family:'Special Elite', serif; letter-spacing: 0.5px;"></p>
<div style="margin-top:20px;">{vault_sidebar_tree_html}</div></div>
<div class="main-content">{body}</div>
<script>
  function toggleFolderTree(el) {{ let nested = el.nextElementSibling; if (nested && nested.classList.contains("tree-nested-items")) {{ nested.style.display = nested.style.display === "none" ? "block" : "none"; }} }}
  const pool = {json.dumps(splash_quotes_pool)}; document.getElementById("dynamic-splash-box").innerText = pool[Math.floor(Math.random() * pool.length)].toUpperCase();
</script></body></html>"""

master_relationships_map = {}
for root, dirs, files in os.walk(content_dir):
    dirs[:] = [d for d in dirs if not d.startswith('.') and d.lower() not in ['node_modules', 'venv', 'env']]
    for file in files:
        if file.endswith(".md") and "private" in root.lower():
            try:
                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f.read().splitlines():
                        if line.strip().startswith("|") and line.count("|") >= 4:
                            cells = [c.strip() for c in line.split("|") if c.strip()]
                            if len(cells) >= 4:
                                c1, r12, r21, c2 = cells[0].lower().strip(), cells[1], cells[2], cells[3].lower().strip()
                                if c1 not in master_relationships_map: master_relationships_map[c1] = []
                                if c2 not in master_relationships_map: master_relationships_map[c2] = []
                                master_relationships_map[c1].append({"target": c2, "relation": r12, "thumb": f"Art/{c2}/thumbnail.png"})
                                master_relationships_map[c2].append({"target": c1, "relation": r21, "thumb": f"Art/{c1}/thumbnail.png"})
            except Exception: pass

for root, dirs, files in os.walk(content_dir):
    dirs[:] = [d for d in dirs if not d.startswith('.') and d.lower() not in ['node_modules', 'venv', 'env']]
    for file in files:
        if file.endswith(".md"):
            if "private" in root.lower() or "art" in root.lower() or ".git" in root.lower(): continue
            clean_f_name = os.path.splitext(file)[0]
            c_key_var = clean_f_name.lower().strip()
            is_char = "characters" in root.lower() or "bios" in root.lower()
            
            try:
                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f: text = f.read()
            except Exception: continue
            
            display_title = clean_f_name.capitalize()
            text_normalized = text.replace('\r\n', '\n').replace('\r', '\n')
            fm_pattern = re.compile(r'^\s*---\s*\n(.*?)\n\s*---\s*\n', re.DOTALL)
            fm_find = fm_pattern.search(text_normalized)
            
            if fm_find:
                frontmatter_content = fm_find.group(1)
                text = text_normalized[fm_find.end():].strip()
                for line in frontmatter_content.split('\n'):
                    if ':' in line:
                        key, val = [s.strip() for s in line.split(':', 1)]
                        if key.lower().strip() == "title": display_title = val.strip("'\"")

            text = re.sub(r'\[\[([^|\]\n#]+)\|([^\]]+)\]\]', r'<a href="\1.html">\2</a>', text)
            text = re.sub(r'\[\[([^\]\n#]+)\]\]', r'<a href="\1.html">\1</a>', text)
            text = re.sub(r'href="([^"]+)\.html"', lambda m: f'href="{m.group(1).lower().strip()}.html"', text)

            paragraphs = "" if is_char else "".join([f"<p>{l.strip()}</p>\n" for l in text.split("\n") if l.strip()])
            brief_p = ""

            if is_char and c_key_var != "index":
                char_art_folder = None
                for a_root, a_dirs, a_files in os.walk(content_dir):
                    if a_root.lower().endswith(os.path.join("art", c_key_var).lower()) or a_root.lower().endswith(os.path.join("characters", "art", c_key_var).lower()):
                        char_art_folder = a_root
                        break
                
                slides_html, thumb_src = "", "https://placehold.co"
                if char_art_folder and os.path.exists(char_art_folder):
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
                table_html = ""
                for rel in prim_rel:
                    table_html += f'<tr><td><b><a href="{rel["target"]}.html">{rel["target"].capitalize()}</a></b></td><td>"{rel["relation"]}"</td></tr>\n'
                if not table_html: table_html = '<tr><td colspan="2" style="text-align:center; opacity:0.6;">No direct relationships documented.</td></tr>\n'

                traits = master_traits_map.get(c_key_var.lower().strip(), {"age": "Classified", "gender": "Classified", "sexuality": "Classified", "height": "Classified", "trope": "Classified", "motifs": "Classified", "first_ment": "Unlogged", "first_app": "Unlogged", "playlist": ""})
                playlist_markup = f'<a href="{traits["playlist"]}" target="_blank" class="playlist-badge-link">🎵 Character Playlist</a>' if traits["playlist"] else ""

                dossier_appearance_table = f"""<table class="dossier-table-grid" style="margin-top:15px; margin-bottom:20px; background:#faf9f6;">
                  <tr><td style="width:40%; font-weight:bold; border-right:1px solid #dfd2b5; background:#dfd2b5;">First mentioned</td><td>{traits['first_ment']}</td></tr>
                  <tr><td style="font-weight:bold; border-right:1px solid #dfd2b5; background:#dfd2b5;">First appearance</td><td>{traits['first_app']}</td></tr>
                </table>"""

                js_rendered = js_raw_base.replace("NODE_PLACEHOLDER", json.dumps([{"id": c_key_var, "label": "", "thumb": thumb_src, "color": "#704829", "size": 24, "layer": 1, "isRoot": True}])).replace("EDGE_PLACEHOLDER", json.dumps([])).replace("THUMB_PLACEHOLDER", thumb_src)
                
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
                <table class="dossier-table-grid">
                  <thead><tr><th style="width:35%;">Character</th><th>Relationship to {display_title}</th></tr></thead>
                  <tbody>{table_html}</tbody>
                </table>
                <script>{js_rendered}</script>"""
                
                with open(os.path.join(output_dir, f"{c_key_var}.html"), "w", encoding="utf-8") as f:
                    f.write(scaffold_html(display_title, char_html))
            else:
                out_filename = "index.html" if c_key_var == "index" else f"supp_{c_key_var}.html"
                supp_html = f"<h1>{display_title.upper()}</h1><div style='margin-top:20px; background:rgba(255,255,255,0.15); padding:25px; border-radius:6px; border:1px solid #dfd2b5;'>{paragraphs if paragraphs else '<p>Archival log database record entry.</p>'}</div>"
                
                with open(os.path.join(output_dir, out_filename), "w", encoding="utf-8") as f:
                    f.write(scaffold_html(display_title, supp_html))

print("\nCompilation Complete! Pure zero-dependency script executed flawlessly.")
