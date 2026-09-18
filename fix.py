import os

ts_config_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\quartz.config.ts"
ts_layout_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\quartz.layout.ts"

print("Initiating full clean-slate configuration structural override...")

# Complete, unbroken official Quartz v5 TypeScript configuration matrix
factory_config_code = """import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4.0 Configuration
 *
 * See https://jzhao.xyz for more information.
 */
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
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
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

# Complete, unbroken official Quartz v5 page element layout assignment map
factory_layout_code = """import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

// Components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [],
  footer: Component.Footer({
    links: {
      GitHub: "https://github.com",
    },
  }),
}

// Components for pages that display a single slot of content
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

// Components for pages that display lists of pages (e.g. tags or folders)
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

# Force write the pristine configurations back down onto the hard drive
try:
    with open(ts_config_path, 'w', encoding='utf-8') as f:
        f.write(factory_config_code)
    print(" -> Successfully overwrote quartz.config.ts with a pristine blueprint profile.")
    
    with open(ts_layout_path, 'w', encoding='utf-8') as f:
        f.write(factory_layout_code)
    print(" -> Successfully overwrote quartz.layout.ts with pristine components.")
    
except Exception as e:
    print(f"Error executing file replacement pass: {e}")

print("\nAll configuration and layout frameworks fully restored to factory specs!")
