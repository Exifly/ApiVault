<template>
  <section class="mt-auto like-number-container">
    <p class="text-wrapper like-text-animation">
      <slot />
    </p>
  </section>
</template>

<style scoped>
.like-number-container {
  margin-top: auto;
  padding: 0.3rem;
  transition: all 0.2s linear all;
}

.like-number-container:active {
  animation: moveUp 0.2s linear;
}

.like-number-container p {
  font-size: medium;
  line-height: 1.2;
  margin: 0;
}
</style>
