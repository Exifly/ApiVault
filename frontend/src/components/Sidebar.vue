<script setup>
defineProps({
  categories: {
    type: Array,
    required: false,
  },
});
</script>

<template>
  <div
    id="responsive"
    class="flex-shrink-0 bg-normal h-100"
    style="width: 35vh"
  >
    <a
      href="/"
      class="d-flex align-items-center pb-3 mb-3 link-dark text-decoration-none border-bottom"
    >
      <svg class="bi me-2" width="30" height="24">
        <use xlink:href="#bootstrap" />
      </svg>
      <span class="fs-5 fw-semibold text-white mt-3">
        <font-awesome-icon :icon="['fas', 'list-ul']" />
        Categories: {{}}
      </span>
    </a>
    <div class="scrollbox">
      <ul class="list-unstyled ps-0 text-white mx-4">
        <li
          class="mb-1 mt-3 category-custom"
          v-for="category in categories"
          :key="category"
        >
          {{ category }}
          <hr />
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
@media only screen and (max-width: 600px) {
  #responsive {
    display: none;
  }
}
.bg-normal {
  background-color: var(--nav-color) !important;
  position: fixed;
}

.category-custom {
  color: rgb(165, 165, 165);
  transition: all 0.3s;
}

.category-custom:hover {
  color: rgb(218, 218, 218);
}

::-webkit-scrollbar {
  width: 5px;
}

::-webkit-scrollbar-thumb {
  background: #fff;
}

.scrollbox {
  overflow: scroll;
  height: 76vh;
}

#sidebar-custom,
p {
  margin-left: 3vw;
}
</style>
