import os

config_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\quartz.config.default.yaml"
if not os.path.exists(config_path):
    config_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\quartz.config.yaml"

print("Injecting valid linkCasing parameter rule to fix line 4 syntax error...")

try:
    with open(config_path, "r", encoding="utf-8") as f:
        content = f.read()
except Exception:
    with open(config_path, "r", encoding="cp1252") as f:
        content = f.read()

# 1. Clean out the broken line 4 patch from the previous step
if "slugify: true" in content:
    content = content.replace("    slugify: true\n", "")
    content = content.replace("    slugify: true", "")

# 2. Inject the official Quartz configuration rule directly into the theme settings block
if "linkCasing:" not in content:
    if "theme:" in content:
        # Places the casing rule precisely underneath the theme definition panel row
        content = content.replace(
            "  theme:",
            "  theme:\n    linkCasing: lowercase"
        )
        print("Success! Integrated native linkCasing mapping rules.")
    else:
        print("Error: Could not locate theme header block.")
else:
    print("Official link casing patch already present.")

with open(config_path, "w", encoding="utf-8") as f:
    f.write(content)

print("YAML cleanup complete!")
