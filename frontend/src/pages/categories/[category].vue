<template>
  <BodyFlex>
    <header>
      <Navbar />
    </header>
    <Sidebar />
    <ContentBody
      :title="route.params.category.toUpperCase()"
      :isNullCategory="isNullCategory"
    >
      <template #topAreaContent>
        <SearchBar />
      </template>
      <template #heroAreaContent>
        <Hero @update:colorScheme="handleChangeScheme" />
      </template>
      <template #cardAreaContent>
        <div class="row">
          <div
            class="col-12 col-lg-4 col-md-6 mb-4 mb-md-4"
            v-for="api in apiData"
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
import axios from "axios";

const categoriesAttributes = inject("categoryMapping");
const route = useRoute();
const router = useRouter();

const scheme = reactive({
  color: "dark",
});

const handleChangeScheme = (val) => {
  scheme.color = val;
  console.log(scheme.color);
};

const categoryExist = categoriesAttributes.some(
  (category) => category.name === route.params.category
);

if (!categoryExist) {
  router.push("/error404");
}

let isNullCategory = ref(null);
let apiData = ref(null);
const apiCall = async () => {
  await axios
    .get(`http://localhost:5001/api/all?categorie=${route.params.category}`)
    .then((res) => {
      apiData.value = res.data;
      isNullCategory.value = true ? apiData.value.length === 0 : false;
    })
    .catch((er) => {
      console.error(er);
    });
};

onMounted(async () => {
  await apiCall();
});

onBeforeUpdate(async () => {
  await apiCall();
});
</script>
