<template>
  <div class="flex-adjust container p-4 overflow-hidden">
    <div class="hero container">
      <div class="row">
        <div class="col-12 col-lg-12 col-md-12">
          <slot name="heroAreaContent"></slot>
          <h1 id="title-trending" class="text-wrapper mb-3">TRENDING</h1>
          <div class="trend-container mb-5">
            <TrendCategory
              v-for="category in trendCategoriesList"
              :key="category"
            >
              <router-link
                :to="`/categories/${category.category_name}`"
                class="text-wrapper"
                style="text-decoration: none"
              >
                <font-awesome-icon
                  class="me-2 icon-color"
                  width="12"
                  height="12"
                  :icon="categoryMap[category.category_name]"
                />{{ category.category_name }}
                <span class="api_count">({{ category.api_count }})</span>
              </router-link>
            </TrendCategory>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-12 mb-5">
        <slot name="topAreaContent"></slot>
      </div>
    </div>

    <h1 class="text-wrapper mb-3">{{ props.title }}</h1>
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

<script setup>
import TrendCategory from "@/components/TrendCategory.vue";
import trendCategories from "@/components/api/trendCategories";
import { onMounted, ref, inject } from "vue";
const categoryMap = inject("categoryDict");
const props = defineProps({
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

let trendCategoriesList = ref(null);
onMounted(async () => {
  trendCategoriesList.value = await trendCategories();
});
</script>

<style scoped>
.api_count {
  color: #8b8b8b;
}
.trend-container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
.icon-color {
  color: #ff3130;
}
.hero {
  align-items: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
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
  margin-top: 4vw;
}

.sidebar {
  width: 25vw;
}

.body-wrap {
  left: 25%;
}

@media only screen and (max-width: 600px) {
  .mobile-first {
    display: none;
  }
  .flex-adjust {
    margin-left: 0vw;
    margin-top: 8vh;
  }

  .trend-container {
    display: none;
  }

  #title-trending {
    display: none;
  }
}

@media (min-width: 1581px) {
  .flex-adjust {
    margin-left: 26vw;
    margin-right: 8vw;
    margin-top: 7vw;
  }
}

@media only screen and (max-width: 600px) and (device-width: 390px) and (device-height: 844px) and (-webkit-device-pixel-ratio: 3) {
  .element {
    display: none;
  }
}
</style>
