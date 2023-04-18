<template>
  <div class="category-container px-2">
    <p>
      <slot />
    </p>
  </div>
</template>

<style scoped>
.category-container {
  align-self: center;
  border-radius: 4px;
  border-color: rgb(153, 0, 0);
  background: rgba(0, 98, 195, 0.2);
  color: rgb(3, 155, 178);
  margin-left: 0;
  margin-right: 1vw;
  justify-content: center;
}

p {
  font-size: 12px;
  font-weight: 600;
  margin: 0;
  text-align: center;
}

@media only screen and (max-width: 600px) {
  .category-container {
    border-radius: 4px;
    border-color: rgb(153, 0, 0);
    background: rgba(0, 98, 195, 0.2);
    color: rgb(3, 155, 178);
    margin-left: 0;
    margin-right: 4vw;
    margin-top: 10px;
    margin-bottom: 6px;
    justify-content: center;
    width: 20vw;
  }
}
</style>
