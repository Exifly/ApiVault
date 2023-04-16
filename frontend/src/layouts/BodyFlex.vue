<template>
  <div class="flex-parent">
    <slot />
  </div>
</template>

<style scoped>
.flex-parent {
  display: flex;
  flex-direction: row;
  flex-grow: 0;
}
</style>
