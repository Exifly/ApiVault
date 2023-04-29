<template>
  <a :href="profile" target="_blank">
    <img
      :src="avatarUrl"
      class="wonderful-person-img"
      alt="wonderful person"
      style="border-radius: 12px"
    />
  </a>
</template>

<script setup>
const props = defineProps({
  avatarUrl: {
    type: String,
    required: true,
  },
  profile: {
    type: String,
    required: true,
    default: "#",
  },
});
</script>

<style scoped>
.wonderful-person-img {
  background: var(--bg-color);
  border-radius: 12px;
  border: 0.01px solid var(--border-color-cards);
  width: 88px;
  height: 88px;
  align-self: center;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 15px -3px,
    rgba(0, 0, 0, 0.05) 0px 4px 6px -2px;
  transition: all 0.7s;
}

.wonderful-person-img:hover {
  transform: scale(-1, 1);
}

@media only screen and (max-width: 600px) {
  .wonderful-person-img {
    align-self: center;
    background: var(--bg-color);
    border-radius: 12px;
    border: 0.01px solid var(--border-color-cards);
    width: 64px;
    height: 64px;
    align-self: center;
  }
}
</style>
