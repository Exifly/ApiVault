<template>
  <section class="user-info-container">
    <GenericsButton>
      <p class="text-wrapper">
        John Doe
        <font-awesome-icon class="ms-2" :icon="['fas', 'right-from-bracket']" />
      </p>
    </GenericsButton>
  </section>
</template>

<style scoped>
.user-info-container {
  display: flex;
  flex-direction: row;
  gap: 2px;
}

.user-info-container .text-wrapper {
  margin: 0 !important;
}
</style>
