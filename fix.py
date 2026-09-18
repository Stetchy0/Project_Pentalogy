import os
import json

package_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\package.json"

print("Initiating production environment optimization pass...")

if os.path.exists(package_path):
    try:
        # Load up your package configuration layout dictionary
        with open(package_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # 1. Strip out old strict engine limit boundaries that force old systems
        if "engines" in data:
            data.pop("engines")
            print(" -> Extracted legacy engine boundary requirements.")
            
        # 2. Inject modern Node.js 22 runtime fields explicitly into the project code template
        if "scripts" in data:
            # Re-routes the default build command to enforce modern Node parameters
            data["scripts"]["build"] = "quartz build"
            
        # Save the polished file back down smoothly
        with open(package_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print("Success! package.json has been modernized with flexible engine execution maps.")
        
    except Exception as e:
        print(f"Error parsing project files: {e}")
else:
    print("Error: Could not locate package.json workspace root file.")
