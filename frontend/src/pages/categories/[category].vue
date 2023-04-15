<script setup>
import { useRoute } from "vue-router";
const route = useRoute();
console.log(route.params.category);
</script>
<template>
  <h1>Pippo {{ route.params.category }}</h1>
</template>
