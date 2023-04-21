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
      <div class="collapse navbar-collapse" id="navbarNav">
        <div class="scrollbox">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a
                class="navbar-text-wrapper nav-link active"
                aria-current="page"
                href="#"
              >
                <font-awesome-icon :icon="['fab', 'github']" /> Stars
                {{ github.number.toFixed(0) }}
              </a>
            </li>
            <li class="nav-item">
              <a class="navbar-text-wrapper nav-link" href="#">
                <font-awesome-icon :icon="['fas', 'angles-right']" /> Submit API
              </a>
            </li>
            <li class="nav-item">
              <a @click="setMode()" class="navbar-text-wrapper nav-link">
                <font-awesome-icon :icon="iconTheme" /> {{ iconThemeText }}
              </a>
            </li>
            <hr />
            <h5 class="navbar-text-wrapper navbar-header-wrapper">MENU</h5>
            <li class="navbar-text-wrapper mt-2 category-custom">
              <router-link class="navbar-text-wrapper" to="/">
                <font-awesome-icon
                  class="mx-2"
                  width="12"
                  height="12"
                  icon="fa-solid fa-house"
                />Home</router-link
              >
            </li>
            <li class="navbar-text-wrapper mt-2 category-custom">
              <font-awesome-icon
                class="mx-2"
                width="12"
                height="12"
                :icon="['fab', 'github']"
              />Repository
            </li>
            <li class="navbar-text-wrapper mt-2 category-custom">
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
              class="navbar-text-wrapper mt-2 category-custom"
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
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, inject, reactive, onMounted, watch } from "vue";
import axios from "axios";
import gsap from "gsap";
import { CSSPlugin } from "gsap/CSSPlugin";

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

const setMode = () => {
  // set night or light mode
  const theme = document.body.getAttribute("data-theme");

  if (theme === "dark" || theme === null) {
    document.querySelector("body")?.setAttribute("data-theme", "light");
    iconThemeText.value = "Ligth Mode"; // to change icon style
    colorScheme.value = "dark";
    logoPath.value = "/img/apivault-light-nobg.png";
    return (iconTheme.value = "fa-solid fa-moon"); // return icon to display
  } else {
    document.querySelector("body")?.setAttribute("data-theme", "dark");
    iconThemeText.value = "Dark Mode";
    colorScheme.value = "light";
    logoPath.value = "/img/apivault-dark-nobg.png";
    return (iconTheme.value = "fa-solid fa-sun");
  }
};

const githubData = async () => {
  await axios
    .get("https://api.github.com/repos/exifly/tweetyfly")
    .then((res) => {
      number.value = res.data.stargazers_count;
    })
    .catch((er) => {
      console.log(er.response.data.message);
    });
};

// =================== COMPONENT LOGIC =================== //
watch(number, (n) => {
  gsap.to(github, { duration: 0.5, number: Number(n) || 0 });
});

onMounted(() => {
  githubData();
});
</script>

<style>
::-webkit-scrollbar {
  width: 0px;
}

.scrollbox {
  overflow: scroll;
  height: 89vh;
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

@media only screen and (min-heigth: 680px) {
  .navbar-custom {
    width: 100%;
  }
  .glass-nav {
    background-color: var(--bg-color);
  }
}
</style>
