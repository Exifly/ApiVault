<template>
  <div class="modal fade" id="submitApiModal" tabindex="-1" aria-labelledby="submitApiModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="custom-border-radius glass-card modal-content">
        <div class="custom-border modal-header">
          <h1 class="text-wrapper modal-title fs-5" id="submitApiModalLabel">{{ title }}</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label for="recipient-name" class="text-wrapper col-form-label">Name:</label>
              <input type="text" class="inverted-input-box text-wrapper form-control" id="recipient-name">
            </div>
            <div class="mb-3">
              <label for="recipient-name" class="text-wrapper col-form-label">Category:</label>
              <input type="text" class="inverted-input-box form-control" id="recipient-name">
            </div>
            <div class="mb-3">
              <label for="message-text" class="text-wrapper col-form-label">Description:</label>
              <input type="text" class="inverted-input-box form-control" id="message-text">
            </div>
            <div class="mb-3">
              <label for="message-text" class="text-wrapper col-form-label">Url:</label>
              <input type="text" class="inverted-input-box form-control" id="message-text">
            </div>
            <div class="mb-3">
              <label for="message-text" class="text-wrapper col-form-label">Auth:</label>
              <input type="text" class="inverted-input-box form-control" id="message-text">
            </div>
            <div class="mb-0">
                <label for="message-text" class="me-2 text-wrapper col-form-label primary">CORS:</label>
              <input class="form-check-input" type="checkbox" id="checkboxNoLabel" value="" aria-label="...">
            </div>
            <div class="mb-0">
              <label for="message-text" class="me-2 text-wrapper col-form-label">HTTPS:</label>
              <input class="form-check-input" type="checkbox" id="checkboxNoLabel" value="" aria-label="...">
            </div>
          </form>
        </div>
        <div class="custom-border modal-footer" style="margin-right: auto">
          <GenericsButton :isInverted="true" class="m-1" data-bs-dismiss="modal">Close</GenericsButton>
          <GenericsButton class="m-1" data-bs-dismiss="modal">Send</GenericsButton>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
defineProps({
  title: {
    type: String,
    required: true,
  },
})
</script>

<style scoped>
.inverted-input-box {
  background: var(--bg-trending-category);
  border: hidden;
}

.custom-border {
  border: hidden;
}

.custom-border-radius {
  border-radius: 8px;
}
</style>
