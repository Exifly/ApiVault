<template>
  <label for="message-text" class="text-wrapper">ORDER</label>
  <select
    v-model="order"
    placeholder="Choose order"
    class="px-3 text-wrapper inverted-input-box api-filter-select"
    aria-label="Select corse state"
  >
    <option selected value="0">A - Z</option>
    <option value="1">Z - A</option>
    <option value="2">LIKE</option>
  </select>
</template>

<script lang="ts" setup>
const order = ref(0);
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
