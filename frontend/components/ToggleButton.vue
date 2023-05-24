<template>
  <button class="toggle-button" :class="{ active: isActive }" @click="toggle">
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
  background-color: black;
}

.toggle-button.active .toggle-icon {
  transform: translateX(30px);
}

.toggle-icon {
  display: flex;
  position: absolute;
  left: 0;
  justify-content: center;
  align-items: center;
  width: 30px;
  height: 30px;
  background-color: #fff;
  border-radius: 50%;
  transition: transform 0.3s ease;
}
</style>
