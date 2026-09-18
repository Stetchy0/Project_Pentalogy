import { PageLayout, SharedLayout } from "./quartz/cfg"
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
