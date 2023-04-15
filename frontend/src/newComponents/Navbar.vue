<script setup>
import { ref } from "vue";

const stars = 104;
var iconTheme = ref("fa-solid fa-sun");
var iconMenuToggleColor = ref("#fff");
var iconThemeText = ref("Dark Mode");

const setMode = () => {
  const theme = document.body.getAttribute("data-theme");

  if (theme === "dark" || theme === null) {
    document.querySelector("body")?.setAttribute("data-theme", "light");
    iconThemeText.value = "Ligth Mode";
    return (iconTheme.value = "fa-solid fa-moon");
  } else {
    document.querySelector("body")?.setAttribute("data-theme", "dark");
    iconThemeText.value = "Dark Mode";
    return (iconTheme.value = "fa-solid fa-sun");
  }
};
</script>

<template>
  <nav class="glass-nav navbar-custom navbar navbar-expand-lg fixed-top">
    <div class="container-fluid">
      <router-link to="/" class="navbar-text-wrapper navbar-brand">
        <img src="../assets/img/logo.jpeg" alt="" width="30" height="30" />
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
              <font-awesome-icon :icon="['fab', 'github']" /> Stars {{ stars }}
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

@media (min-width: 1281px) {
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
