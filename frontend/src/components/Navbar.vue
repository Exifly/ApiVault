<template>
  <nav class="glass-nav navbar-custom navbar navbar-expand-lg fixed-top">
    <div class="container-fluid">
      <router-link to="/" class="navbar-text-wrapper navbar-brand">
        <img :src="logoPath" alt="" width="30" height="30" />
        APIVault
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
          <li class="nav-item">
            <a
              class="navbar-text-wrapper nav-link active"
              aria-current="page"
              href="https://github.com/Exifly/ApiVault"
            >
              <font-awesome-icon :icon="['fab', 'github']" /> Stars
              {{ github.number.toFixed(0) }}
            </a>
          </li>
          <li class="nav-item">
            <a
              class="navbar-text-wrapper nav-link"
              href="https://github.com/Exifly/ApiVault/issues/new?assignees=&labels=add+api&template=add-your-api.md&title=%5BAPIFT%5D"
            >
              <font-awesome-icon :icon="['fas', 'angles-right']" /> Submit API
            </a>
          </li>
          <li class="nav-item">
            <a @click="setMode()" class="navbar-text-wrapper nav-link">
              <font-awesome-icon :icon="iconTheme" /> {{ iconThemeText }}
            </a>
          </li>
          <hr />
          <div id="scrollb" class="scrollbox">
            <div class="d-block d-sm-none">
              <h5 class="navbar-text-wrapper navbar-header-wrapper">MENU</h5>
              <li class="nav-item navbar-text-wrapper mt-2 category-custom">
                <router-link class="navbar-text-wrapper" to="/">
                  <font-awesome-icon
                    class="mx-2"
                    width="12"
                    height="12"
                    icon="fa-solid fa-house"
                  />Home</router-link
                >
              </li>
              <li class="nav-item navbar-text-wrapper mt-2 category-custom">
                <font-awesome-icon
                  class="mx-2"
                  width="12"
                  height="12"
                  :icon="['fab', 'github']"
                />Repository
              </li>
              <li class="nav-item navbar-text-wrapper mt-2 category-custom">
                <font-awesome-icon
                  class="mx-2"
                  width="12"
                  height="12"
                  icon="fa-solid fa-hand-holding-dollar"
                />Sponsor
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
                  class="navbar-text-wrapper"
                  :to="'/categories/' + category.name"
                >
                  <font-awesome-icon
                    class="mx-2"
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
const colorScheme = inject("colorScheme");
const categoriesAttributes = inject("categoryMapping");

var iconTheme = ref("fa-solid fa-sun");
var iconThemeText = ref("Dark Mode");
var logoPath = ref("/img/apivault-dark-nobg.png");

/**

Toggles the color scheme of the document body between light and dark mode. 
Updates the values of iconThemeText, colorScheme, logoPath, and iconTheme 
based on the new color scheme. Returns the new value of iconTheme to display.
@returns {String} - The new value of iconTheme to display
*/
const setMode = () => {
  const theme = document.body.getAttribute("data-theme");

  if (theme === "dark" || theme === null) {
    document.querySelector("body")?.setAttribute("data-theme", "light");
    iconThemeText.value = "Ligth Mode";
    colorScheme.value = "dark";
    logoPath.value = "/img/apivault-light-nobg.png";
    return (iconTheme.value = "fa-solid fa-moon");
  } else {
    document.querySelector("body")?.setAttribute("data-theme", "dark");
    iconThemeText.value = "Dark Mode";
    colorScheme.value = "light";
    logoPath.value = "/img/apivault-dark-nobg.png";
    return (iconTheme.value = "fa-solid fa-sun");
  }
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
@media (min-width: 1281px) and (max-width: 1572px) {
  .navbar-custom {
    width: 100vw;
  }
  .custom-props-navbar {
    position: fixed;
    width: 100vw;
  }
}

@media (min-width: 1025px) and (max-width: 1280px) {
  .navbar-custom {
    height: 8vh;
    width: 100vw;
  }
  .custom-props-navbar {
    position: fixed;
    width: 100%;
  }
}

@media only screen and (max-width: 680px) {
  .navbar-custom {
    width: 100%;
  }
  .glass-nav {
    background-color: var(--bg-color);
  }
  .scrollbox {
    overflow: scroll;
    height: 76vh !important;
  }
}

::-webkit-scrollbar {
  width: 0px;
}

.scrollbox {
  overflow: scroll;
  height: 0;
}

.navbar-custom {
  background-color: var(--bg-color);
  width: 100vw;
}

.navbar-text-wrapper {
  color: var(--text-color) !important;
  text-decoration: none;
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

@media (min-width: 1572px) {
  .navbar-custom {
    width: 100vw;
    margin-left: 11.3vw;
  }
  .custom-props-navbar {
    position: fixed;
    width: 100vw;
  }
}

.nav-item:hover {
  color: var(--nav-item-hover);
  scale: 1.05;
}
</style>
