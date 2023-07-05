<template>
  <NuxtLayout>
    <div>
      <NuxtPage />
    </div>
  </NuxtLayout>
</template>

<script lang="ts">
// workaround for bootstrap javascript
export default {
  head() {
    return {
      script: [
        {
          src: "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js",
        },
      ],
    };
  },
};
</script>

<script lang="ts" setup>
onMounted(() => {
  if (process.client) {
    if (localStorage.getItem("APIVaultTheme") === "" || localStorage.getItem("APIVaultTheme") === null) {
      localStorage.setItem("APIVaultTheme", "dark");
    }
  }
})
</script>
