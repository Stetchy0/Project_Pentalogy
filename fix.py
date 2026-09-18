import os

ts_config_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\quartz.config.ts"
ts_layout_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\quartz.layout.ts"
yaml_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\quartz.config.default.yaml"
if not os.path.exists(yaml_path):
    yaml_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\quartz.config.yaml"

print("Initiating full repository system calibration restorer...")

# 1. Pristine factory-standard Quartz 5 config file with your custom beige palette
perfect_config_code = """import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

const config: QuartzConfig = {
  configuration: {
    pageTitle: "The Project Pentalogy",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
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
      Plugin.CreatedModifiedDate({ priority: ["frontmatter", "filesystem"] }),
      Plugin.SyntaxHighlighting({ theme: { light: "github-light", dark: "github-dark" } }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Latex({ renderEngine: "katex" }),
      Plugin.Description(),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({ enableSiteMap: true, enableRSS: true }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config
"""

# 2. Pristine factory-standard Quartz 5 layout map file to heal component tracking errors
perfect_layout_code = """import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [],
  footer: Component.Footer({
    links: {
      GitHub: "https://github.com/jackyzha0/quartz",
    },
  }),
}

export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.Breadcrumbs(),
    Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.DesktopOnly(Component.Explorer()),
  ],
  right: [
    Component.Graph(),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
  ],
}

export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.DesktopOnly(Component.Explorer()),
  ],
  right: [],
}
"""

with open(ts_config_path, "w", encoding="utf-8") as f:
    f.write(perfect_config_code)
print(" -> Successfully overwrote configuration matrices.")

with open(ts_layout_path, "w", encoding="utf-8") as f:
    f.write(perfect_layout_code)
print(" -> Successfully restored factory layout structures.")

if os.path.exists(yaml_path):
    with open(yaml_path, "w", encoding="utf-8") as f:
        f.write("# Repaired track line marker\n")
    print(" -> Successfully scrubbed residual YAML artifacts.")

print("\nAll systemic configuration models re-aligned perfectly!")
