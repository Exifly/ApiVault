<template>
  <button class="mobile-toogle-wrapper toggle-button" :class="{ active: isActive }" @click="toggle">
    <span class="toggle-icon">
      <font-awesome-icon :icon="['fas', icon]" />
    </span>
  </button>
</template>

<script lang="ts" setup>
const isActive = ref(false);

const toggle = () => {
  isActive.value = !isActive.value;
};

const icon = computed(() => {
  return isActive.value ? "sun" : "moon";
});

onMounted(() => {
  const isLight = useTheme();
  isActive.value = true ? isLight.value === "dark" : false;
});
</script>

<style>
.toggle-button {
  width: 60px;
  height: 30px;
  background-color: #ccc;
  border-radius: 15px;
  position: relative;
  outline: none;
  border: none;
  cursor: pointer;
}

.toggle-button.active {
  background-color: #ccc;
}

.toggle-button.active .toggle-icon {
  transform: translateX(30px);
}

.toggle-icon {
  align-items: center;
  background-color: #fff;
  border-radius: 50%;
  color: var(--icon-gradient-theme-color-primary);
  display: flex;
  justify-content: center;
  height: 30px;
  left: 0;
  position: absolute;
  transition: transform 0.3s ease;
  width: 30px;
}

@media (max-width: 480px) {
  .mobile-toogle-wrapper {
    margin-left: 0 !important;
  }
}

</style>
