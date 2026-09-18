import os

config_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\quartz.config.default.yaml"

if not os.path.exists(config_path):
    # Fallback check if the file is named quartz.config.yaml instead
    config_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\quartz.config.yaml"

print("Injecting clean YAML formatting to fix the block error...")

try:
    with open(config_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
except Exception:
    with open(config_path, "r", encoding="cp1252") as f:
        lines = f.readlines()

new_lines = []
skip_mode = False

for line in lines:
    # Look for the start of the typography block
    if "typography:" in line:
        # Inject perfectly spaced lines (4 spaces for typography, 6 spaces for fonts)
        new_lines.append("    typography:\n")
        new_lines.append('      header: "Special Elite"\n')
        new_lines.append('      body: "Courier Prime"\n')
        new_lines.append('      code: "Share Tech Mono"\n')
        skip_mode = True
        continue
    
    # Stop skipping once we hit the colors block
    if "colors:" in line and skip_mode:
        skip_mode = False
        
    if not skip_mode:
        new_lines.append(line)

with open(config_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Success! Spacing has been permanently repaired.")
