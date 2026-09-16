import os
import shutil

root_dir = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\content\Characters"

print("Starting deep directory sweep...")

for folder_name in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder_name)
    
    if os.path.isdir(folder_path):
        # Find folders that contain uppercase letters (the ghosts)
        if not folder_name.islower():
            lowercase_version = folder_name.lower()
            lowercase_path = os.path.join(root_dir, lowercase_version)
            
            # If both paths physically exist on the disk, safely merge/clean them
            if os.path.exists(lowercase_path) and folder_path != lowercase_path:
                print(f"Cleaning duplicate ghost folder structural tracking for: {folder_name}")
                try:
                    # Move any missed files from the ghost folder to the lowercase folder
                    for item in os.listdir(folder_path):
                        src = os.path.join(folder_path, item)
                        dst = os.path.join(lowercase_path, item)
                        if not os.path.exists(dst):
                            shutil.move(src, dst)
                    # Erase the duplicate tracking reference
                    os.rmdir(folder_path)
                except Exception:
                    pass

print("Sweep complete! Check GitHub Desktop.")
