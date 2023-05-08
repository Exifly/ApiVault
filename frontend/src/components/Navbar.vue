<template>
  <nav class="glass-nav navbar-custom navbar navbar-expand-lg fixed-top">
    <div class="container-fluid">
      <router-link to="/" class="navbar-text-wrapper navbar-brand">
        <img :src="logoPath" alt="" width="150" />
      </router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span
          ><font-awesome-icon
            :icon="['fas', 'bars']"
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
            >
              <font-awesome-icon :icon="['fab', 'github']" /> Stars
              {{ github.number.toFixed(0) }}
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
            <a @click="setMode()" class="navbar-text-wrapper flex items-center gap-2">
              <font-awesome-icon :icon="iconTheme" /> {{ iconThemeText }}
            </a>
          </li>
          <hr />
          <div id="scrollb" class="scrollbox">
            <div class="d-block d-sm-none">
              <h5 class="navbar-text-wrapper navbar-header-wrapper">MENU</h5>
              <li class="nav-item navbar-text-wrapper mt-2 category-custom">
                <router-link class="navbar-text-wrapper flex items-center gap-2" to="/">
                  <font-awesome-icon
                    class=""
                    width="12"
                    height="12"
                    icon="fa-solid fa-house"
                  />Home</router-link
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
                <router-link class="navbar-text-wrapper flex items-center gap-2" to="/contributors">
                  <font-awesome-icon
                    class=""
                    width="12"
                    height="12"
                    icon="fa-solid fa-users"
                  />Contributors</router-link
                >
              </li>
              <hr />
              <h5 class="navbar-text-wrapper navbar-header-wrapper">
                CATEGORIES
              </h5>
              <li
                class="nav-item navbar-text-wrapper mt-2 category-custom"
                v-for="category in categoriesAttributes"
                :key="category"
              >
                <router-link
                  class="navbar-text-wrapper flex items-center gap-2"
                  :to="'/categories/' + category.name"
                >
                  <font-awesome-icon
                    class=""
                    width="12"
                    height="12"
                    :icon="category.icon"
                  />{{ category.name }}</router-link
                >
              </li>
            </div>
          </div>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, inject, reactive, onMounted, watch } from "vue";
import { CSSPlugin } from "gsap/CSSPlugin";
import getStars from "@/components/api/githubStarsApi.js";
import axios from "axios";
import gsap from "gsap";

gsap.registerPlugin(CSSPlugin);

const number = ref(0);
const github = reactive({
  number: 0,
});
const theme = inject("theme");
const categoriesAttributes = inject("categoryMapping");
const themeIcons = {
  light: "fa-solid fa-sun",
  dark: "fa-solid fa-moon"
}
const iconTheme = ref(themeIcons[theme.value]);
const iconThemeText = ref(theme.value[0].toUpperCase() + theme.value.slice(1, theme.value.length) + " Mode");
const logoPath = ref(`/img/apivault-full-${theme.value}-nobg.png`);

/**

Toggles the color scheme of the document body between light and dark mode. 
Updates the values of iconThemeText, theme, logoPath, and iconTheme 
based on the new color scheme. Returns the new value of iconTheme to display.
@returns {String} - The new value of iconTheme to display
*/
const setMode = () => {
  if (theme.value === "dark" || theme.value === undefined) {
    theme.value = "light";
    localStorage.setItem("APIVaultTheme", "light");
  } else {
    theme.value = "dark";
    localStorage.setItem("APIVaultTheme", "dark");
  }
  const themeText = theme.value[0].toUpperCase() + theme.value.slice(1, theme.value.length) + " Mode";

  document.querySelector("body")?.setAttribute("data-theme", theme.value);
  iconThemeText.value = themeText;
  iconTheme.value = themeIcons[theme.value];
  logoPath.value = `/img/apivault-full-${theme.value}-nobg.png`;
};

/**
Fetch repository data using github Api and get the stars count
*/
const githubData = async () => {
  let data = await getStars();
  number.value = data.stargazers_count;
};

if (window.screen.height > 768) {
  document.querySelectorAll("#scrollb").remove;
}

/**
Watch for number variable ref to change and apply an animation to it
 */
watch(number, (n) => {
  gsap.to(github, { duration: 0.5, number: Number(n) || 0 });
});

onMounted(() => {
  githubData();
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
  padding: .3rem .2rem; 
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
