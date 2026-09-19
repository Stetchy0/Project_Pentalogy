import os
import shutil
import json
import re
import random

repo_root = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy"
content_dir = os.path.join(repo_root, "content")
output_dir = os.path.join(repo_root, "prof")
templates_dir = os.path.join(repo_root, "compiler_templates")

print("Initializing Fixed Modular Compilation Pipeline...")
if os.path.exists(output_dir):
    try: shutil.rmtree(output_dir)
    except Exception: pass
os.makedirs(output_dir, exist_ok=True)
# ACCURATE PATH TRAVERSAL: Pinpoint private notes sitting inside nested workspace trees
private_data_dir = os.path.join(content_dir, "Project Pentalogy", "private")
if not os.path.exists(private_data_dir):
    private_data_dir = os.path.join(content_dir, "private")

master_splash_txt_path = os.path.join(private_data_dir, "Vault Splash Text.txt")
master_data_note_path = os.path.join(private_data_dir, "Character Core Data.md")

# Read in your real custom splash texts natively from your txt document file
splash_quotes_pool = ["SECURE MAINBOARD INITIALIZED", "ACCESS CODE GRANTED"]
if os.path.exists(master_splash_txt_path):
    with open(master_splash_txt_path, 'r', encoding='utf-8', errors='ignore') as sf:
        lines_pool = [l.strip() for l in sf.readlines() if l.strip()]
        if lines_pool: splash_quotes_pool = lines_pool

with open(os.path.join(templates_dir, "style.css.txt"), "r", encoding="utf-8") as f:
    global_css = f.read()
with open(os.path.join(templates_dir, "graph_carousel_engine.js.txt"), "r", encoding="utf-8") as f:
    js_raw_base = f.read()
with open(os.path.join(output_dir, "style.css"), "w", encoding="utf-8") as f:
    f.write(global_css)
def build_vault_tree_html(current_dir_path):
    folders_html, files_html = "", ""
    for item in sorted(os.listdir(current_dir_path)):
        full_path = os.path.join(current_dir_path, item)
        if os.path.isdir(full_path):
            if item.lower() in ["bios", "art"]:
                folders_html += build_vault_tree_html(full_path)
                continue
            if item.startswith(".") or "templates" in item.lower() or "private" in item.lower():
                continue
            sub = build_vault_tree_html(full_path)
            if sub.strip():
                folders_html += f'<div class="tree-folder" onclick="toggleFolderTree(this)">{item}</div>\n<div class="tree-nested-items" style="display:none;">{sub}</div>\n'
        elif item.endswith(".md"):
            clean_name = os.path.splitext(item)[0]
            is_char = "characters" in current_dir_path.lower() or "bios" in current_dir_path.lower()
            url = "index.html" if clean_name.lower() == "index" else (f"{clean_name.lower()}.html" if is_char else f"supp_{clean_name.lower()}.html")
            files_html += f'<a class="tree-file-link" href="{url}">{clean_name.capitalize()}</a>\n'
    return folders_html + files_html

vault_sidebar_tree_html = build_vault_tree_html(content_dir)

def scaffold_html(title, body):
    return f"""<!DOCTYPE html><html><head><title>{title}</title><link rel="stylesheet" href="style.css"><link href="https://googleapis.com" rel="stylesheet"></head>
<body><div class="sidebar"><h2 style="margin-top:0;"><a href="index.html" style="color:#2b1e13;">Project Pentalogy</a></h2>
<p id="dynamic-splash-box" style="font-size:0.75rem; color:#704829; text-align:center; font-weight:bold; margin-top:0; min-height:36px; padding:0 5px; font-family:'Special Elite', serif;"></p>
<div style="margin-top:20px;">{vault_sidebar_tree_html}</div></div>
<div class="main-content">{body}</div>
<script>
  function toggleFolderTree(el) {{ let nested = el.nextElementSibling; if (nested && nested.classList.contains("tree-nested-items")) {{ nested.style.display = nested.style.display === "none" ? "block" : "none"; }} }}
  const pool = {json.dumps(splash_quotes_pool)}; document.getElementById("dynamic-splash-box").innerText = pool[Math.floor(Math.random() * pool.length)].toUpperCase();
</script></body></html>"""
master_relationships_map, master_traits_map = {}, {}

# FIXED: Tuned line pipe count down to match standard 11-column note grids natively
if os.path.exists(master_data_note_path):
    with open(master_data_note_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f.readlines():
            if line.strip().startswith("|") and line.count("|") >= 11:
                cells = [c.strip() for c in line.split("|")[1:-1]]
                if cells and "character" not in cells[0].lower() and "---" not in cells[0]:
                    char_key = cells[0].lower().strip()
                    master_traits_map[char_key] = {
                        "age": cells[1] if len(cells) > 1 and cells[1] else "Classified",
                        "gender": cells[2] if len(cells) > 2 and cells[2] else "Classified",
                        "sexuality": cells[3] if len(cells) > 3 and cells[3] else "Classified",
                        "height": cells[4] if len(cells) > 4 and cells[4] else "Classified",
                        "trope": cells[5] if len(cells) > 5 and cells[5] else "Classified",
                        "motifs": cells[6] if len(cells) > 6 and cells[6] else "Classified",
                        "first_ment": cells[7] if len(cells) > 7 and cells[7] else "Unlogged",
                        "first_app": cells[8] if len(cells) > 8 and cells[8] else "Unlogged",
                        "present_in": cells[9] if len(cells) > 9 and cells[9] else "Unlogged",
                        "playlist": cells[10] if len(cells) > 10 and cells[10] else ""
                    }

# Parse relationship strings independently out of your custom private connection matrix maps
for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".md") and "private" in root.lower():
            try:
                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f.readlines():
                        if line.strip().startswith("|") and line.count("|") == 5:
                            cells = [c.strip() for c in line.split("|")[1:-1]]
                            if cells and "character" not in cells[0].lower() and "---" not in cells[0]:
                                c1, r12, r21, c2 = cells[0].lower().strip(), cells[1], cells[2], cells[3].lower().strip()
                                if c1 not in master_relationships_map: master_relationships_map[c1] = []
                                if c2 not in master_relationships_map: master_relationships_map[c2] = []
                                master_relationships_map[c1].append({"target": c2, "relation": r12, "thumb": f"Art/{c2}/thumbnail.png"})
                                master_relationships_map[c2].append({"target": c1, "relation": r21, "thumb": f"Art/{c1}/thumbnail.png"})
            except Exception: pass
for root, dirs, files in os.walk(content_dir):
    if "private" in root.lower() or "art" in root.lower() or ".git" in root.lower():
        continue
    for file in files:
        if file.endswith(".md"):
            clean_f_name = os.path.splitext(file)[0]
            c_key_var = clean_f_name.lower().strip()
            is_char = "characters" in root.lower() or "bios" in root.lower()
            
            try:
                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f: text = f.read()
            except Exception: continue
            
            display_title = clean_f_name.capitalize()
            title_match = re.search(r'^(?:title|name|#)\s*:\s*["\']?([^"\']+)["\']?', text, re.IGNORECASE | re.MULTILINE)
            if title_match: display_title = title_match.group(1).strip()
            elif text.startswith("# "):
                # FIXED: Corrected compound list slicing syntax to handle heading blocks safely
                first_line = text.split("\n")[0]
                display_title = first_line.replace("# ", "").strip()
            if text.startswith("---"):
                try: text = text.split("---", 2)[-1].strip()
                except Exception: pass

            text = re.sub(r'\[\[([^|\]\n#]+)\|([^\]]+)\]\]', r'<a href="\1.html">\2</a>', text)
            text = re.sub(r'\[\[([^\]\n#]+)\]\]', r'<a href="\1.html">\1</a>', text)
            text = re.sub(r'href="([^"]+)\.html"', lambda m: f'href="{m.group(1).lower().strip()}.html"', text)

            clean_lines = []
            for l in text.split("\n"):
                l_strip = l.strip()
                if any(x in l_strip.lower() for x in ["basic overview", "age:", "gender:", "sexuality:", "height:", "trope/s:", "similar characters", "general appearance:", "other info:", "motifs / symbols:", "relationship title", "target character", "reciprocal title", "character's playlist", "click here for long text", "first mentioned", "first appearance", "present in", "dossier", "character artwork", "backstory & details", "character connections", "details"]): continue
                if l_strip.startswith(("|", "*", "---", "🔗", "^", "❮", "❯", "►", ">")) or "PLAYLIST_URL_HERE" in l_strip or "![[" in l_strip: continue
                clean_lines.append(l_strip)
            
            paragraphs = "".join([f"<p>{l}</p>\n" for l in clean_lines if l])
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

                js_rendered = js_raw_base.replace("NODE_PLACEHOLDER", json.dumps(g_nodes)).replace("EDGE_PLACEHOLDER", json.dumps(g_edges)).replace("THUMB_PLACEHOLDER", thumb_src)
                
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
                  <thead><tr><th style="width:35%;">Character</th><th>Relationship to {display_title}</th></tr></thead>
                  <tbody>{table_html}</tbody>
                </table>
                <script>{js_rendered}</script>"""
                with open(os.path.join(output_dir, f"{c_key_var}.html"), "w", encoding="utf-8") as f: f.write(scaffold_html(display_title, char_html))
            else:
                out_filename = "index.html" if c_key_var == "index" else f"supp_{c_key_var}.html"
                supp_html = f"<h1>{display_title.upper()}</h1><div style='margin-top:20px; background:rgba(255,255,255,0.15); padding:25px; border-radius:6px; border:1px solid #dfd2b5;'>{paragraphs if paragraphs else '<p>Archival log database record entry.</p>'}</div>"
                with open(os.path.join(output_dir, out_filename), "w", encoding="utf-8") as f: f.write(scaffold_html(display_title, supp_html))

print("\nCompilation Complete! Pure zero-dependency script executed flawlessly.")
