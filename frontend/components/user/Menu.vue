<template>
  <div class="dropdown">
    <GenericsButton data-bs-toggle="dropdown" aria-expanded="false">
      {{ username }}
      <font-awesome-icon class="ms-2" :icon="['fas', 'angles-down']" />
    </GenericsButton>
    <ul class="dropdown-wrapper-override dropdown-animation dropdown-menu dropdown-menu-dark">
      <li><a class="text-wrapper dropdown-item" href="#">
        <font-awesome-icon class="me-2" :icon="['fas', 'bookmark']" />
        My bookmarks
      </a></li>
      <hr class="m-1" />
      <li><a class="text-wrapper dropdown-item" href="#">
        <font-awesome-icon class="me-2" :icon="['fas', 'user']" />
        Logout
      </a></li>
    </ul>
  </div>
</template>

<script lang="ts" setup>
let { username } = defineProps({
  username: {
    type: String,
    required: true,
  }
})
</script>

<style scoped>
.dropdown-wrapper-override {
  background: var(--bg-card-glass);
  font-size: 15px !important;
}

.dropdown-animation {
  animation: fadeIn 0.2s !important;
  transition: all 0.2s linear ease-in-out !important;
}
</style>
