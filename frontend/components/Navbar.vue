<template>
  <nav class="glass-nav navbar-custom navbar navbar-expand-lg fixed-top">
    <div class="container-fluid">
      <NuxtLink to="/" class="navbar-text-wrapper navbar-brand">
        <img :src="logoPath" alt="logo" width="150" />
      </NuxtLink>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span>
          <font-awesome-icon
            icon="fa-solid fa-bars"
            style="color: var(--text-color)"
        /></span>
      </button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item navbar-text-wrapper mt-2">
            <a
              class="navbar-text-wrapper flex items-center gap-2 active"
              aria-current="page"
              href="https://github.com/Exifly/ApiVault"
              target="_blank"
            >
              <font-awesome-icon :icon="['fab', 'github']" />
              Stars {{ stargazers }}
            </a>
          </li>
          <li class="nav-item navbar-text-wrapper mt-2">
            <a
              class="navbar-text-wrapper flex items-center gap-2"
              href="https://github.com/Exifly/ApiVault/issues/new?assignees=&labels=add+api&template=add-your-api.md&title=%5BAPIFT%5D"
            >
              <font-awesome-icon :icon="['fas', 'angles-right']" /> Submit API
            </a>
          </li>
          <li class="nav-item navbar-text-wrapper mt-2">
            <ToggleButton
              @click="setModeLocal"
              :theme="theme"
              class="flex items-center gap-2 ms-2"
            />
          </li>
          <hr />
          <div id="scrollb" class="scrollbox">
            <div class="d-block d-sm-none">
              <h5 class="navbar-text-wrapper navbar-header-wrapper">MENU</h5>
              <li class="nav-item navbar-text-wrapper mt-2 category-custom">
                <NuxtLink
                  class="navbar-text-wrapper flex items-center gap-2"
                  to="/"
                >
                  <font-awesome-icon
                    class=""
                    width="12"
                    height="12"
                    icon="fa-solid fa-house"
                  />Home</NuxtLink
                >
              </li>
              <li class="nav-item navbar-text-wrapper mt-2 category-custom">
                <a
                  class="navbar-text-wrapper flex items-center gap-2"
                  style="text-decoration: none"
                  href="https://github.com/Exifly/ApiVault"
                >
                  <font-awesome-icon
                    class=""
                    width="12"
                    height="12"
                    :icon="['fab', 'github']"
                  />Repository</a
                >
              </li>
              <li class="nav-item navbar-text-wrapper mt-2 category-custom">
                <a
                  class="navbar-text-wrapper flex items-center gap-2"
                  style="text-decoration: none"
                  href="https://www.buymeacoffee.com/exifly"
                >
                  <font-awesome-icon
                    class=""
                    width="12"
                    height="12"
                    icon="fa-solid fa-hand-holding-dollar"
                  />Sponsor</a
                >
              </li>
              <li class="nav-item navbar-text-wrapper mt-2 category-custom">
                <NuxtLink
                  class="navbar-text-wrapper flex items-center gap-2"
                  to="/contributors"
                >
                  <font-awesome-icon
                    class=""
                    width="12"
                    height="12"
                    icon="fa-solid fa-users"
                  />Contributors</NuxtLink
                >
              </li>
              <hr />
              <h5 class="navbar-text-wrapper navbar-header-wrapper">
                CATEGORIES
              </h5>
              <li
                class="nav-item navbar-text-wrapper mt-2 category-custom"
                v-for="category in categoriesAttributes"
                :key="category.name"
              >
                <NuxtLink
                  class="navbar-text-wrapper flex items-center gap-2"
                  :to="'/categories/' + category.name"
                >
                  <font-awesome-icon
                    class=""
                    width="12"
                    height="12"
                    :icon="category.icon"
                  />{{ category.name }}</NuxtLink
                >
              </li>
            </div>
          </div>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script lang="ts" setup>
import { categoriesProperties } from "../utils/categoryMapping";
import GithubService from "../services/GithubServices";
import {
  getThemeElements,
  themeIcons,
  setThemeLogoPath,
  setLocalStorage,
} from "../utils/themeutils";

const stargazers = await GithubService.repoStars();
console.log(stargazers);
const categoriesAttributes = categoriesProperties;
const theme = useState("APIVaultTheme", () =>
  process.client ? localStorage.getItem("APIVaultTheme")! : "light"
);
const iconTheme = ref(themeIcons[theme.value]);
const logoPath = ref(setThemeLogoPath(theme));

/**
Toggles the color scheme of the document body between light and dark mode.
Updates the values of iconThemeText, theme, logoPath, and iconTheme
based on the new color scheme. Returns the new value of iconTheme to display.
@returns {String} - The new value of iconTheme to display
*/
let defaultTheme = ref<boolean>(true);
const setModeLocal = (): void => {
  if (process.client) {
    defaultTheme.value = setLocalStorage(theme);
    defaultTheme.value = getThemeElements(theme);
  }
  iconTheme.value = themeIcons[theme.value];
  logoPath.value = setThemeLogoPath(theme);
};

/**
This is needed to set the dafault theme class for first
visit on the website.
*/
useHead({
  htmlAttrs: {
    class: computed(() => {
      return defaultTheme.value ? "" : "light";
    }),
  },
});

onMounted(() => {
  theme.value = setTheme();
  const isDarkTheme: boolean =
    theme.value === "dark" || theme.value === null ? true : false;
  defaultTheme.value = isDarkTheme;
  iconTheme.value = themeIcons[theme.value];
  logoPath.value = setThemeLogoPath(theme);
});
</script>

<style scoped>
::-webkit-scrollbar {
  width: 0px;
}

.scrollbox {
  overflow: scroll;
  height: 0;
}

.navbar-custom {
  margin-left: 10px;
  background-color: var(--bg-color);
}

.navbar-text-wrapper {
  color: var(--text-color) !important;
  text-decoration: none;
  padding: 0.3rem 0.2rem;
  border-radius: 5px;
}

.navbar-header-wrapper {
  font-weight: 600;
}

.glass-nav {
  backdrop-filter: blur(16px) saturate(200%);
  -webkit-backdrop-filter: blur(16px) saturate(200%);
  background-color: rgba(var(--bg-color), 0.76);
}

.custom-radius {
  border-radius: var(--border-radius);
}

.custom-props-navbar {
  position: fixed;
  width: 100%;
}

.nav-item:hover {
  cursor: pointer;
  color: var(--nav-item-hover);
  background-color: var(--bg-card-glass-hover);
  cursor: pointer;
  border-radius: 5px;
}

@media (min-width: 1025px) and (max-width: 1280px) {
  .navbar-custom {
    height: 8vh;
  }
}

@media (min-width: 1572px) {
  .navbar-custom {
    max-width: calc(100vw - (11.3vw * 2));
    margin: auto;
  }
}

@media only screen and (max-width: 680px) {
  .glass-nav {
    background-color: var(--bg-color);
  }
  .scrollbox {
    overflow: scroll;
    height: 73vh !important;
  }
}
</style>
