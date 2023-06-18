<template>
  <font-awesome-icon
    :icon="isClicked ? 'fa-solid fa-bookmark' : 'fa-regular fa-bookmark'"
    :class="['mt-auto btn-like', { clicked: isClicked }]"
    @click.prevent="toggleClicked"
  />
</template>

<script lang="ts" setup>
const isClicked = ref(false);
const toggleClicked = () => {
  isClicked.value = !isClicked.value;
};
</script>

<style scoped>
.btn-like {
  aspect-ratio: 1;
  background-size: 2900%;
  background-repeat: no-repeat;
  cursor: pointer;
  color: white;
  padding: 0.3rem;
  text-decoration: none !important;
  min-width: 0 !important;
  width: -20px;
}

.clicked {
  animation: hearthBeat 0.2s steps(28) forwards;
  color: #ff9143;
}

@keyframes hearthBeat {
  0% {
    scale: 1.1;
  }
  50% {
    scale: 1.3;
  }
  100% {
    scale: 1;
  }
}
</style>
