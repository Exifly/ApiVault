<template>
  <div class="row">
    <div>
      <h1 class="text-wrapper page-title">
        Your Gateway to a World of Public APIs.
      </h1>
      <h5 class="text-wrapper">
        This tool is completely free and Open-Source!
      </h5>
    </div>
  </div>
</template>

<style scoped>
.hero-flex {
  align-self: center;
}
.page-title {
  align-items: center;
  align-self: center;
  font-size: calc(1.375rem + 1vw);
  justify-content: center;
  margin-bottom: 0;
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
