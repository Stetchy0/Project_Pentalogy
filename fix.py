import os

config_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\quartz.config.default.yaml"
if not os.path.exists(config_path):
    config_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\quartz.config.yaml"

print("Injecting full Quartz structural parameters with vintage archive theme...")

# Complete, unbroken Quartz v4.5+ YAML configuration matrix containing mandatory layout arrays
complete_yaml = """configuration:
  pageTitle: "The Project Pentalogy"
  enableSPA: true
  enablePopovers: true
  analytics:
    provider: google
    tagId: ""
  locale: en-US
  baseUrl: projectpentalogy.netlify.app
  theme:
    fontOrigin: googleFonts
    cdnCaching: true
    typography:
      header: "Special Elite"
      body: "Courier Prime"
      code: "Share Tech Mono"
    colors:
      lightMode:
        light: "#f2ebd9"
        lightgray: "#dfd2b5"
        gray: "#a89470"
        darkgray: "#3d2d1e"
        dark: "#2b1e13"
        secondary: "#704829"
        highlight: "rgba(112, 72, 41, 0.1)"
        textHighlight: "#dfbe91"
      darkMode:
        light: "#1c1610"
        lightgray: "#2c2219"
        gray: "#6e5a47"
        darkgray: "#ded0bf"
        dark: "#ebdcc8"
        secondary: "#b58764"
        highlight: "rgba(181, 135, 100, 0.15)"
        textHighlight: "#7d5d3d"
plugins:
  transformers:
    - FrontMatter:
    - GitHubFlavoredMarkdown:
    - SyntaxHighlighting:
    - Links:
    - ObsidianFlavoredMarkdown:
    - Latex:
  filters:
    - ExplicitPublish:
  emitters:
    - Aliases:
    - Assets:
    - Static:
    - ComponentResources:
    - ContentPage:
    - TagPage:
    - FolderPage:
    - ContentIndex:
"""

with open(config_path, "w", encoding="utf-8") as f:
    f.write(complete_yaml)

print("Success! Configuration matrix rebuilt with mandatory filtering keys.")
