<template>
  <button
    type="button"
    :class="[
      'btn',
      { 'custom-button': !isInverted },
      { 'inverted-theme-color': isInverted },
    ]"
  >
    <slot />
  </button>
</template>

<script lang="ts" setup>
defineProps({
  isInverted: {
    type: Boolean,
    required: false,
    default: false,
  },
});
</script>

<style scoped>
.custom-button {
  background: var(--bg-card-glass);
  border-radius: 8px;
  border: 1px solid var(--border-color-cards);
  color: var(--text-color);
  font-weight: 400;
  font-size: 15px;
  margin-left: auto;
  margin-right: auto;
}

.custom-button p {
  margin: 0;
  padding: 0;
}

.custom-button:hover {
  border: solid 1px var(--icon-color);
  transition: scale 0.1s ease-in-out;
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
    width: 75%;
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
