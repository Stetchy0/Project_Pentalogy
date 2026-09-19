import os
import json

repo_root = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy"
package_json_path = os.path.join(repo_root, "package.json")
lock_json_path = os.path.join(repo_root, "quartz.lock.json")

print("Injecting Quartz Community packages directly into standard project dependencies...")

# 1. Update package.json to manage community plugins directly via NPM
if os.path.exists(package_json_path):
    try:
        with open(package_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # Ensure dependencies dictionary block exists
        if "dependencies" not in data:
            data["dependencies"] = {}
            
        # Force-inject all your required layout modules directly into standard tracking elements
        plugins_to_add = {
            "@quartz-community/frontmatter": "^1.0.0",
            "@quartz-community/created-modified-date": "^1.0.1",
            "@quartz-community/syntax-highlighting": "^1.0.1",
            "@quartz-community/obsidian-flavored-markdown": "^1.0.0",
            "@quartz-community/github-flavored-markdown": "^1.0.0",
            "@quartz-community/crawl-links": "^1.0.0",
            "@quartz-community/latex": "^1.0.0",
            "@quartz-community/description": "^1.0.0",
            "@quartz-community/remove-draft": "^1.0.0",
            "@quartz-community/alias-redirects": "^1.0.0",
            "@quartz-community/component-resources": "^1.0.0",
            "@quartz-community/content-page": "^1.0.0",
            "@quartz-community/folder-page": "^1.0.0",
            "@quartz-community/tag-page": "^1.0.0",
            "@quartz-community/content-index": "^1.0.0",
            "@quartz-community/assets": "^1.0.0",
            "@quartz-community/static": "^1.0.0",
            "@quartz-community/not-found-page": "^1.0.0",
            "@quartz-community/head": "^1.0.0",
            "@quartz-community/footer": "^1.0.0",
            "@quartz-community/breadcrumbs": "^1.0.0",
            "@quartz-community/article-title": "^1.0.0",
            "@quartz-community/content-meta": "^1.0.0",
            "@quartz-community/tag-list": "^1.0.0",
            "@quartz-community/page-title": "^1.0.0",
            "@quartz-community/spacer": "^1.0.0",
            "@quartz-community/search": "^1.0.0",
            "@quartz-community/darkmode": "^1.0.0",
            "@quartz-community/explorer": "^1.0.0",
            "@quartz-community/graph": "^1.0.0",
            "@quartz-community/table-of-contents": "^1.0.0",
            "@quartz-community/backlinks": "^1.0.0"
        }
        
        for key, value in plugins_to_add.items():
            data["dependencies"][key] = value
            
        with open(package_json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print(" -> Successfully merged community layout hooks into package.json.")
    except Exception as e:
        print(f" Error updating package.json: {e}")

# 2. Erase the conflicting quartz.lock.json file so the builder completely skips the broken plugin script track
if os.path.exists(lock_json_path):
    try:
        os.remove(lock_json_path)
        print(" -> Extracted quartz.lock.json to skip custom installer loops.")
    except Exception as e:
        print(f" Error unlinking file: {e}")

print("\nWorkspace dependencies optimized! Ready to ship.")
