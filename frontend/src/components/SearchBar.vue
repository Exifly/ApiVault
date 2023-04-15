<script setup>
// import Button from './Button.vue';
</script>

<template>
  <div class="search-bar text-black">
    <span
      ><font-awesome-icon
        :icon="['fas', 'magnifying-glass']"
        style="color: #ffffff; margin-left: 1vw; margin-right: 1vw"
      />
      <input class="input-bar" type="text" placeholder="Search" />
    </span>
    <!-- <Button value="Categories" /> -->
  </div>
</template>

<style scoped>
@media only screen and (max-width: 600px) {
  .input-bar {
    width: 82.5vw;
  }
}
.search-bar {
  align-items: center;
  background-color: #212329;
  border-radius: 16px;
  display: flex;
  transition: all 0.3s ease-in-out;
  /* justify-content: center; */
}

.input-bar {
  background-color: #212329;
  border-radius: 16px;
  border-style: transparent;
  border-color: transparent;
  color: white;
  margin-bottom: 0vh;
  height: 6vh;
  width: 45.5vw;
}
</style>
