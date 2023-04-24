<template>
  <BodyFlex>
    <header>
      <Navbar />
    </header>
    <Sidebar />
    <ContentBody
      :title="categorySearched.category"
      :isNullCategory="isNullCategory"
    >
      <template #topAreaContent>
        <SearchBar @search:apiSearch="handleSearch" />
      </template>
      <template #heroAreaContent>
        <Hero @update:colorScheme="handleChangeScheme" />
      </template>
      <template #cardAreaContent>
        <div class="row">
          <div
            class="col-12 col-lg-4 col-md-6 mb-4 mb-md-4"
            v-for="api in apiSearched"
            :key="api"
          >
            <a :href="api.Link" style="text-decoration: none">
              <Card
                :title="api.API"
                :subtitle="api.Category"
                :body="api.Description"
                :cors="api.Cors"
                :https="api.HTTPS"
                :auth="api.Auth"
                :faviconSrc="api.Link"
              />
            </a>
          </div>
        </div>
      </template>
      <template #footerArea>
        <Footer :scheme="scheme.color" />
      </template>
    </ContentBody>
  </BodyFlex>
</template>

<script setup>
import { onMounted, reactive, ref, onBeforeUpdate, inject } from "vue";
import ContentBody from "@/layouts/ContentBody.vue";
import SearchBar from "@/components/SearchBar.vue";
import { useRoute, useRouter } from "vue-router";
import Sidebar from "@/components/Sidebar.vue";
import BodyFlex from "@/layouts/BodyFlex.vue";
import Footer from "@/components/Footer.vue";
import Navbar from "@/components/Navbar.vue";
import Card from "@/components/Card.vue";
import Hero from "@/components/Hero.vue";
import getApiData from "@/components/api/categoriesApi.js";

const categoriesAttributes = inject("categoryMapping");
const route = useRoute();
const router = useRouter();
const isNullCategory = ref(null);
const apiData = ref(null);

onMounted(async () => {
  apiData.value = await getApiData(route.params.category);
  isNullCategory.value = true ? apiData.value.length === 0 : false;
});

onBeforeUpdate(async () => {
  apiData.value = await getApiData(route.params.category);
  isNullCategory.value = true ? apiData.value.length === 0 : false;
});

const scheme = reactive({
  color: "dark",
});

const handleChangeScheme = (val) => {
  scheme.color = val;
};

const categoryExist = categoriesAttributes.some(
  (category) => category.name === route.params.category
);

if (!categoryExist) {
  router.push("/error404");
}

let apiSearched = ref(null);
let categorySearched = reactive({
  category: null,
});

const handleSearch = (val) => {
  if (val.length > 0) {
    categorySearched.category = val[0].Category.toUpperCase();
    apiSearched.value = val;
  } else {
    categorySearched.category = route.params.category.toUpperCase();
    apiSearched.value = apiData.value;
  }
};
</script>
