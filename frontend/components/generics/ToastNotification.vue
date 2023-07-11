<template>
  <div class="toast-container fade-in position-fixed bottom-0 end-0 p-3">
    <div
      id="liveToast"
      class="toast show"
      role="alert"
      aria-live="assertive"
      aria-atomic="true"
    >
      <div class="wrapper-toast-header toast-header">
        <img
          src="/img/apivault-dark-nobg.png"
          width="20"
          height="20"
          class="rounded me-2"
          alt="..."
        />
        <strong class="me-auto text-wrapper">Notification</strong>
        <small>just now</small>
        <button
          type="button"
          class="btn-close"
          data-bs-dismiss="toast"
          aria-label="Close"
        ></button>
      </div>
      <div class="toast-body">
        <slot />
      </div>
    </div>
  </div>
</template>

<style scoped>
.wrapper-toast-header {
  background: var(--bg-card-glass);
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
