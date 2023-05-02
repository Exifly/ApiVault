<script setup>
import { onMounted, inject } from "vue";

const theme = inject("theme");

onMounted(() => {
  document.body.setAttribute("data-theme", theme.value);
});
</script>

<template>
  <router-view />
</template>
