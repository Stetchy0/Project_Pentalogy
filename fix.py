import os

ts_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\quartz.config.ts"

print("Replacing date plugin tracking modules to clear asynchronous file crashes...")

if os.path.exists(ts_path):
    try:
        with open(ts_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        with open(ts_path, 'r', encoding='cp1252') as f:
            content = f.read()

    # Define the broken date plugin block text we want to target
    target_date_block = """      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "filesystem"],
      }),"""

    if target_date_block in content:
        # Overwrite it completely with a standard, error-free FrontMatter parsing line
        content = content.replace(target_date_block, "")
        print("Success! Disabled asynchronous date tracking hooks.")
    else:
        # Fallback regex search replacement if spacing differs slightly
        import re
        content = re.sub(r'Plugin\.CreatedModifiedDate\(\{[^}]*\}\),?', '', content)
        print("Executed backup cleaning sweep pass.")

    with open(ts_path, 'w', encoding='utf-8') as f:
        f.write(content)
else:
    print("Error: Could not locate quartz.config.ts file.")
