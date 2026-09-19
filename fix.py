import os
import shutil
import json
import re

# Target workspace directories configuration matrices
repo_root = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy"
content_dir = os.path.join(repo_root, "content")
output_dir = os.path.join(repo_root, "prof")

print("Initializing Master Frontmatter Relational Database Compiler Pass...")
if os.path.exists(output_dir):
    try: shutil.rmtree(output_dir)
    except Exception: pass
os.makedirs(output_dir, exist_ok=True)

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
.profile-thumbnail-panel { flex: 0 0 220px; display: flex; }
.profile-badge-img { width: 100%; height: 250px; object-fit: cover; border-radius: 4px; border: 2px solid #dfd2b5; box-shadow: 0 4px 8px rgba(0,0,0,0.08); background: #faf9f6; }
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
#network-canvas { width: 100%; height: 100%; }
.node-tooltip-card { position: absolute; display: none; background: #fdfaf7; color: #3d2d1e; border: 2px solid #704829; border-radius: 6px; padding: 12px; font-size: 0.8rem; z-index: 100; width: 240px; box-shadow: 0 4px 15px rgba(0,0,0,0.25); }
.tooltip-flex-row { display: flex; gap: 12px; align-items: center; }
.tooltip-thumb { width: 60px; height: 75px; object-fit: cover; }
.dossier-table-grid { width: 100%; border-collapse: collapse; margin-top: 15px; margin-bottom: 25px; background: #dfd2b5; }
.dossier-table-grid th { background: #704829; color: #f2ebd9; font-family: 'Special Elite', sans-serif; padding: 12px; text-align: left; }
.dossier-table-grid td { padding: 12px; border-bottom: 1px solid #a89470; }
"""
with open(os.path.join(output_dir, "style.css"), "w", encoding="utf-8") as f: f.write(global_css)

def build_vault_tree_html(current_dir_path):
    folders_html, files_html = "", ""
    for item in sorted(os.listdir(current_dir_path)):
        full_path = os.path.join(current_dir_path, item)
        clean_item_name = os.path.splitext(item)[0]
        if os.path.isdir(full_path):
            if item.startswith(".") or "templates" in item.lower() or "art" in item.lower() or "private" in item.lower(): continue
            sub_content = build_vault_tree_html(full_path)
            if sub_content.strip():
                folders_html += f'<div class="tree-folder" onclick="toggleFolderTree(this)">{item}</div>\n<div class="tree-nested-items" style="display:none;">{sub_content}</div>\n'
        elif item.endswith(".md"):
            url = "index.html" if clean_item_name.lower() == "index" else (f"{clean_item_name.lower()}.html" if "bios" in current_dir_path.lower() else f"supp_{clean_item_name.lower()}.html")
            files_html += f'<a class="tree-file-link" href="{url}">{clean_item_name.capitalize()}</a>\n'
    return folders_html + files_html

vault_sidebar_tree_html = build_vault_tree_html(content_dir)

def scaffold_html(title, body):
    return f"""<!DOCTYPE html><html><head><title>{title}</title><link rel="stylesheet" href="style.css"><link href="https://googleapis.com" rel="stylesheet"></head>
<body><div class="sidebar"><h2 style="margin-top:0;"><a href="index.html" style="color:#2b1e13;">Project Pentalogy</a></h2><p style="font-size:0.7rem; color:#704829; text-align:center; margin-top:0;"><b>VAULT FILE EXPLORER</b></p><div style="margin-top:20px;">{vault_sidebar_tree_html}</div></div>
<div class="main-content">{body}</div>
<script>
  function toggleFolderTree(el) {{
    let nested = el.nextElementSibling;
    if (nested && nested.classList.contains("tree-nested-items")) {{ nested.style.display = nested.style.display === "none" ? "block" : "none"; }}
  }}
</script></body></html>"""
master_relationships_map = {}
master_traits_map = {}

# Crawl entire vault to parse both relationships and 10-column core trait data tables automatically
for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".md"):
            try:
                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                for line in lines:
                    if line.strip().startswith("|") and line.count("|") >= 5:
                        parts = [p.strip() for p in line.split("|")[1:-1]]
                        if len(parts) >= 4 and parts[0].lower() != "character 1" and parts[0].lower() != "character" and not set(parts).issubset({'-', ':', ' '}):
                            if len(parts) == 4:
                                c1, r12, r21, c2 = parts[0].lower(), parts[1], parts[2], parts[3].lower()
                                if c1 not in master_relationships_map: master_relationships_map[c1] = []
                                if c2 not in master_relationships_map: master_relationships_map[c2] = []
                                master_relationships_map[c1].append({"target": c2, "relation": r12, "thumb": f"Art/{c2}/thumbnail.png"})
                                master_relationships_map[c2].append({"target": c1, "relation": r21, "thumb": f"Art/{c1}/thumbnail.png"})
                            elif len(parts) >= 10:
                                char_key = parts[0].lower()
                                master_traits_map[char_key] = {
                                    "age": parts[1], "gender": parts[2], "sexuality": parts[3],
                                    "height": parts[4], "trope": parts[5], "motifs": parts[6],
                                    "first_ment": parts[7], "first_app": parts[8], "present_in": parts[9]
                                }
            except Exception: pass

bios_search_dir = os.path.join(content_dir, "Project Pentalogy", "Characters", "Bios")
if not os.path.exists(bios_search_dir): bios_search_dir = os.path.join(content_dir, "characters", "bios")
character_files = [f for f in os.listdir(bios_search_dir) if f.endswith(".md")] if os.path.exists(bios_search_dir) else []

for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".md"):
            if "private" in root.lower(): continue
            target_name_string = os.path.splitext(file)[0]
            c_key = target_name_string.lower()
            is_char = "bios" in root.lower()
            
            try:
                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f: text = f.read()
            except Exception: continue
            if text.startswith("---"): text = text.split("---", 2)[-1].strip()

            # Clean wiki internal backlinks mapping strings [[Link|Display]] -> Display
            text = re.sub(r'\\\[\\\[([^|\\\]]+)\\|([^\\\]]+)\\]\\\]', r'\\2', text)
            text = re.sub(r'\\\[\\\[([^\\\]]+)\\]\\\]', r'\\1', text)

            paragraphs = "".join([f"<p>{l.strip()}</p>\n" for l in text.split("\n") if l.strip() and not l.strip().startswith(("#", "|", "*"))])
            brief_p = "<p>No summary logged.</p>"
            for chunk in text.split("\n"):
                if any(x in chunk.lower() for x in ["brief:", "tldr:", "summary:"]):
                    brief_p = f"<p>{chunk.split(':', 1)[-1].strip()}</p>"; break

            if is_char:
                char_art_folder = os.path.join(content_dir, "Project Pentalogy", "Characters", "Art", c_key)
                slides_html, thumb_src = "", "https://placehold.co"
                if os.path.exists(char_art_folder):
                    imgs = os.listdir(char_art_folder)
                    os.makedirs(os.path.join(output_dir, "Art", c_key), exist_ok=True)
                    for img in imgs:
                        if img.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".gif")):
                            shutil.copy(os.path.join(char_art_folder, img), os.path.join(output_dir, "Art", c_key, img))
                            if os.path.splitext(img)[0].lower() == "thumbnail": thumb_src = f"Art/{c_key}/{img}"
                    slide_imgs = [i for i in imgs if i.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".gif")) and os.path.splitext(i)[0].lower() != "thumbnail"]
                    for img in slide_imgs: slides_html += f'<div class="mySlides"><img src="Art/{c_key}/{img}"><div class="slide-caption">{img}</div></div>\n'
                if not slides_html: slides_html = '<div class="mySlides" style="display:block;"><p style="padding:40px; color:#3d2d1e;">No attachments cataloged.</p></div>'

                prim_rel = master_relationships_map.get(c_key, [])
                prim_t = [r["target"] for r in prim_rel]
                g_nodes = [{"id": c_key, "label": "", "thumb": thumb_src, "color": "#704829", "size": 24, "layer": 1, "isRoot": True}]
                g_edges, table_html = [], ""

                for rel in prim_rel:
                    g_nodes.append({"id": rel["target"], "label": rel["target"].capitalize(), "relation": rel["relation"], "thumb": rel["thumb"], "color": "#a89470", "size": 10, "layer": 1, "isRoot": False})
                    g_edges.append({"source": c_key, "target": rel["target"], "layer": 1})
                    table_html += f'<tr><td><b><a href="{rel["target"]}.html">{rel["target"].capitalize()}</a></b></td><td>"{rel["relation"]}"</td></tr>\n'
                if not table_html: table_html = '<tr><td colspan="2" style="text-align:center; opacity:0.6;">No direct relationships documented.</td></tr>\n'

                traits = master_traits_map.get(c_key, {"age": "Classified", "gender": "Classified", "sexuality": "Classified", "height": "Classified", "trope": "Classified", "motifs": "Classified", "first_ment": "", "first_app": "", "present_in": ""})
                dossier_appearance_table = f"<table class='dossier-table-grid' style='margin-top:0; margin-bottom:15px; background:#faf9f6;'><tr><td style='width:40%; font-weight:bold; border-right:1px solid #dfd2b5; background:#dfd2b5;'>First mentioned</td><td>{traits['first_ment']}</td></tr><tr><td style='font-weight:bold; border-right:1px solid #dfd2b5; background:#dfd2b5;'>First appearance</td><td>{traits['first_app']}</td></tr><tr><td style='font-weight:bold; border-right:1px solid #dfd2b5; background:#dfd2b5;'>Present in</td><td>{traits['present_in']}</td></tr></table>"

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
            </script>"""
