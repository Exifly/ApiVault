<template>
  <div class="category-container">
    <p>
      <slot />
    </p>
  </div>
</template>

<style scoped>
.category-container {
  border-radius: 4px;
  border-color: rgb(153, 0, 0);
  background: rgba(0, 98, 195, 0.2);
  color: rgb(3, 155, 178);
  margin-left: 0;
  margin-right: auto;
  margin-top: 10px;
  margin-bottom: 6px;
  justify-content: center;
  width: 10vw;
}

p {
  font-size: 14px;
  margin: 0;
  text-align: center;
}
</style>
