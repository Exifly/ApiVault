<template>
  <button type="button" class="btn load-more-button">
    <LoadingEffectSmall v-if="isLoading" />
    <p v-if="!isLoading">Load More</p>
  </button>
</template>

<script lang="ts" setup>
const { isLoading } = defineProps({
  isLoading: {
    type: Boolean,
    default: false,
  },
});
</script>

<style scoped>
.load-more-button {
  background: var(--bg-card-glass);
  border-radius: 8px;
  border: 1px solid var(--border-color-cards);
  color: var(--text-color);
  font-weight: 600;
  font-size: 14px;
  margin-left: auto;
  margin-right: auto;
  width: 10%;
}

.load-more-button p {
  margin: 0;
  padding: 0;
}

.load-more-button:hover {
  border: solid 1px var(--icon-color);
  transition: scale 0.1s ease-in-out;
}

@media only screen and (max-width: 680px) {
  .load-more-button {
    background: var(--bg-card-glass);
    border-radius: 8px;
    color: var(--text-color);
    font-weight: 600;
    font-size: 20px;
    margin-left: auto;
    margin-right: auto;
    width: 40%;
  }
}
</style>
