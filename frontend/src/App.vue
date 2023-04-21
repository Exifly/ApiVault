<script setup>
import { onMounted } from "vue";

onMounted(() => {
  document.body.setAttribute("data-theme", "dark");
});
</script>

<template>
  <router-view />
</template>
