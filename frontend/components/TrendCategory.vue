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
  background: var(--bg-card-glass);
  border-color: var(--bg-card-glass-border);
  border-style: solid;
  border-width: max(1px, 0.0625rem);
  color: var(--card-attribute-color);
  margin-left: 0;
  margin-right: 0.4vw;
  margin-bottom: 0.4rem;
  max-width: 13rem;
  justify-content: center;
}

.trend-category-container p {
  font-size: 16px;
  padding: 3px;
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
    background: var(--bg-card-glass);
    color: var(--card-attribute-color);
    margin-left: 0;
    margin-right: 4vw;
    margin-top: 10px;
    margin-bottom: 6px;
    justify-content: center;
    width: 20vw;
    border: 1px solid var(--border-color-cards);
  }
}
</style>
