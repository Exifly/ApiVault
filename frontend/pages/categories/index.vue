<template></template>
<script lang="ts" setup>
/*
 * This act like a navigation guard, if a user want to go on
 * apivault.dev/categories, the router will push the app
 * to the dashboard index page
 */
const router = useRouter();
onMounted(() => {
  router.push("/");
});
</script>
