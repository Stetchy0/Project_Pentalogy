import os
import json

repo_root = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy"
package_json_path = os.path.join(repo_root, "package.json")

print("Restoring project workspace package baselines...")

if os.path.exists(package_json_path):
    try:
        with open(package_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # Clean out the non-existent npm registry references we added
        if "dependencies" in data:
            keys_to_remove = [k for k in data["dependencies"].keys() if k.startswith("@quartz-community")]
            for key in keys_to_remove:
                data["dependencies"].pop(key)
                
        with open(package_json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print(" -> package.json cleanly restored to your original framework specs.")
    except Exception as e:
        print(f"Error restoring package file: {e}")
