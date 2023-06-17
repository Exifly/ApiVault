<template>
  <font-awesome-icon
    :icon="isClicked ? 'fa-solid fa-heart' : 'fa-regular fa-heart'"
    :class="['mt-auto btn-like', { clicked: isClicked }]"
    @click.prevent="toggleClicked"
  />
</template>

<script lang="ts" setup>
/* 
  It emit an event that will be handled by parent component (CardAPI) 
  to understand if the like button is already clicked
*/
const emit = defineEmits(["like:isClicked"]);
const isClicked = ref<boolean>(false);
const toggleClicked = () => {
  isClicked.value = !isClicked.value;
  emit("like:isClicked", isClicked.value);
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
  color: #ff3130;
}
</style>
