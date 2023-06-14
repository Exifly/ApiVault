import { resolve } from "path";
import { categoriesProperties } from "./utils/categoryMapping";


export default defineNuxtConfig({
  components: true,
  alias: {
    '@': resolve(__dirname, "/")
  },
  plugins: [
    '@/plugins/fontawesome',
  ],
  modules: [
    'nuxt-simple-sitemap',
    [
      '@nuxtjs/robots', 
      { configPath: '~/config/robots.config' }
    ]
  ],
  sitemap: {
    siteUrl: 'https://apivault.dev',
    urls: async () => {
      return categoriesProperties.map(category => ({
        loc: `/categories/${category.name.replace('\&', '\&amp;')}`,
        lastmod: new Date(),
        changefreq: 'daily',
        priority: 0.2,
      }))
    },
    defaults: {
      changefreq: 'daily',
      priority: 0.5,
      lastmod: new Date()
    }
  },
  app: {
    pageTransition: {
      name: "page",
      mode: "out-in",
    },
    head: {
      htmlAttrs: {
        lang: 'en',
      },
      title: "A free API database list for developers",
      meta: [
        { name: "keywords", content: "free api, free api list, apivault, free apis for projects, open-source, public APIs, free apis for learning, free apis to use" },
        { name: "description", content: "ApiVault - The largest collection of free and public APIs, categorized for easy search." },
        { name: "author", content: "exifly"},
        { name: "twitter:title", content: "A free API database list for developers"},
        { name: "twitter:description", content: "ApiVault - The largest collection of free public APIs, categorized for easy search."},
        { name: "twitter:url", content: "https://apivault.dev/"},
        { name: "twitter:card", content: "summary_large_image"},
        { name: "twitter:site", content: "apivault"},
        { name: "twitter:keywords", content: "free api, free api list, apivault, free apis for projects, open-source, public APIs, free apis for learning, free apis to use"},
        { name: "twitter:image", content: "https://raw.githubusercontent.com/Exifly/ApiVault/main/assets/Hero.jpg"},
        { property: "og:title", content: "A free API database list for developers"},
        { property: "og:description", content: "ApiVault - The largest collection of free public APIs, categorized for easy search."},
        { property: "og:site_name", content: "APIVault"},
        { property: "og:url", content: "https://apivault.dev/"},
        { property: "og:image", content: "https://raw.githubusercontent.com/Exifly/ApiVault/main/assets/Hero.jpg" },
        { property: "og:type", content: "website"}
      ]
    }
  },
  css: [
    '~/assets/styles/bootstrap.scss',
    '~/assets/styles/main.css', 
    '~/assets/styles/normalize.css',
    '~/assets/styles/animations.scss',
    '@fortawesome/fontawesome-svg-core/styles.css'
  ],
  build: {
    transpile: ['@fortawesome/vue-fontawesome']
  },
})
