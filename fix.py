import os
import shutil
import json

# Target directory paths
repo_root = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy"
content_dir = os.path.join(repo_root, "content")
output_dir = os.path.join(repo_root, "prof")
bios_dir = os.path.join(content_dir, "Project Pentalogy", "Characters", "Bios")
art_dir = os.path.join(content_dir, "Project Pentalogy", "Characters", "Art")
supp_dir = os.path.join(content_dir, "Project Pentalogy", "Supplementary Items")

if not os.path.exists(bios_dir):
    bios_dir = os.path.join(content_dir, "characters", "bios")
    art_dir = os.path.join(content_dir, "characters", "art")
    supp_dir = os.path.join(content_dir, "supplementary items")

print("Initializing Pure-Text Native Frontmatter Relation Parser Engine...")
if os.path.exists(output_dir):
    try: shutil.rmtree(output_dir)
    except Exception: pass
os.makedirs(output_dir, exist_ok=True)

# Generate card stacking styling profiles with bold serif sidebar overrides
global_css = """
body { background-color: #f2ebd9; color: #3d2d1e; font-family: 'Courier Prime', Courier, monospace; margin: 0; padding: 0; line-height: 1.6; }
h1, h2, h3 { font-family: 'Special Elite', Georgia, serif; color: #2b1e13; border-bottom: 2px solid #dfd2b5; padding-bottom: 8px; }
a { color: #704829; text-decoration: none; font-weight: bold; }
a:hover { text-decoration: underline; }
.sidebar { position: fixed; left: 0; top: 0; bottom: 0; width: 280px; background: #dfd2b5; padding: 25px; overflow-y: auto; border-right: 2px solid #a89470; box-sizing: border-box; }
.sidebar h2 { font-family: 'Special Elite', Georgia, serif; font-weight: 900; font-size: 1.6rem; margin-bottom: 5px; letter-spacing: -0.5px; }
.sidebar h3 { font-family: 'Special Elite', Georgia, serif; font-size: 1.05rem; font-weight: 700; margin-top: 25px; margin-bottom: 10px; border-bottom: 1px solid #a89470; padding-bottom: 3px; color: #704829; }
.sidebar ul { padding-left: 15px; line-height: 1.8; list-style-type: square; margin-top: 5px; }
.main-content { margin-left: 320px; max-width: 850px; padding: 40px; box-sizing: border-box; }
.profile-header-box { display: flex; gap: 25px; align-items: stretch; margin-bottom: 30px; flex-wrap: wrap; }
.profile-thumbnail-panel { flex: 0 0 220px; display: flex; }
.profile-badge-img { width: 100%; height: 250px; object-fit: cover; border-radius: 4px; border: 2px solid #dfd2b5; box-shadow: 0 4px 8px rgba(0,0,0,0.08); background: #faf9f6; }
.profile-info-panel { flex: 1; min-width: 280px; display: flex; flex-direction: column; justify-content: center; }
.profile-info-panel ul { list-style-type: square; padding-left: 20px; margin: 0; }
.carousel-container { max-width: 100%; position: relative; margin: 15px auto 30px auto; border-radius: 8px; height: 560px; background: #1c1610; display: flex; align-items: center; justify-content: center; overflow: hidden; box-shadow: inset 0 0 20px rgba(0,0,0,0.8), 0 10px 25px rgba(0,0,0,0.3); }
.mySlides { display: none; position: absolute; width: auto; max-width: 85%; height: 90%; background: #f4edd3; border-radius: 2px; padding: 15px 15px 55px 15px; box-sizing: border-box; text-align: center; border: 1px solid #d4cbb3; box-shadow: 0 8px 20px rgba(0,0,0,0.4), 0 2px 5px rgba(0,0,0,0.3); transition: transform 0.5s cubic-bezier(0.25, 1, 0.5, 1); }
.mySlides img { height: 100%; max-width: 100%; object-fit: contain; border: 2px solid #2b1e13; box-sizing: border-box; }
.slide-caption { color: #3d2d1e; font-size: 0.7rem; font-weight: bold; margin-top: 12px; font-family: 'Courier Prime', monospace; letter-spacing: 0.5px; opacity: 0.8; text-transform: lowercase; }
.slide-out-back { animation: slideBack 0.55s cubic-bezier(0.25, 1, 0.5, 1) forwards; }
@keyframes slideBack { 0% { transform: translateX(0) scale(1); z-index: 10; opacity: 1; } 50% { transform: translateX(-110%) scale(0.96); z-index: 10; opacity: 1; } 51% { z-index: 1; } 100% { transform: translateX(0) scale(0.92); z-index: 1; opacity: 0; } }
.active-card { display: block; z-index: 5; transform: scale(1); opacity: 1; }
.background-card { display: block; z-index: 2; transform: scale(0.96) translateY(8px); opacity: 0.4; }
.carousel-btn { cursor: pointer; position: absolute; top: 50%; width: auto; padding: 16px; margin-top: -22px; color: #ebdcc8; font-weight: bold; font-size: 18px; transition: 0.3s; border-radius: 4px; user-select: none; background: rgba(43,30,19,0.7); border: none; z-index: 20; }
.carousel-btn:hover { background-color: rgba(112,72,41,0.9); }
.prev-btn { left: 10px; } .next-btn { right: 10px; }
details { background: #dfd2b5; padding: 15px; border-radius: 6px; margin: 15px 0; border-left: 5px solid #704829; }
summary { font-weight: bold; cursor: pointer; font-size: 1.05rem; }
.graph-wrapper-box { position: relative; width: 100%; height: 420px; background: #1c1610; border-radius: 8px; border: 2px solid #a89470; margin-top: 15px; margin-bottom: 35px; overflow: hidden; box-shadow: 0 6px 15px rgba(0,0,0,0.15); }
#network-canvas { width: 100%; height: 100%; cursor: grab; } #network-canvas:active { cursor: grabbing; }
.node-tooltip-card { position: absolute; display: none; background: #fdfaf7; color: #3d2d1e; border: 2px solid #704829; border-radius: 6px; padding: 12px; font-family: 'Courier Prime', monospace; font-size: 0.8rem; pointer-events: none; z-index: 100; box-shadow: 0 4px 15px rgba(0,0,0,0.25); width: 240px; }
.tooltip-flex-row { display: flex; gap: 12px; align-items: center; }
.tooltip-thumb { width: 60px; height: 75px; object-fit: cover; border-radius: 3px; border: 1px solid #dfd2b5; background: #faf9f6; }
.tooltip-info { flex: 1; }
.tooltip-title { font-family: 'Special Elite', sans-serif; font-size: 0.95rem; margin: 0 0 4px 0; color: #2b1e13; border-bottom: 1px solid #dfd2b5; }
.dossier-table-grid { width: 100%; border-collapse: collapse; margin-top: 15px; font-family: 'Courier Prime', monospace; font-size: 0.9rem; background: #dfd2b5; border-radius: 4px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
.dossier-table-grid th { background: #704829; color: #f2ebd9; font-family: 'Special Elite', sans-serif; padding: 12px; text-align: left; font-size: 0.95rem; letter-spacing: 0.5px; }
.dossier-table-grid td { padding: 12px; border-bottom: 1px solid #a89470; color: #3d2d1e; }
.dossier-table-grid tr:last-child td { border-bottom: none; } .dossier-table-grid tr:hover td { background: rgba(112, 72, 41, 0.08); }
"""
with open(os.path.join(output_dir, "style.css"), "w", encoding="utf-8") as f: f.write(global_css)

character_links_html = ""
character_files = [f for f in os.listdir(bios_dir) if f.endswith(".md")] if os.path.exists(bios_dir) else []
for char_file in sorted(character_files):
    c_name = os.path.splitext(char_file)[0]
    character_links_html += f'    <li><a href="{c_name.lower()}.html">{c_name.capitalize()}</a></li>\n'

supp_sections_html = ""
if os.path.exists(supp_dir):
    for folder in sorted(os.listdir(supp_dir)):
        f_path = os.path.join(supp_dir, folder)
        if os.path.isdir(f_path):
            s_files = [f for f in os.listdir(f_path) if f.endswith(".md")]
            if s_files:
                supp_sections_html += f"  <h3>{folder.upper()}</h3>\n  <ul>\n"
                for sf in sorted(s_files):
                    sf_name = os.path.splitext(sf)[0]
                    supp_sections_html += f'    <li><a href="supp_{folder.lower()}_{sf_name.lower()}.html">{sf_name.capitalize()}</a></li>\n'
                supp_sections_html += "  </ul>\n"

def scaffold_html(title, body, sidebar_chars, sidebar_supp):
    return f"""<!DOCTYPE html><html><head><title>{title}</title><link rel="stylesheet" href="style.css"><link href="https://googleapis.com" rel="stylesheet"></head>
<body><div class="sidebar"><h2 style="margin-top:0;"><a href="index.html" style="color:#2b1e13;">Project Pentalogy</a></h2><p style="font-size:0.75rem; color:#704829; margin-top:0;"><b>SYSTEM DOSSIER LOCK</b></p><h3>SUBJECT PROFILES</h3><ul style="list-style-type:none; padding-left:5px; margin:0;">{sidebar_chars}</ul>{sidebar_supp}</div>
<div class="main-content">{body}</div></body></html>"""
master_relationships_map = {}
for char_file in character_files:
    c_key = os.path.splitext(char_file)[0].lower()
    master_relationships_map[c_key] = []
    try:
        with open(os.path.join(bios_dir, char_file), 'r', encoding='utf-8', errors='ignore') as f:
            raw = f.read()
        if raw.startswith("---"):
            y_block = raw.split("---")[1]
            in_rel, c_char, c_type = False, None, None
            for line in y_block.split("\n"):
                if "relationships:" in line.lower(): in_rel = True; continue
                if in_rel:
                    if line.strip().startswith("-") or (":" in line and not line.startswith(" ")):
                        if c_char: master_relationships_map[c_key].append({"target": c_char.lower(), "relation": c_type if c_type else "Connection", "thumb": f"Art/{c_char.lower()}/thumbnail.png"})
                        c_char, c_type = None, None
                    if "character:" in line.lower(): c_char = line.split(":", 1)[1].strip().replace('"', '').replace("'", "")
                    elif "type:" in line.lower(): c_type = line.split(":", 1)[1].strip().replace('"', '').replace("'", "")
            if c_char: master_relationships_map[c_key].append({"target": c_char.lower(), "relation": c_type if c_type else "Connection", "thumb": f"Art/{c_char.lower()}/thumbnail.png"})
    except Exception: pass

for file in character_files:
    c_key = os.path.splitext(file)[0].lower()
    c_title = os.path.splitext(file)[0].capitalize()
    with open(os.path.join(bios_dir, file), 'r', encoding='utf-8', errors='ignore') as f: body = f.read()
    if body.startswith("---"): body = body.split("---", 2)[2].strip()

    char_art_folder = os.path.join(art_dir, c_key)
    slides_html, thumb_src = "", "https://placehold.co"
    if os.path.exists(char_art_folder) and os.path.isdir(char_art_folder):
        all_imgs = os.listdir(char_art_folder)
        os.makedirs(os.path.join(output_dir, "Art", c_key), exist_ok=True)
        for img in all_imgs:
            if img.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".gif")):
                shutil.copy(os.path.join(char_art_folder, img), os.path.join(output_dir, "Art", c_key, img))
                if os.path.splitext(img)[0].lower() == "thumbnail": thumb_src = f"Art/{c_key}/{img}"
        slide_imgs = [i for i in all_imgs if i.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".gif")) and os.path.splitext(i)[0].lower() != "thumbnail"]
        for idx, img_name in enumerate(slide_imgs): slides_html += f'    <div class="mySlides"><img src="Art/{c_key}/{img_name}"><div class="slide-caption">{img_name}</div></div>\n'
    if not slides_html: slides_html = '    <div class="mySlides" style="display:block;"><p style="padding:40px; color:#3d2d1e;">No archive photograph attachments cataloged.</p></div>'

    brief_p = "<p>No primary summary logged inside this profile ledger index.</p>"
    lines = body.split("\n")
    for idx, line in enumerate(lines):
        if any(x in line.lower() for x in ["tldr", "summary", "brief"]):
            if idx + 1 < len(lines) and lines[idx+1].strip(): brief_p = f"<p>{lines[idx+1].strip()}</p>"; break

    prim_rel = master_relationships_map.get(c_key, [])
    prim_t = [r["target"] for r in prim_rel]
    g_nodes = [{"id": c_key, "label": "", "thumb": thumb_src, "color": "#704829", "size": 24, "layer": 1, "isRoot": True}]
    g_edges, table_html = [], ""

    for rel in prim_rel:
        g_nodes.append({"id": rel["target"], "label": rel["target"].capitalize(), "relation": rel["relation"], "thumb": rel["thumb"], "color": "#a89470", "size": 10, "layer": 1, "isRoot": False})
        g_edges.append({"source": c_key, "target": rel["target"], "layer": 1})
        table_html += f'    <tr><td><b><a href="{rel["target"]}.html">{rel["target"].capitalize()}</a></b></td><td>"{rel["relation"]}"</td></tr>\n'

    for rel in prim_rel:
        for l2 in master_relationships_map.get(rel["target"], []):
            if l2["target"] != c_key and l2["target"] not in prim_t:
                if not any(n["id"] == l2["target"] for n in g_nodes):
                    g_nodes.append({"id": l2["target"], "label": l2["target"].capitalize(), "relation": l2["relation"] + f" (via {rel['target'].capitalize()})", "thumb": l2["thumb"], "color": "rgba(168, 148, 112, 0.35)", "size": 7, "layer": 2, "isRoot": False})
                g_edges.append({"source": rel["target"], "target": l2["target"], "layer": 2})
    if not table_html: table_html = '    <tr><td colspan="2" style="text-align:center; opacity:0.6;">No direct relationships documented.</td></tr>\n'

    paragraphs = "".join([f"    <p>{l.strip()}</p>\n" for l in body.split("\n") if l.strip() and not any(x in l.lower() for x in ["brief", "tldr", "summary", "character artwork"])])

    char_html = f"""  <h1>{c_title.upper()}</h1>
  <div class="profile-header-box">
    <div class="profile-thumbnail-panel"><img src="{thumb_src}" class="profile-badge-img" onerror="this.src='https://placehold.co'"></div>
    <div class="profile-info-panel"><h3>Basic Overview</h3><ul style="padding-left:15px; margin:0;"><li><b>Age:</b> Case File Record Locked</li><li><b>Gender:</b> Classified</li><li><b>Sexuality:</b> Documented</li><li><b>Height:</b> Measured</li><li><b>Trope/s:</b> Logged</li><li><b>Motifs / Symbols:</b> Filed</li></ul></div>
  </div>
  <div class="carousel-container"><button class="carousel-btn prev-btn" onclick="moveCard(-1)">&#10094;</button>{slides_html}    <button class="carousel-btn next-btn" onclick="moveCard(1)">&#10095;</button></div>
  <details><summary>Brief</summary><div style="padding:10px 5px 5px 5px;">{brief_p}</div></details>
  <details open><summary>Dossier</summary><div style="padding:10px 5px 5px 5px;">{paragraphs}</div></details>
  <div class="graph-wrapper-box"><canvas id="network-canvas"></canvas><div id="tooltip-modal" class="node-tooltip-card"></div></div>
  <table class="dossier-table-grid"><thead><tr><th style="width:35%;">Character</th><th>Relationship to {c_title}</th></tr></thead><tbody>{table_html}</tbody></table>
"""
    js_template_block = """
<script>
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
  function resizeCanvas() { canvas.width = canvas.parentElement.clientWidth; canvas.height = canvas.parentElement.clientHeight; }
  resizeCanvas(); const rootImg = new Image(); rootImg.src = "THUMB_PLACEHOLDER";
  
  nodes.forEach((node, idx) => {
    if (node.isRoot) { node.x = canvas.width / 2; node.y = canvas.height / 2; }
    else { const angle = (idx * 2 * Math.PI) / (nodes.length - 1); const radius = node.layer === 2 ? 200 : 110; node.x = canvas.width / 2 + radius * Math.cos(angle); node.y = canvas.height / 2 + radius * Math.sin(angle); }
  });

  function drawGraph() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
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
</script>
"""
    js_rendered = js_template_block.replace("NODE_PLACEHOLDER", json.dumps(g_nodes)).replace("EDGE_PLACEHOLDER", json.dumps(g_edges)).replace("THUMB_PLACEHOLDER", thumb_src)
    full_body_content = char_html + js_rendered
    with open(os.path.join(output_dir, f"{c_key}.html"), "w", encoding="utf-8") as f: f.write(scaffold_html(c_title, full_body_content, character_links_html, supp_sections_html))

if character_files:
    first_char = os.path.splitext(sorted(character_files)[0])[0].lower()
    shutil.copy(os.path.join(output_dir, f"{first_char}.html"), os.path.join(output_dir, "index.html"))
print("\nCompilation Complete! Native zero-dependency metadata maps generated.")
