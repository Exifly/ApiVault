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
  border-radius: 12px;
  border: 1px solid var(--border-color-cards);
  color: var(--text-color);
  font-weight: 600;
  font-size: 20px;
  margin-left: auto;
  margin-right: auto;
  width: 30%;
}

.load-more-button p {
  margin: 0;
  padding: 0;
}

.load-more-button:hover {
  background-color: var(--bg-card-glass-hover);
}

@media only screen and (max-width: 680px) {
  .load-more-button {
    background: var(--bg-card-glass);
    border-radius: 12px;
    color: var(--text-color);
    font-weight: 600;
    font-size: 20px;
    margin-left: auto;
    margin-right: auto;
    width: 40%;
  }
}
</style>
