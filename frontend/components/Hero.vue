<template>
  <div class="row">
    <div>
      <h1 class="text-wrapper page-title">
        Your Gateway to a World of Public APIs.
        <h5>This tool is completely free and Open-Source!</h5>
      </h1>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";

// TODO: set theme variable in nuxt.config.ts as public value (global state)
const theme = useState("APIVaultTheme", () =>
  process.client ? localStorage.getItem("APIVaultTheme")! : "dark"
);

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
.hero-flex {
  align-self: center;
}
.page-title {
  align-items: center;
  align-self: center;
  font-size: calc(1.375rem + 1vw);
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
