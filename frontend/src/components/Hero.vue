<template>
  <div class="row">
    <div id="hero-logo" class="col-2">
      <Logo :source="imageSource" height="150" width="150" />
    </div>
    <div class="col-12 col-md-10">
      <h1 class="text-wrapper page-title mb-4 pt-md-5 px-md-5">
        Your Gateway to a World of Public APIs.
        <h5>This tool is completely free and Open-Source!</h5>
      </h1>
    </div>
  </div>
</template>

<script setup>
import Logo from "./Logo.vue";
import { reactive, computed, inject } from "vue";

const theme = inject("theme");

// Compute the image source based on the current theme
const imageSource = computed(() => {
  if (theme.value === "dark") {
    return "/img/apivault-dark-nobg.png";
  } else {
    return "/img/apivault-light-nobg.png";
  }
});
</script>

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
  border-radius: 12px;
  border: 1px solid var(--border-color-cards);
}

.hero-card {
  margin-left: 15vw;
  margin-right: 15vw;
  margin-bottom: 4vh;
  width: 30vw;
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

  #hero-logo {
    display: none;
  }
}
</style>
