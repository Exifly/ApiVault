<script setup>
import CategoryName from "@/components/CategoryName.vue";

defineProps({
  title: {
    type: String,
    required: true,
  },
  subtitle: {
    type: String,
    required: true,
  },
  body: {
    type: String,
    required: true,
  },
  properties: {
    type: [],
    required: false,
  },
});
</script>

<template>
  <div class="glass-card card">
    <img
      src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/NGC_4414_%28NASA-med%29.jpg/1200px-NGC_4414_%28NASA-med%29.jpg"
      class="card-img-top"
      alt="..."
      style="border-radius: 12px"
    />
    <div class="card-body">
      <h5 class="text-wrapper card-title">Card title</h5>
      <h6 class="text-wrapper card-subtitle mb-2 text-body-secondary">
        Card subtitle
      </h6>
      <p class="text-wrapper card-text">
        Some quick example text to build on the card title and make up the bulk
        of the card's content.
      </p>
      <CategoryName category="Pippo" />
    </div>
  </div>
</template>

<style scoped>
.glass-card {
  backdrop-filter: blur(16px) saturate(200%);
  -webkit-backdrop-filter: blur(16px) saturate(200%);
  background-color: var(--bg-card-glass);
  /* background-color: rgba(var(--bg-color), 0.78); */
  border-radius: 12px;
  border: 1px solid var(--border-color-cards);
}
</style>
