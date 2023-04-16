<script setup>
import { reactive, computed } from "vue";
const props = defineProps({
  scheme: {
    type: String,
    required: false,
  },
});

const logoMode = computed(() => {
  if (props.scheme === "dark") {
    return "/img/apivault-dark-nobg.png";
  }
  return "/img/apivault-light-nobg.png";
});
</script>

<template>
  <footer
    class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4"
  >
    <p class="col-md-4 mb-0 text-wrapper-no-hover">
      &copy; 2023 Exifly
      <br />
      Coded by
      <a
        href="/"
        class="text-wrapper-authors"
        style="text-decoration: none; font-weight: 600"
      >
        gdjohn4s
      </a>
      &
      <a
        href="/"
        class="text-wrapper-authors"
        style="text-decoration: none; font-weight: 600"
      >
        flavioad
      </a>
    </p>

    <router-link
      to="/"
      class="col-md-4 d-flex align-items-center justify-content-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none"
    >
      <img :src="logoMode" alt="" width="30" height="30" />
    </router-link>

    <ul class="nav col-md-4 justify-content-end">
      <li class="nav-item">
        <a href="#" class="nav-link px-2 text-wrapper"
          ><font-awesome-icon :icon="['fab', 'github']"
        /></a>
      </li>
      <li class="nav-item">
        <a href="#" class="nav-link px-2 text-wrapper">Contact</a>
      </li>
      <li class="nav-item">
        <a href="#" class="nav-link px-2 text-wrapper">Sponsor</a>
      </li>
      <li class="nav-item">
        <a href="#" class="nav-link px-2 text-wrapper">FAQs</a>
      </li>
      <li class="nav-item">
        <a href="#" class="nav-link px-2 text-wrapper">About</a>
      </li>
    </ul>
  </footer>
</template>

<style scoped>
.text-wrapper {
  color: var(--text-color);
}

.text-wrapper:hover {
  color: var(--text-color-hover);
}

.text-wrapper-no-hover {
  color: var(--text-color);
}

.text-wrapper-authors {
  color: rgb(3, 155, 178);
}

.text-wrapper-authors:hover {
  color: rgb(0, 201, 232);
}
</style>
