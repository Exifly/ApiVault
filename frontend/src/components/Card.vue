<script setup>
import CardAttributes from "@/components/CardAttributes.vue";

defineProps({
  title: {
    type: String,
    required: true,
  },
  subtitle: {
    type: String,
    required: true,
  },
  body: {
    type: String,
    required: true,
  },
  properties: {
    type: [],
    required: false,
  },
});
</script>

<template>
  <div class="glass-card card">
    <div class="card-header-wrapper">
      <div class="logo-container">
        <img
          src="https://exifly.it/assets/img/no_bg_black%202.png"
          class="favicon-api"
          alt="webLogo"
          style="border-radius: 12px"
        />
      </div>
      <div class="text-wrapper text-wrapper-header-card">Featured</div>
    </div>
    <div class="card-body mt-3">
      <h6 class="text-wrapper card-subtitle mb-2 text-body-secondary">
        Card subtitle
      </h6>
      <p class="text-wrapper card-text">
        Some quick example text to build on the card title and make up the bulk
        of the card's content.
      </p>
      <CardAttributes> Pippo </CardAttributes>
    </div>
  </div>
</template>

<style scoped>
.glass-card {
  backdrop-filter: blur(16px) saturate(200%);
  -webkit-backdrop-filter: blur(16px) saturate(200%);
  background-color: var(--bg-card-glass);
  /* background-color: rgba(var(--bg-color), 0.78); */
  border-radius: 12px;
  border: 1px solid var(--border-color-cards);
}

.text-wrapper-header-card {
  align-self: center;
  font-weight: 600;
  font-size: 20px;
  margin-left: 0.3vw;
}

.card-header-wrapper {
  border-bottom: 0.3px solid gray;
  display: flex;
  flex-direction: row;
}

.favicon-api {
  background: var(--bg-color);
  border-radius: 12px;
  border: 0.01px solid var(--border-color-cards);
  margin-left: 1vw;
  width: 64px;
  height: 64px;
  align-self: center;
  margin-bottom: -13px;
  margin-top: 12px;
}

@media only screen and (max-width: 600px) {
  .text-wrapper-header-card {
    align-self: center;
    font-weight: 600;
    font-size: 20px;
    margin-left: 3.3vw;
  }
  .favicon-api {
    background: var(--bg-color);
    border-radius: 12px;
    border: 0.01px solid var(--border-color-cards);
    margin-left: 4vw;
    width: 64px;
    height: 64px;
    align-self: center;
    margin-bottom: -13px;
    margin-top: 12px;
  }
}
</style>
