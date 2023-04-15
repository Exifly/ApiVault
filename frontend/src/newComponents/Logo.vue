<script setup>
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
  image: {
    type: String,
    required: false,
    default: "../assets/img/logo.jpeg",
  },
});
</script>

<template>
  <img src="../assets/img/logo.jpeg" alt="" :width="width" :height="height" />
</template>
