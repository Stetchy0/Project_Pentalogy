import os
import shutil

# Target directory where the character folders are located
base_dir = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\content\Characters"

# 1. Establish the correct top-level global folders
global_bios_dir = os.path.join(base_dir, "bios")
global_art_dir = os.path.join(base_dir, "art")

os.makedirs(global_bios_dir, exist_ok=True)
os.makedirs(global_art_dir, exist_ok=True)

print("Sweeping and fixing character layout leftovers...")

# 2. Iterate through every character folder
for item_name in os.listdir(base_dir):
    item_path = os.path.join(base_dir, item_name)
    
    # Skip the global target directories themselves
    if item_name.lower() in ["bios", "art"] or not os.path.isdir(item_path):
        continue
        
    character_folder = item_name  # e.g., 'carter', 'bunny'
    
    # Walk through the character's internal folder contents
    for root, dirs, files in os.walk(item_path, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            file_lower = file.lower()
            
            # --- HANDLE TEXT FILES ---
            if file_lower.endswith(".md"):
                # Move it to /Characters/bios/ and name it cleanly after the character folder
                target_bio_name = f"{character_folder.lower()}.md"
                target_bio_path = os.path.join(global_bios_dir, target_bio_name)
                
                shutil.move(file_path, target_bio_path)
                print(f" Moved Bio: {file} -> bios/{target_bio_name}")
                
            # --- HANDLE IMAGES AND ARTWORK ---
            elif file_lower.endswith((".png", ".jpg", ".jpeg", ".webp", ".gif")):
                # Ensure a character-specific art folder exists globally
                char_art_dir = os.path.join(global_art_dir, character_folder.lower())
                os.makedirs(char_art_dir, exist_ok=True)
                
                target_art_path = os.path.join(char_art_dir, file)
                shutil.move(file_path, target_art_path)
                print(f" Moved Image: {file} -> art/{character_folder.lower()}/")
                
            # --- HANDLE MISPLACED DIRECTORIES (Like the ones in alex) ---
            elif file_lower in ["bios", "art"]:
                # If they are empty leftover artifact folders, we skip to let rmdir clear them
                continue

    # 3. Clean up the now-empty character directory
    try:
        shutil.rmtree(item_path)
        print(f" Cleaned up empty folder: {character_folder}")
    except Exception as e:
        print(f" Couldn't completely delete {character_folder}: {e}")

print("\n System layout sweep complete!")
