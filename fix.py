import os

root = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\content\Characters"

for path, subdirs, files in os.walk(root):
    folder = os.path.basename(path)
    for f in files:
        if f.lower() == f"{folder.lower()}.md":
            old_path = os.path.join(path, f)
            new_path = os.path.join(path, "index.md")
            
            # Step 1: Get the clean character name (e.g., "Aiko")
            character_name = os.path.splitext(f)[0]
            
            try:
                with open(old_path, 'r', encoding='utf-8') as file_obj:
                    lines = file_obj.readlines()
            except Exception:
                with open(old_path, 'r', encoding='cp1252') as file_obj:
                    lines = file_obj.readlines()
            
            # Step 2: Inject the title line inside the existing frontmatter box
            new_lines = []
            title_injected = False
            
            for line in lines:
                new_lines.append(line)
                # If we hit the absolute first '---' line, inject the title line right after it
                if line.strip() == "---" and not title_injected:
                    new_lines.append(f"title: {character_name}\n")
                    title_injected = True
            
            # Step 3: Write out to the new index.md file
            with open(new_path, 'w', encoding='utf-8') as file_obj:
                file_obj.writelines(new_lines)
                
            # Step 4: Remove the old duplicate named file
            os.remove(old_path)
            print(f"Injected title & renamed: {f} -> index.md")
