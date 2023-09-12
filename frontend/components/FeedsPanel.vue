<script setup lang="ts">
const props = defineProps({
  isLoading: {
    type: Boolean,
    required: true,
  }
})
const likes = ref<Number>(0);
</script>

<template>
  <h1 class="text-wrapper">LAST ADDED</h1>
  <hr />
  <div class="row">
    <TransitionGroup name="cards">
      <div class="wrapper" v-if="isLoading">
        <div
          class="col-12 col-lg-4 col-md-6 mb-4 mb-md-4"
          style="height: 180px"
          v-for="card in 4"
          :key="card"
        >
          <AnimationCardSkeleton />
        </div>
      </div>
      <div
        v-else
        class="col-12 col-lg-4 col-md-6 mb-4 mb-md-4"
        style="height: 180px"
        v-for="card in 4"
        :key="card"
      >
        <CardAPI 
          title="Pippo"
          subtitle="Api bellissimissimissima"
          body="Ciao come stai" 
          favicon-src="https://bitcoin.com/"
          :https=true
          auth="OAuth"
          :likes-count="likes" />
      </div>
    </TransitionGroup>
  </div>
</template>
