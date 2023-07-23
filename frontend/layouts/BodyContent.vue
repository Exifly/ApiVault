<template>
  <GenericsButton
    id="bottom-feedback-button"
    class="text-wrapper-inverted"
    :isInverted="true"
    data-bs-toggle="modal"
    data-bs-target="#feedbackModal"
  >
    Feedback
  </GenericsButton>
  <div class="flex-adjust container p-4 overflow-hidden">
    <div class="hero container">
      <div class="row">
        <div id="hero-column" class="col-12 col-lg-12 col-md-12">
          <div class="hero-flex">
            <slot name="heroAreaContent"></slot>
          </div>
          <slot name="trendingCategories"></slot>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-12 mb-3">
        <slot name="topAreaContent"></slot>
      </div>
    </div>
    <h1 class="text-wrapper">{{ title }}</h1>
    <hr />
    <h5 class="text-wrapper" v-if="isNullCategory">
      No Api's found for this category.. Sorry!!
    </h5>
    <slot name="cardAreaContent"></slot>
    <div class="container mt-5">
      <hr />
      <slot name="footerArea"></slot>
    </div>
  </div>
</template>

<script setup lang="ts">
const { title, isNullCategory } = defineProps({
  title: {
    type: String,
    required: false,
    default: "RANDOM",
  },
  isNullCategory: {
    type: Boolean,
    required: false,
    default: false,
  },
});
</script>

<style scoped>
#bottom-feedback-button {
  bottom: 10px;
  font-size: 13px;
  position: fixed;
  right: 10px;
  z-index: 1;
}
.hero {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

#hero-column .hero-flex {
  align-self: center !important;
}

.container {
  padding-right: 15px;
  padding-left: 2px;
  margin-right: auto;
  margin-left: auto;
}

.flex-child {
  flex-direction: column;
  flex-grow: 1;
  top: 25%;
  left: 25%;
}

.flex-adjust {
  margin-left: 22vw;
  margin-top: 1vw;
  width: auto;
}

.sidebar {
  width: 25vw;
}

.body-wrap {
  left: 25%;
}

@media only screen and (max-width: 600px) {
  .flex-adjust {
    margin-left: 0vw;
    margin-top: 8vh;
  }
}

@media (min-width: 1581px) {
  .flex-adjust {
    margin-left: 26vw;
    margin-right: 8vw;
    margin-top: 2vw;
  }
}
</style>
