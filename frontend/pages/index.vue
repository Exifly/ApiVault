<template>
  <NuxtLayout :name="layouts" :title="categorySearched.category">
    <template #heroAreaContent>
      <Hero />
    </template>
    <template #topAreaContent>
      <SearchBar @search:apiSearch="handleSearchDashboard" />
    </template>
    <template #trendingCategories>
      <h1 id="title-trending" class="text-wrapper mb-3">TRENDING</h1>
      <div class="trend-container mb-3" v-if="!isLoading">
        <TransitionGroup name="cards">
          <TrendCategory
            v-for="category in trendCategoriesList"
            :key="category.name"
          >
            <NuxtLink
              :to="`/categories/${category.name}`"
              class="text-wrapper"
              style="text-decoration: none"
            >
              <font-awesome-icon
                class="me-2 icon-color"
                width="12"
                height="12"
                :icon="categoriesDict[category.name]"
              />{{ category.name }}
              <span class="api_count mx-1">({{ category.api_count }})</span>
            </NuxtLink>
          </TrendCategory>
        </TransitionGroup>
      </div>
      <div class="trend-container mb-3" v-else>
        <TransitionGroup name="cards">
          <TrendCategory
            class="skeleton-box"
            style="height: 30px"
            v-for="category in 10"
            :key="category"
          />
        </TransitionGroup>
        <hr />
      </div>
    </template>
    <template #cardAreaContent>
      <div class="row">
        <TransitionGroup name="cards">
          <div class="wrapper" v-if="isLoading">
            <div
              class="col-12 col-lg-4 col-md-6 mb-4 mb-md-4"
              style="height: 180px"
              v-for="card in 9"
              :key="card"
            >
              <AnimationCardSkeleton />
            </div>
          </div>
          <div
            class="col-12 col-lg-4 col-md-6 mb-4 mb-md-4"
            v-for="api in apiSearched"
            :key="api.id"
          >
            <a
              v-if="showList"
              :href="api.url"
              target="_blank"
              style="text-decoration: none"
            >
              <CardAPI
                :title="api.name"
                :subtitle="api.category"
                :body="api.description"
                :cors="api.cors"
                :https="api.https"
                :auth="api.auth"
                :faviconSrc="api.url"
              />
            </a>
          </div>
        </TransitionGroup>
      </div>
      <div class="row mt-4">
        <LoadMoreButton
          v-if="showLoadMore"
          @click="handleLoadMore"
          :isLoading="isLoadingState"
        />
      </div>
    </template>
    <template #footerArea>
      <Footer />
    </template>
  </NuxtLayout>
</template>

<script lang="ts" setup>
import { handleSearch } from "~/pages/functions/searchEngine";
import ApivaultServices from "~/services/ApivaultServices";
import { categoriesDict } from "~/utils/categoryMapping";
import { TrendingCategory } from "~/models/types";
import { APIType } from "~/models/types";

// adding cookie script
useHead({
  script: [
    {
      src: "https://app.enzuzo.com/apps/enzuzo/static/js/__enzuzo-cookiebar.js?uuid=f59a7360-00b5-11ee-a49e-231d479eb14f",
    },
  ],
});

// layout name
const layouts: string = "body-content";

// trending and random data
const trendCategoriesList = ref<TrendingCategory[]>();
const apiData: any = ref([]);

// search bar data
const apiSearched: Ref<APIType[]> = ref([]);
const categorySearched = reactive({
  category: "RANDOM",
});

// loading state animation
const isLoading = ref(true);
const showList = ref(true);

// loading more state
let isLoadingState = ref(false);
let hasMoreData = ref(true);

// wrapper for handleSearch function
const handleSearchDashboard = (val: string, title: string) => {
  handleSearch(
    val,
    title,
    apiData,
    apiSearched,
    categorySearched,
    "RANDOM",
    showList
  );
};

// this computed property is used for manage the data state for load more
const showLoadMore = computed(() => {
  return (
    hasMoreData.value &&
    categorySearched.category === "RANDOM" &&
    !isLoading.value
  );
});

// this function is used to handle the load more event
const handleLoadMore = async () => {
  isLoadingState.value = true;
  setTimeout(async () => {
    const newData = await ApivaultServices.randomApis();
    const filteredData = newData.filter((newItem) => {
      return !apiData.value.some(
        (existingItem: any) => existingItem.url === newItem.url
      );
    });

    if (filteredData.length === 0) {
      hasMoreData.value = false;
      isLoadingState.value = false;
    } else {
      apiData.value = [...apiData.value, ...filteredData];
      isLoadingState.value = false;
    }
  }, 200);
};

onBeforeMount(async () => {
  trendCategoriesList.value = await ApivaultServices.getTrendingCategories()!;
  apiData.value = await ApivaultServices.randomApis();
  isLoading.value = true
    ? apiData.value === null || apiData.value === ""
    : false;
});

onMounted(async () => {
  showList.value = true;
});
</script>

<style scoped>
@media only screen and (max-width: 600px) {
  #title-trending {
    display: none;
  }
  .trend-container {
    display: none !important;
  }
}

@media only screen and (max-width: 600px) and (device-width: 390px) and (device-height: 844px) and (-webkit-device-pixel-ratio: 3) {
  .element {
    display: none;
  }
}

.icon-color {
  color: var(--icon-color);
}

.trend-container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
</style>
