<script setup>
import ContentBody from "@/layouts/ContentBody.vue";
import SearchBar from "@/components/SearchBar.vue";
import Sidebar from "@/components/Sidebar.vue";
import { onMounted, reactive, ref, onBeforeUpdate } from "vue";
import BodyFlex from "@/layouts/BodyFlex.vue";
import Footer from "@/components/Footer.vue";
import Navbar from "@/components/Navbar.vue";
import Card from "@/components/Card.vue";
import Hero from "@/components/Hero.vue";
import { useRoute } from "vue-router";
import axios from "axios";

const route = useRoute();
const scheme = reactive({
  color: "dark",
});

const handleChangeScheme = (val) => {
  scheme.color = val;
  console.log(scheme.color);
};

//http://localhost:5001/api/search?q=data&category=develop

let isNullCategory = ref(null);
let apiData = ref(null);
const apiCall = async () => {
  await axios
    .get(
      `http://localhost:5001/api/search?q=data&category=${route.params.category}`
    )
    .then((res) => {
      apiData.value = res.data;
      isNullCategory.value = true ? apiData.value.length === 0 : false;
    })
    .catch((er) => {
      console.error(er);
    });
};

onBeforeUpdate(() => {
  apiCall();
});
</script>

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
