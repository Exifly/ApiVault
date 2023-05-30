<template>
  <NuxtLayout :name="layouts" :title="categorySearched.category">
    <template #heroAreaContent>
      <Hero />
    </template>
    <template #topAreaContent>
      <SearchBar @search:apiSearch="handleSearchCategory" />
    </template>
    <template #cardAreaContent>
      <div class="row" v-if="isLoading">
        <LoadingEffect />
      </div>
      <div class="row" v-if="showList">
        <div
          class="col-12 col-lg-4 col-md-6 mb-4 mb-md-4"
          v-for="api in apiSearched"
          :key="api.id"
        >
          <a
            class="text-white text-decoration-none"
            :href="api.url"
            target="_blank"
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
      </div>
    </template>
    <template #footerArea>
      <Footer />
    </template>
  </NuxtLayout>
</template>

<script lang="ts" setup>
import { APIType } from "~/models/types";
import ApivaultServices from "~/services/ApivaultServices";
import { handleSearch } from "~/pages/functions/searchEngine";

const layouts = "body-content";
const route = useRoute();
const categoryTitle = route.params.category as string;
const isLoading = ref(true);
const isNullCategory = ref(null);
const apiData: Ref<APIType[]> = ref([]);
const apiSearched: Ref<APIType[]> = ref([]);
const categorySearched = reactive({
  category: "",
});
const showList = ref(true);

useHead({
  title: `${route.params.category} APIs List`,
});

const handleSearchCategory = (val: string, title: string) => {
  handleSearch(
    val,
    title,
    apiData,
    apiSearched,
    categorySearched,
    categoryTitle.toUpperCase(),
    showList
  );
};

onMounted(async () => {
  apiData.value = await ApivaultServices.apiCategoryData(route.params.category);
  isNullCategory.value ? apiData.value.length === 0 : false;
  isLoading.value = false;
});
</script>
