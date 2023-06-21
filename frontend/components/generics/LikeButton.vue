<template>
  <font-awesome-icon
    :icon="isClicked ? 'fa-solid fa-heart' : 'fa-regular fa-heart'"
    :class="['mt-auto btn-like', { clicked: isClicked }]"
    @click.prevent="clickHandler"
  />
</template>

<script lang="ts" setup>
const { likedByUser } = defineProps({
  likedByUser: {
    type: Boolean,
    required: false,
    default: false,
  },
});

/* 
  It emit an event that will be handled by parent component (CardAPI) 
  to understand if the like button is already clicked
*/
const emit = defineEmits(["like:isClicked"]);
const isClicked = ref<boolean>(false);

const clickHandler = () => {
  isClicked.value = !isClicked.value;
  emit("like:isClicked", true);
};

onMounted(() => {
  isClicked.value = likedByUser ? true : false;
});
</script>

<style scoped>
.btn-like {
  aspect-ratio: 1;
  background-size: 2900%;
  background-repeat: no-repeat;
  cursor: pointer;
  color: var(--text-color);
  padding: 0.3rem;
  text-decoration: none !important;
  min-width: 0 !important;
  width: -20px;
}

.btn-like:hover {
  transition: scale 0.1s linear;
  transform: scale(1.1)
}

.clicked {
  animation: hearthBeat 0.2s steps(28) forwards;
  color: #ff3130;
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
