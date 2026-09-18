import os

# Target path configuration tracking
base_content = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\content\Project Pentalogy\Characters"

bios_dir = os.path.join(base_content, "Bios")
art_dir = os.path.join(base_content, "Art")

print("Targeting directory structure path: content/Project Pentalogy/Characters")
print("Executing bullet formatting correction pass...")
processed_count = 0

if not os.path.exists(bios_dir):
    print(f"Error: Could not find bios folder at {bios_dir}")
    exit()

for file in os.listdir(bios_dir):
    if file.endswith(".md"):
        file_path = os.path.join(bios_dir, file)
        character_key = os.path.splitext(file)[0].lower() 
        character_title = os.path.splitext(file)[0].capitalize() 
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                body_content = f.read()
        except Exception:
            with open(file_path, 'r', encoding='cp1252') as f:
                body_content = f.read()
        
        if body_content.startswith("---"):
            parts = body_content.split("---", 2)
            if len(parts) >= 3:
                body_content = parts[2].lstrip()

        char_art_folder = os.path.join(art_dir, character_key)
        image_slides_html = ""
        thumbnail_src = "https://placehold.co" 
        
        if os.path.exists(char_art_folder) and os.path.isdir(char_art_folder):
            valid_extensions = (".png", ".jpg", ".jpeg", ".webp", ".gif")
            all_files = os.listdir(char_art_folder)
            
            for f_name in all_files:
                if os.path.splitext(f_name)[0].lower() == "thumbnail" and f_name.lower().endswith(valid_extensions):
                    thumbnail_src = f"../Art/{character_key}/{f_name}"
                    break
            
            images = [img for img in all_files if img.lower().endswith(valid_extensions) and not os.path.splitext(img)[0].lower() == "thumbnail"]
            for idx, img_name in enumerate(images):
                web_img_path = f"../Art/{character_key}/{img_name}"
                image_slides_html += f'  <!-- Slide {idx + 1} -->\n'
                image_slides_html += f'  <div class="mySlides fade">\n'
                image_slides_html += f'    <img src="{web_img_path}" style="width:100%">\n'
                image_slides_html += f'  </div>\n'

        if not image_slides_html:
            image_slides_html = '  <div class="mySlides fade" style="display:block; text-align:center; padding: 20px;">\n    <p>No artwork added to folder yet.</p>\n  </div>\n'

        # Using explicit HTML list syntax inside the flex container to ensure uniform cross-platform lines
        new_layout = f"""---
title: {character_title}
aliases: []
tags: []
---

<div class="profile-header-box">
  <div class="profile-thumbnail-panel">
    <img src="{thumbnail_src}" class="profile-badge-img" onerror="this.src='https://placehold.co'">
  </div>
  <div class="profile-info-panel">
    <h3 style="margin-top:0;">Basic Overview</h3>
    <ul style="list-style-type: disc; margin: 0; padding-left: 20px; line-height: 1.6;">
      <li><b>Age:</b> </li>
      <li><b>Gender:</b> </li>
      <li><b>Sexuality:</b> </li>
      <li><b>Height:</b> </li>
      <li><b>Trope/s:</b> </li>
      <li><b>Similar characters in personality:</b> </li>
      <li><b>General Appearance:</b> </li>
      <li><b>Other info:</b> </li>
      <li><b>Motifs / Symbols:</b> </li>
    </ul>
  </div>
</div>

---

### Character Artwork
<div class="slideshow-container">
{image_slides_html}
</div>

<style>
  .profile-header-box {{ display: flex; gap: 25px; align-items: stretch; margin-bottom: 20px; flex-wrap: wrap; }}
  .profile-thumbnail-panel {{ flex: 0 0 220px; display: flex; }}
  .profile-badge-img {{ width: 100%; height: 100%; object-fit: cover; border-radius: 6px; border: 2px solid var(--lightgray); box-shadow: 0 4px 8px rgba(0,0,0,0.08); background: var(--background); }}
  .profile-info-panel {{ flex: 1; min-width: 280px; display: flex; flex-direction: column; justify-content: center; }}
  
  .slideshow-container {{ max-width: 100%; position: relative; margin: 20px auto; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.15); }}
  .mySlides {{ display: none; }}
  .fade {{ animation-name: fade; animation-duration: 1.5s; }}
  @keyframes fade {{ from {{opacity: .4}} to {{opacity: 1}} }}
</style>

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

---

### Backstory & Details

<details>
<summary><b>Click Here for long text (This is quite long)</b></summary>

{body_content}

</details>

**TLDR:** 

---

### Character Connections

<div class="connection-row">
  <div class="connection-card-pair">
    <div class="connection-card left-card">
      <img src="{thumbnail_src}" class="conn-avatar" onerror="this.src='https://placehold.co'">
      <div class="conn-label">Relationship Title (e.g. Older Brother)</div>
    </div>
    <div class="connection-link-icon">🔗</div>
    <div class="connection-card right-card">
      <img src="../Art/target_character_folder/thumbnail.png" class="conn-avatar" onerror="this.src='https://placehold.co'">
      <div class="conn-label"><a href="TARGET_CHARACTER_NOTE.md">Target Character Name</a></div>
      <div class="conn-sublabel">Reciprocal Title (e.g. Younger Brother)</div>
    </div>
  </div>
</div>

<style>
  .connection-row {{ display: flex; flex-direction: column; gap: 20px; margin: 25px 0; }}
  .connection-card-pair {{ display: flex; align-items: center; justify-content: space-between; background: var(--highlight); border-radius: 8px; padding: 15px; border: 1px solid var(--lightgray); box-shadow: 0 2px 6px rgba(0,0,0,0.05); }}
  .connection-card {{ flex: 1; display: flex; flex-direction: column; align-items: center; text-align: center; }}
  .connection-link-icon {{ font-size: 20px; padding: 0 15px; color: var(--secondary); }}
  .conn-avatar {{ width: 70px; height: 70px; border-radius: 8px; object-fit: cover; border: 2px solid var(--gray); background: var(--background); }}
  .conn-label {{ font-size: 0.9rem; font-weight: bold; margin-top: 8px; color: var(--dark); }}
  .conn-sublabel {{ font-size: 0.8rem; color: var(--gray); margin-top: 2px; }}
  .connection-card a {{ text-decoration: none; color: var(--secondary) !important; }}
  .connection-card a:hover {{ text-decoration: underline; }}
</style>

---
[Character's Playlist!](PLAYLIST_URL_HERE)
"""

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_layout)
            
        print(f"Formatted Clean Badge Layout: {file}")
        processed_count += 1

print(f"\nCompleted! All {processed_count} files fixed into stacked HTML bullet listings.")
