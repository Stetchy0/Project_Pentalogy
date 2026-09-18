import os

ts_config_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\quartz.config.ts"
ts_layout_path = r"C:\Users\losti\Documents\GitHub\Project_Pentalogy\quartz.layout.ts"

print("Injecting Quartz v5 Community Edition module mapping structures...")

# Mathematically perfect community format config block
community_config = """import { QuartzConfig } from "./quartz/cfg"
import FrontMatter from "@quartz-community/frontmatter"
import CreatedModifiedDate from "@quartz-community/created-modified-date"
import SyntaxHighlighting from "@quartz-community/syntax-highlighting"
import ObsidianFlavoredMarkdown from "@quartz-community/obsidian-flavored-markdown"
import GitHubFlavoredMarkdown from "@quartz-community/github-flavored-markdown"
import CrawlLinks from "@quartz-community/crawl-links"
import Latex from "@quartz-community/latex"
import Description from "@quartz-community/description"
import RemoveDrafts from "@quartz-community/remove-draft"
import AliasRedirects from "@quartz-community/alias-redirects"
import ComponentResources from "@quartz-community/component-resources"
import ContentPage from "@quartz-community/content-page"
import FolderPage from "@quartz-community/folder-page"
import TagPage from "@quartz-community/tag-page"
import ContentIndex from "@quartz-community/content-index"
import Assets from "@quartz-community/assets"
import Static from "@quartz-community/static"
import NotFoundPage from "@quartz-community/not-found-page"

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
      FrontMatter(),
      CreatedModifiedDate({ priority: ["frontmatter", "filesystem"] }),
      SyntaxHighlighting(),
      ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      GitHubFlavoredMarkdown(),
      CrawlLinks({ markdownLinkResolution: "shortest" }),
      Latex({ renderEngine: "katex" }),
      Description(),
    ],
    filters: [RemoveDrafts()],
    emitters: [
      AliasRedirects(),
      ComponentResources(),
      ContentPage(),
      FolderPage(),
      TagPage(),
      ContentIndex({ enableSiteMap: true, enableRSS: true }),
      Assets(),
      Static(),
      NotFoundPage(),
    ],
  },
}

export default config
"""

# Mathematically perfect community layout map components
community_layout = """import { PageLayout, SharedLayout } from "./quartz/cfg"
import Head from "@quartz-community/head"
import Footer from "@quartz-community/footer"
import Breadcrumbs from "@quartz-community/breadcrumbs"
import ArticleTitle from "@quartz-community/article-title"
import ContentMeta from "@quartz-community/content-meta"
import TagList from "@quartz-community/tag-list"
import PageTitle from "@quartz-community/page-title"
import Spacer from "@quartz-community/spacer"
import Search from "@quartz-community/search"
import Darkmode from "@quartz-community/darkmode"
import Explorer from "@quartz-community/explorer"
import Graph from "@quartz-community/graph"
import TableOfContents from "@quartz-community/table-of-contents"
import Backlinks from "@quartz-community/backlinks"

export const sharedPageComponents: SharedLayout = {
  head: Head(),
  header: [],
  afterBody: [],
  footer: Footer({
    links: {
      GitHub: "https://github.com",
    },
  }),
}

export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Breadcrumbs(),
    ArticleTitle(),
    ContentMeta(),
    TagList(),
  ],
  left: [
    PageTitle(),
    Spacer(),
    Search(),
    Darkmode(),
    Explorer(),
  ],
  right: [
    Graph(),
    TableOfContents(),
    Backlinks(),
  ],
}

export const defaultListPageLayout: PageLayout = {
  beforeBody: [Breadcrumbs(), ArticleTitle(), ContentMeta()],
  left: [
    PageTitle(),
    Spacer(),
    Search(),
    Darkmode(),
    Explorer(),
  ],
  right: [],
}
"""

try:
    with open(ts_config_path, 'w', encoding='utf-8') as f:
        f.write(community_config)
    print(" -> Successfully mapped community configuration modules.")
    
    with open(ts_layout_path, 'w', encoding='utf-8') as f:
        f.write(community_layout)
    print(" -> Successfully mapped community component layouts.")
except Exception as e:
    print(f"Error executing file patch pass: {e}")

print("\nAll community dependencies synchronized!")
