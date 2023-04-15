<script setup>
defineProps({
  categories: {
    type: [],
    required: false
  }
})
const stars = 104;
</script>

<template>
<nav class="navbar navbar-expand-lg navbar-props fixed-top nav-glass">
  <div class="container-fluid">
    <a class="navbar-brand text-white" href="#">API Vault 🤓</a>
    <button class="navbar-toggler " type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active text-white" aria-current="page" href="#">
            <font-awesome-icon :icon="['fab', 'github']" /> Stars {{ stars }}
          </a>
        </li>
      </ul>
      <h5 class="my-auto">
        Made with ❤️
      </h5>
      <hr>
      <div class="d-block d-md-none">
        <h5 class="my-3">Categories</h5>
        <div class="div" v-for="category in categories" :key="category">
          <p>{{ category }}</p>
        </div>
      </div>
    </div>
  </div>
</nav>
</template>

<style scoped>
@media only screen and (max-width: 600px) {
  .responsive {
    display: none;
  }
}
.navbar-props {
    background-color: var(--nav-color);
    color: white;
}

.nav-glass {
    background: #221f1fa8;
    /* box-shadow: 0 8px 32px 0 rgb(0 0 0 / 37%); */
    backdrop-filter: blur( 20px );
    -webkit-backdrop-filter: blur( 20px );
    border-radius: 10px;
}
</style>