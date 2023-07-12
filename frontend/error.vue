<template>
  <div class="container-custom-error">
    <div class="body">
      <div class="message">
        <h1>
          Error <span class="errorcode">{{ error.statusCode }}</span>
        </h1>
        <p class="output">
          {{ error.statusMessage }} <br />
          Try again later, you will be more lucky next time
        </p>
        <GenericsButton @click="handleError" class="">Go back</GenericsButton>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps({
  error: {
    type: Object,
    required: true,
  },
});

const handleError = () => clearError({ redirect: "/" });
</script>

<style scoped>
.body {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  height: 100%;
  background-color: #5b1414cc;
  background-image: radial-gradient(#5b1414cc, #041607);
  font-size: 1.5rem;
  color: #fa4549cc;
  text-shadow: 0 0 1ex #ff5c5fcc, 0 0 2px rgba(255, 255, 255, 0.8);
}
.justify {
  justify-content: center;
}

.container-custom-error {
  position: absolute;
  width: 100%;
  height: 100%;
  background: repeating-linear-gradient(
    180deg,
    rgba(0, 0, 0, 0) 0,
    rgba(0, 0, 0, 0.3) 50%,
    rgba(0, 0, 0, 0) 100%
  );
  background-size: auto 4px;
  z-index: 99;
}

.container-custom-error::before {
  content: "";
  position: absolute;
  display: block;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
  background-image: -webkit-gradient(
    linear,
    left bottom,
    left top,
    from(transparent),
    color-stop(2%, #041607),
    color-stop(3%, #ba2c2ccc),
    color-stop(3%, #041607),
    to(transparent)
  );
  background-image: linear-gradient(
    0deg,
    transparent 0%,
    #041607 2%,
    #5b1414cc 3%,
    #041607 3%,
    transparent 100%
  );
  background-repeat: no-repeat;
  -webkit-animation: scan 7.5s linear 0s infinite;
  animation: scan 7.5s linear 0s infinite;
}

@-webkit-keyframes scan {
  0% {
    background-position: 0 -100vh;
  }
  35%,
  100% {
    background-position: 0 100vh;
  }
}

@keyframes scan {
  0% {
    background-position: 0 -100vh;
  }
  35%,
  100% {
    background-position: 0 100vh;
  }
}
.message {
  -webkit-box-sizing: inherit;
  box-sizing: inherit;
  position: absolute;
  height: 100%;
  width: 1000px;
  max-width: 100%;
  padding: 4rem;
  text-transform: uppercase;
}

.output {
  color: #ba2c2ccc;
  text-shadow: 0 0 1px #fb3939cc, 0 0 2px rgba(157, 157, 157, 0.8);
}

.social::before {
  content: "> ";
}

a {
  color: #fff;
  text-decoration: none;
}

a::before {
  content: "[";
}

a::after {
  content: "]";
}

.errorcode {
  color: white;
}
</style>
