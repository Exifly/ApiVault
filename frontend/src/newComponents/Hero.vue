<template>
  <div class="hero-card hero-text-wrapper glass-card card text-center">
    <div class="card-body">
      <h4 class="hero-header-text-wrapper">CONTRIBUTE</h4>
      Help us contributing on the repository. <br />If you want of course.
    </div>
    <a href="#" class="btn-wrapper btn btn-outline-primary m-3">REPOSITORY</a>
  </div>
</template>

<style scoped>
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
