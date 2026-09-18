import os

ts_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\quartz.config.ts"

print("Modifying configuration layout to turn off third-party analytics trackers...")

if os.path.exists(ts_path):
    try:
        with open(ts_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        with open(ts_path, 'r', encoding='cp1252') as f:
            content = f.read()

    # Locate the analytics block and replace it with a clean, disabled state
    if "analytics: {" in content:
        # Find the block and rewrite it to completely remove third-party trackers
        old_analytics = """    analytics: {
      provider: "plausible",
    },"""
        
        new_analytics = """    analytics: null,"""
        
        if old_analytics in content:
            content = content.replace(old_analytics, new_analytics)
        else:
            # Fallback robust replacement if spacing differs slightly
            import re
            content = re.sub(r'analytics:\s*\{[^}]*\},', 'analytics: null,', content)

    with open(ts_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Success! Analytics module has been fully unlinked.")
else:
    print("Error: Could not locate quartz.config.ts file.")
