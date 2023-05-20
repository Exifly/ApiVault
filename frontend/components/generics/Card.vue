<template>
  <div class="glass-card card h-100">
    <div class="card-header-wrapper">
      <div class="card-header-column">
        <div class="text-wrapper text-wrapper-header-card mb-2">
          {{ title }}
        </div>
      </div>
      <div class="logo-container">
        <img :url="imageUrl" />
      </div>
    </div>
    <div class="card-body">
      <p class="text-wrapper card-text-wrapper card-text">
        {{ body }}
      </p>
      <slot />
    </div>
  </div>
</template>

<script lang="ts" setup>
defineProps({
  title: {
    type: String,
    required: true,
  },
  body: {
    type: String,
    required: true,
  },
  imageUrl: {
    type: String,
    required: true,
  },
});
</script>

<style scoped>
.glass-card {
  backdrop-filter: blur(16px) saturate(200%);
  -webkit-backdrop-filter: blur(16px) saturate(200%);
  background-color: var(--bg-card-glass);
  border-radius: 12px;
  border: 1px solid var(--border-color-cards);
  transition-property: scale, background-color;
  transition: 0.3s ease !important;
}

.logo-container {
  align-self: center;
}

#icon1,
#icon2 {
  color: var(--text-color) !important;
}

.text-wrapper-header-card {
  font-weight: 600;
  font-size: 20px;
  margin-left: 0.3vw;
}

.text-body-secondary {
  font-weight: 600;
}

.card-text-wrapper {
  font-size: 20px;
}

.card-header-wrapper {
  align-self: center;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin: 1rem;
  margin-bottom: 0;
}

.card-header-column {
  display: flex;
  flex-direction: column;
}

.attributes-container {
  display: flex;
  flex-direction: row;
}

@media only screen and (min-width: 1500px) {
  .glass-card {
    backdrop-filter: blur(16px) saturate(200%);
    -webkit-backdrop-filter: blur(16px) saturate(200%);
    background-color: var(--bg-card-glass);
    border-radius: 12px;
  }
}

@media only screen and (min-width: 1024px) {
  .glass-card {
    backdrop-filter: blur(16px) saturate(200%);
    -webkit-backdrop-filter: blur(16px) saturate(200%);
    background-color: var(--bg-card-glass);
    border-radius: 12px;
  }
}

@media only screen and (max-width: 600px) {
  .text-wrapper-header-card {
    font-weight: 600;
    font-size: 20px;
    margin-left: 2vw;
  }
  .card-text-wrapper {
    font-size: 15px;
    margin-left: 2vw;
  }
}

.glass-card:hover {
  background-color: var(--bg-card-glass-hover);
  scale: 1.01;
  transition: scale 0.1s ease-in-out;
}
</style>
