<template>
  <div class="switch">
    <input v-if="!checked" type="checkbox" id="toggleAll" />
    <input v-else checked type="checkbox" id="toggleAll" />
    <label for="toggleAll"></label>
  </div>
</template>

<script lang="ts" setup>
defineProps({
  checked: {
    type: Boolean,
    default: false,
  }
})
</script>

<style scoped>
.switch {
  display: inline-flex;
  margin: 0 10px;
}
.switch input[type=checkbox] {
  height: 0;
  width: 0;
  visibility: hidden;
}
.switch input[type=checkbox]:checked + label {
  background: green;
}
.switch input[type=checkbox]:checked + label::after {
  left: calc(100% - 4px);
  transform: translateX(-100%);
}
.switch label {
  cursor: pointer;
  width: 48px;
  height: 24px;
  background: grey;
  display: block;
  border-radius: 24px;
  position: relative;
}
.switch label::after {
  content: "";
  position: absolute;
  top: 4px;
  left: 4px;
  width: 16px;
  height: 16px;
  background: white;
  border-radius: 16px;
  transition: 0.3s;
}
</style>
