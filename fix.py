import os
import json

repo_root = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy"
vercel_json_path = os.path.join(repo_root, "vercel.json")

print("Generating official Vercel routing header file...")

# Explicit routing properties that force Vercel to render your HTML/CSS maps with perfect browser flags
pristine_vercel_json = {
    "version": 2,
    "cleanUrls": True,
    "trailingSlash": False,
    "routes": [
        {
            "src": "/style.css",
            "headers": { "cache-control": "s-maxage=31536000,max-age=0" },
            "dest": "/prof/style.css"
        },
        {
            "src": "/Art/(.*)",
            "dest": "/prof/Art/$1"
        },
        {
            "src": "/(.*)",
            "dest": "/prof/$1"
        }
    ]
}

try:
    with open(vercel_json_path, 'w', encoding='utf-8') as f:
        json.dump(pristine_vercel_json, f, indent=2)
    print("Success! vercel.json configuration manifest has been written to the repository root.")
except Exception as e:
    print(f"Error creating vercel routing lock file: {e}")
