import os

gitignore_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\.gitignore"

print("Un-hiding website folder from Git tracking limits...")

if os.path.exists(gitignore_path):
    try:
        with open(gitignore_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        # Keep every line EXCEPT lines that block 'prof' or 'public'
        new_lines = [l for line in lines if (l := line.strip()) and not l.startswith("prof") and not l.startswith("public")]
        
        with open(gitignore_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
            
        print("Success! Website files are now visible to GitHub Desktop.")
    except Exception as e:
        print(f"Error updating gitignore: {e}")
else:
    print("Error: Could not locate .gitignore file.")
