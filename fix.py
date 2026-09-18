import os

ts_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\quartz.config.ts"

print("Stripping out conflicting description modules to restore code integrity...")

if os.path.exists(ts_path):
    try:
        with open(ts_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        with open(ts_path, 'r', encoding='cp1252') as f:
            content = f.read()

    # Locate and completely extract the broken description line tracker
    if "Plugin.Description()" in content:
        content = content.replace("      Plugin.Description(),\n", "")
        content = content.replace("      Plugin.Description(),", "")
        print("Success! Conflicting block unlinked from configuration list.")
    else:
        print("Note: Description line was already modified or removed.")

    with open(ts_path, 'w', encoding='utf-8') as f:
        f.write(content)
else:
    print("Error: Could not locate quartz.config.ts file.")
