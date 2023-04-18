<script setup>
import { ref } from "vue";
defineProps({
  width: {
    type: String,
    required: false,
    default: "30",
  },
  height: {
    type: String,
    required: false,
    default: "30",
  },
  source: {
    type: String,
    required: false,
    default: "/img/apivault-dark-nobg.png",
  },
});
</script>

<template>
  <img :src="source" alt="Logo" :width="width" :height="height" />
</template>
