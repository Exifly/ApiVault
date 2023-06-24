<template>
  <div class="glass-card fade-in alert alert-danger d-flex align-items-center" role="alert">
    <font-awesome-icon :icon="['fas', 'triangle-exclamation']" class="me-2"/>
      <div class="text-danger">
        <slot />
      </div>
  </div>
</template>

<style scoped>
.notification-transition {
  transition: all 0.2s ease-in-out;
}

.fade-in {
  opacity: 0;
  animation: fadeIn 0.3s forwards;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

</style>
