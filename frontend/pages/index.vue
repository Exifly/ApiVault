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
      <div class="trend-container mb-3">
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
              :icon="categoryMap[category.name]"
            />{{ category.name }}
            <span class="api_count mx-1">({{ category.api_count }})</span>
          </NuxtLink>
        </TrendCategory>
        <hr />
      </div>
    </template>
    <template #cardAreaContent>
      <div class="row">
        <LoadingEffect v-if="isLoading" />
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
            <Card
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

const layouts: string = "body-content";
const categoryMap = categoriesDict;

const apiData: Ref<APIType[]> = ref([]);
const apiSearched: Ref<APIType[]> = ref([]);
const categorySearched = reactive({
  category: "",
});
const isLoading = ref(true);
const showList = ref(true);
let isLoadingState = ref(false);
let hasMoreData = ref(true);

const trendCategoriesList = ref<TrendingCategory[]>([]);
trendCategoriesList.value = await ApivaultServices.getTrendingCategories()!;

const handleSearchDashboard = (val: string, title: string) => {
  handleSearch(val, title, apiData, apiSearched, categorySearched, showList);
};

const showLoadMore = computed(() => {
  return (
    hasMoreData.value &&
    categorySearched.category === "RANDOM" &&
    !isLoading.value
  );
});

const handleLoadMore = async () => {
  isLoadingState.value = true;
  setTimeout(async () => {
    const newData = await ApivaultServices.randomApis();
    const filteredData = newData.filter((newItem) => {
      return !apiData.value.some(
        (existingItem) => existingItem.url === newItem.url
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

onMounted(async () => {
  apiData.value = await ApivaultServices.randomApis();
  console.log(apiData.value);
  isLoading.value = false;
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
