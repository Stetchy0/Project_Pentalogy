import os
import shutil

# Root project path on your computer
repo_root = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy"

# Hidden tracking caches used by Quartz's compiler engine
cache_folder = os.path.join(repo_root, "quartz", ".quartz-cache")
public_folder = os.path.join(repo_root, "public")

print("Executing deep framework compilation cache purge pass...")

# 1. Force clear the internal transpilation cache tracking folder
if os.path.exists(cache_folder):
    try:
        shutil.rmtree(cache_folder)
        print(" -> Successfully purged corrupt hidden .quartz-cache directory.")
    except Exception as e:
        print(f" Could not remove build cache: {e}")
else:
    print(" -> Quartz build cache folder is already empty.")

# 2. Force clear your old local static site output logs
if os.path.exists(public_folder):
    try:
        shutil.rmtree(public_folder)
        print(" -> Successfully cleared historical public folder generation maps.")
    except Exception as e:
        print(f" Could not remove public folder: {e}")

print("\nCache wipe complete! Ready for a pristine framework build pass.")
