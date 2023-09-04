<template>
  <select
    v-model="order"
    class="ps-1 px-3 text-wrapper inverted-input-box api-filter-select"
    aria-label="Select corse state"
    @change="orderApis"
  >
    <option selected value="name">Alphabetical</option>
    <option value="-likes_count">Likes</option>
  </select>
</template>

<script lang="ts" setup>
const order = ref<string>();
const emit = defineEmits(["filter:option"]);

function orderApis() {
  emit("filter:option", order.value);
}
</script>

<style scoped>
.inverted-input-box {
  background: var(--bg-card-glass);
  border: 1px solid var(--border-color-cards);
}

.inverted-input-box:hover {
  border: 1px solid var(--icon-color);
  transition: scale 0.2s ease-in-out;
}

.api-filter-select {
  height: 2.2rem;
  border-radius: 5px;
}
</style>
