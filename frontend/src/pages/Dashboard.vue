<script setup>
import ContentBody from "@/layouts/ContentBody.vue";
import SearchBar from "@/components/SearchBar.vue";
import Sidebar from "@/components/Sidebar.vue";
import { onMounted, reactive, ref } from "vue";
import BodyFlex from "@/layouts/BodyFlex.vue";
import Footer from "@/components/Footer.vue";
import Navbar from "@/components/Navbar.vue";
import Card from "@/components/Card.vue";
import Hero from "@/components/Hero.vue";
import axios from "axios";

const scheme = reactive({
  color: "dark",
});

const handleChangeScheme = (val) => {
  scheme.color = val;
  console.log(scheme.color);
};

let apiData = ref(null);
const apiCall = async () => {
  await axios
    .get("http://localhost:5001/api/random")
    .then((res) => {
      apiData.value = res.data;
    })
    .catch((er) => {
      console.error(er);
    });
};

onMounted(() => {
  apiCall();
});
</script>

<template>
  <BodyFlex>
    <header>
      <Navbar />
    </header>
    <Sidebar />
    <ContentBody>
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
