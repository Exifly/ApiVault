<script setup>
import Logo from "./Logo.vue";
import { ref, inject, reactive, computed } from "vue";

const state = reactive({
  theme: "dark",
});

// Compute the image source based on the current theme
const imageSource = computed(() => {
  if (state.theme === "dark") {
    return "/public/img/apivault-dark-nobg.png";
  } else {
    return "/public/img/apivault-light-nobg.png";
  }
});

// Watch for changes to the data-theme attribute and update the state
const observer = new MutationObserver((mutationsList) => {
  mutationsList.forEach((mutation) => {
    if (
      mutation.type === "attributes" &&
      mutation.attributeName === "data-theme"
    ) {
      state.theme = mutation.target.getAttribute("data-theme");
    }
  });
});
observer.observe(document.body, { attributes: true });
</script>

<template>
  <center>
    <Logo :source="imageSource" height="150" width="150" />
  </center>
  <h1 class="hero-text-wrapper page-title p-3 p-md-5">
    Your Gateway to a World of Public APIs.
    <h5>This tool is completely free and Open-Source!</h5>
  </h1>
</template>

<style scoped>
.page-title {
  align-items: center;
  justify-content: center;
  text-transform: capitalize;
}
.page-subtitle {
  color: white;
}
.glass-card {
  backdrop-filter: blur(16px) saturate(200%);
  -webkit-backdrop-filter: blur(16px) saturate(200%);
  background-color: var(--bg-card-glass);
  /* background-color: rgba(var(--bg-color), 0.78); */
  border-radius: 12px;
  border: 1px solid var(--border-color-cards);
}
.hero-card {
  margin-left: 15vw;
  margin-right: 15vw;
  margin-bottom: 4vh;
  width: 30vw;
}

.hero-text-wrapper {
  color: var(--text-color) !important;
}

.hero-header-text-wrapper {
  color: var(--text-color-hover) !important;
}

.btn-wrapper {
  width: 10vw;
  align-self: center;
}

@media only screen and (max-width: 600px) {
  .hero-card {
    margin-left: 0;
    margin-right: 0;
    margin-bottom: 4vh;
    width: 100%;
  }
  .btn-wrapper {
    width: 70%;
    align-self: center;
  }
}
</style>
