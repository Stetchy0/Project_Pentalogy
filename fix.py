import os

config_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\quartz.config.default.yaml"
if not os.path.exists(config_path):
    config_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\quartz.config.yaml"

print("Injecting Quartz lowercase slug patch to permanently break routing loops...")

try:
    with open(config_path, "r", encoding="utf-8") as f:
        content = f.read()
except Exception:
    with open(config_path, "r", encoding="cp1252") as f:
        content = f.read()

# Check if the slugify configuration is already explicitly defined
if "slugify:" not in content:
    # Find the configuration: block to safely insert the lowercase rule patch
    if "configuration:" in content:
        patched_content = content.replace(
            "configuration:",
            "configuration:\n    slugify: true"
        )
        
        with open(config_path, "w", encoding="utf-8") as f:
            f.write(patched_content)
        print("Success! Enforced global lowercase link formatting rules.")
    else:
        print("Error: Could not locate configuration header block.")
else:
    print("Patch already active inside configuration profile.")
