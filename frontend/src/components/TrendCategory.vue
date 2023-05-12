<template>
  <div class="trend-category-container px-2">
    <p>
      <slot />
    </p>
  </div>
</template>

<style scoped>
.trend-category-container {
  align-self: center;
  border-radius: 4px;
  background: var(--bg-trending-category);
  color: var(--card-attribute-color);
  margin-left: 0;
  margin-right: 1vw;
  margin-bottom: 1rem;
  min-width: 3rem;
  max-width: 12rem;
  justify-content: center;
}

.trend-category-container p {
  font-size: 16px;
}

.trend-category-container:hover {
  background-color: var(--bg-card-glass-hover);
}

p {
  font-size: 12px;
  font-weight: 600;
  margin: 0;
  text-align: center;
}

@media only screen and (max-width: 600px) {
  .trend-category-container {
    border-radius: 4px;
    background: var(--bg-trending-category);
    color: var(--card-attribute-color);
    margin-left: 0;
    margin-right: 4vw;
    margin-top: 10px;
    margin-bottom: 6px;
    justify-content: center;
    width: 20vw;
  }
}
</style>
