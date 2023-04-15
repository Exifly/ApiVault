<script setup>
import DashboardNew from "./pages/DashboardNew.vue";
import { onMounted } from "vue";

onMounted(() => {
  document.body.setAttribute("data-theme", "dark");
});
</script>

<template>
  <router-view />
</template>

<style scoped></style>
