<template>
  <button type="button" class="btn custom-button">
    <slot />
  </button>
</template>

<style scoped>
.custom-button {
  background: var(--bg-card-glass);
  border-radius: 12px;
  border: 1px solid var(--border-color-cards);
  color: var(--text-color);
  font-weight: 600;
  font-size: 20px;
  margin-left: auto;
  margin-right: auto;
}

.custom-button p {
  margin: 0;
  padding: 0;
}

.custom-button:hover {
  background-color: var(--bg-card-glass-hover);
}

@media only screen and (max-width: 680px) {
  .custom-button {
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

@keyframes borderGradient {
  0% {
    transform: rotateZ(1deg);
  }
  100% {
    transform: rotateZ(360deg);
  }
}
</style>
