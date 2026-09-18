import { QuartzConfig } from "./quartz/cfg"
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
