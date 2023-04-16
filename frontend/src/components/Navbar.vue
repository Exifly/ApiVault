<script setup>
import { ref, inject, reactive, onMounted, watch } from "vue";
import axios from "axios";
import gsap from "gsap";
import { CSSPlugin } from "gsap/CSSPlugin";

// =================== PRE LOGIC SIDE =================== //
gsap.registerPlugin(CSSPlugin);

// =================== DATA DEFINITION =================== //
const number = ref(0);
const github = reactive({
  number: 0,
});
const colorScheme = inject("colorScheme");

var iconTheme = ref("fa-solid fa-sun");
var iconThemeText = ref("Dark Mode");
var logoPath = ref("/img/apivault-dark-nobg.png");

// =================== FUNCTION & METHODS =================== //
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
        </ul>
      </div>
    </div>
  </nav>
</template>

<style>
.navbar-custom {
  background-color: var(--bg-color);
  width: 100vw;
}

.navbar-text-wrapper {
  color: var(--text-color) !important;
}

.glass-nav {
  backdrop-filter: blur(16px) saturate(200%);
  -webkit-backdrop-filter: blur(16px) saturate(200%);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  background-color: rgba(var(--bg-color), 0.76);
  border-radius: 12px;
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
}
</style>
