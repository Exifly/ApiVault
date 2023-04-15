<script setup>
// import Button from './Button.vue';
</script>

<template>
  <div class="search-bar text-black">
    <label
      ><font-awesome-icon
        :icon="['fas', 'magnifying-glass']"
        style="color: #ffffff; margin-left: 1vw; margin-right: 1vw"
      />
      <input class="input-bar" type="search" placeholder="Search" />
    </label>
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
  border-radius: 16px;
  display: flex;
  justify-content: center;
  transition: all 0.3s ease-in-out;
  width: 100%;
  /* justify-content: center; */
}

.input-bar {
  border-style: transparent;
  border-color: transparent;
  color: white;
  flex-grow: 1;
  margin-bottom: 0vh;
  height: 6vh;
}

label {
  align-self: center;
  align-items: center;
  border-radius: 16px;
  background-color: #212329;
  color: #6c757d;
  cursor: text;
  display: grid;
  grid-template: 1fr / auto 1fr;
  gap: 12px;
  width: 95%;
}

label:focus-within {
  border: 0.5px solid #ffffff;
}

label > input {
  outline: none;
  border: none;
  background: transparent;
}
</style>
