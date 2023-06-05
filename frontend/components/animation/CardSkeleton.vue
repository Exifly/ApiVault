<template>
  <div class="card">
    <div class="header">
      <div class="details">
        <span class="name"></span>
        <span class="about"></span>
      </div>
      <div class="img"></div>
    </div>
    <div class="description">
      <div class="line line-1"></div>
      <div class="line line-2"></div>
      <div class="line line-3"></div>
    </div>
  </div>
</template>

<style scoped>
.card {
  max-width: 350px;
  width: 100%;
  height: 180px;
  background: var(--bg-card-glass);
  padding: 12px;
  border-radius: 10px;
}

.card .header {
  display: flex;
  justify-content: space-between;
}
.header .img {
  height: 48px;
  width: 48px;
  background: var(--skeleton-primary-color);
  border-radius: 4px;
  position: relative;
  overflow: hidden;
}

.details span {
  display: block;
  background: var(--skeleton-primary-color);
  border-radius: 10px;
  overflow: hidden;
  position: relative;
}
.details .name {
  height: 15px;
  width: 100px;
}
.details .about {
  height: 13px;
  width: 150px;
  margin-top: 10px;
}
.card .description {
  margin: 25px 0;
}
.description .line {
  background: var(--skeleton-primary-color);
  border-radius: 10px;
  height: 13px;
  margin: 10px 0;
  overflow: hidden;
  position: relative;
}
.description .line-1 {
  width: calc(100% - 15%);
}
.description .line-3 {
  width: calc(100% - 40%);
}

.header .img::before,
.details span::before,
.description .line::before {
  position: absolute;
  content: "";
  height: 100%;
  width: 100%;
  background-image: linear-gradient(
    to right,
    rgba(0, 0, 0, 0.05) 5%,
    var(--skeleton-secondary-color) 100%,
    rgba(0, 0, 0, 0.05) 5%
  );
  background-repeat: no-repeat;
  background-size: 450px 400px;
  animation: shimmer 2s ease-in-out infinite;
}
.header .img::before {
  background-size: 650px 600px;
}
.details span::before {
  animation-delay: 0.2s;
}

@keyframes shimmer {
  0% {
    background-position: -450px 0;
  }
  100% {
    background-position: 450px 0;
  }
}
</style>
