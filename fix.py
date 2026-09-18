import os

node_version_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\.node-version"

print("Fixing repository environmental lock files...")

# Force the environmental configuration file to request modern Node.js v22
try:
    with open(node_version_path, 'w', encoding='utf-8') as f:
        f.write("22.16.0\n")
    print("Success! .node-version file has been explicitly set to 22.16.0.")
except Exception as e:
    print(f"Error updating file path: {e}")
