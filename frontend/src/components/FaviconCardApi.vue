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
