import os

repo_root = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy"
content_dir = os.path.join(repo_root, "content")

# Track your native Obsidian characters folder directory trees path
bios_dir = os.path.join(content_dir, "Project Pentalogy", "Characters", "Bios")
if not os.path.exists(bios_dir):
    bios_dir = os.path.join(content_dir, "characters", "bios")

if not os.path.exists(bios_dir):
    print(f"Error: Could not locate character folder at {bios_dir}")
    exit()

print(f"Scanning directory path matrix: {bios_dir}\n")
updated_count = 0

for file in os.listdir(bios_dir):
    if file.endswith(".md") and file.lower() != "index.md":
        file_path = os.path.join(bios_dir, file)
        char_name = os.path.splitext(file)[0].capitalize()
        
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            
        # Skip if the file already has an active frontmatter layout block
        if content.startswith("---"):
            print(f"[-] Skipping {file} - Properties block already active.")
            continue
            
        # Construct the clean, empty Obsidian property parameters grid
        frontmatter = f"""---
title: {char_name}
age: 
gender: 
sexuality: 
height: 
trope: 
motifs: 
---

"""
        # Overwrite the file by prepending the blank metadata block right at the top
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(frontmatter + content)
            
        print(f"[+] Successfully stamped clean properties block onto {file}")
        updated_count += 1

print(f"\nOperation complete! Automatically injected missing keys to {updated_count} profiles.")
