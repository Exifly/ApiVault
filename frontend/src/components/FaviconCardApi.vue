<template>
  <img
    :src="url"
    class="favicon-api"
    alt="webLogo"
    style="border-radius: 12px"
  />
</template>

<script setup>
const props = defineProps({
  url: {
    type: String,
    required: true,
    default: "https://exifly.it/assets/img/no_bg_black%202.png",
  },
});
</script>

<style scoped>
.favicon-api {
  background: var(--bg-color);
  border-radius: 12px;
  border: 0.01px solid var(--border-color-cards);
  margin-left: 1vw;
  width: 48px;
  height: 48px;
  align-self: center;
}

@media only screen and (max-width: 600px) {
  .favicon-api {
    background: var(--bg-color);
    border-radius: 12px;
    border: 0.01px solid var(--border-color-cards);
    margin-left: 4vw;
    width: 48px;
    height: 48px;
    align-self: center;
  }
}
</style>
