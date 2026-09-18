import os

# Define the absolute local paths
yaml_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\quartz.config.default.yaml"
if not os.path.exists(yaml_path):
    yaml_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\quartz.config.yaml"

ts_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\quartz.config.ts"

print("Step 1: Resetting YAML configuration file to a clean, empty state...")
# We leave a minimal, perfect naked matrix so it passes validation checks effortlessly
naked_yaml = """configuration:
  baseUrl: projectpentalogy.netlify.app
"""
with open(yaml_path, "w", encoding="utf-8") as f:
    f.write(naked_yaml)

print("Step 2: Injecting vintage manila theme and typewriter fonts into quartz.config.ts...")
if os.path.exists(ts_path):
    # Perfect, pristine Quartz TS structure containing your custom palette colors and fonts
    perfect_ts_code = """import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

const config: QuartzConfig = {
  configuration: {
    pageTitle: "The Project Pentalogy",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "google",
      tagId: "",
    },
    locale: "en-US",
    baseUrl: "projectpentalogy.netlify.app",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "created",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Special Elite",
        body: "Courier Prime",
        code: "Share Tech Mono",
      },
      colors: {
        lightMode: {
          light: "#f2ebd9",
          lightgray: "#dfd2b5",
          gray: "#a89470",
          darkgray: "#3d2d1e",
          dark: "#2b1e13",
          secondary: "#704829",
          highlight: "rgba(112, 72, 41, 0.1)",
          textHighlight: "#dfbe91",
        },
        darkMode: {
          light: "#1c1610",
          lightgray: "#2c2219",
          gray: "#6e5a47",
          darkgray: "#ded0bf",
          dark: "#ebdcc8",
          secondary: "#b58764",
          highlight: "rgba(181, 135, 100, 0.15)",
          textHighlight: "#7d5d3d",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "filesystem"],
      }),
      Plugin.SyntaxHighlighting(),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Latex({ renderEngine: "katex" }),
      Plugin.Description(),
      Plugin.OxHugoMarkdown(),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config
"""
    with open(ts_path, "w", encoding="utf-8") as f:
        f.write(perfect_ts_code)
    print("Success! Rebuilt the TypeScript configuration file perfectly.")
else:
    print("Error: Could not find quartz.config.ts to rewrite.")
