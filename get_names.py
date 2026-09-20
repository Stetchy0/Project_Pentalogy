import os

repo_root = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy"
content_dir = os.path.join(repo_root, "content")

# Loop to find the true character bios directory folder dynamically
bios_dir = None
for root, dirs, files in os.walk(content_dir):
    dirs[:] = [d for d in dirs if not d.startswith('.') and d.lower() not in ['node_modules', 'venv', 'env', 'private', 'art']]
    if root.lower().endswith(os.path.join("characters", "bios").lower()) or root.lower().endswith("bios"):
        bios_dir = root
        break

if not bios_dir:
    # Fallback to standard tree path rules if explicit folder crawl misses
    bios_dir = os.path.join(content_dir, "Project Pentalogy", "Characters", "Bios")
    if not os.path.exists(bios_dir):
        bios_dir = os.path.join(content_dir, "characters", "bios")

if not os.path.exists(bios_dir):
    print(f"Error: Could not locate your character biography folder directory path.")
    print(f"Searched content root target: {content_dir}")
    exit()

print(f"Successfully connected to Biography Registry Folder: {bios_dir}\n")
print("--- CHARACTER KEY REGISTRY NAME LIST ---")

character_names = []
for file in sorted(os.listdir(bios_dir)):
    if file.endswith(".md") and file.lower() != "index.md":
        # Extract the raw filename string token minus the file extension extension
        raw_name = os.path.splitext(file)[0]
        character_names.append(raw_name)
        print(f"-> {raw_name}")

print("----------------------------------------")
print(f"Operation complete! Extracted {len(character_names)} unique character names.\n")
print("You can copy this exact list directly into your CSV spreadsheet row handles!")
