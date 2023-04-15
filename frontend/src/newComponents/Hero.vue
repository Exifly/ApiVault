<template>
  <h1 class="page-title pb-5">Your Gateway to a World of Public APIs.</h1>
</template>

<style scoped>
.page-title{
  color: white;
  text-transform:capitalize;
}
.page-subtitle{
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
