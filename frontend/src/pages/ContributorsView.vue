<template>
  <BodyFlex>
    <header>
      <Navbar />
    </header>
    <Sidebar />
    <ContentBody title="WONDERFUL PEOPLE ❤️">
      <template #heroAreaContent>
        <Hero />
      </template>
      <template #cardAreaContent>
        <div class="row">
          <LoadingEffect v-if="isLoading" />
          <div
            class="col-3 col-lg-1 col-md-2 mb-4 mb-md-4"
            v-for="contributor in contributors"
            :key="contributor"
          >
            <WonderfulPerson
              :profile="contributor.html_url"
              :avatarUrl="contributor.avatar_url"
            />
          </div>
        </div>
      </template>
      <template #footerArea>
        <Footer />
      </template>
    </ContentBody>
  </BodyFlex>
</template>

<script setup>
import ContentBody from "@/layouts/ContentBody.vue";
import Sidebar from "@/components/Sidebar.vue";
import { onMounted, reactive, ref } from "vue";
import BodyFlex from "@/layouts/BodyFlex.vue";
import Footer from "@/components/Footer.vue";
import Navbar from "@/components/Navbar.vue";
import Hero from "@/components/Hero.vue";
import LoadingEffect from "@/components/LoadingEffect.vue";
import WonderfulPerson from "@/components/WonderfulPerson.vue";
import getContributors from "@/components/api/getGithubContributors";

let isLoading = ref(true);
let contributors = ref(null);
onMounted(async () => {
  contributors.value = await getContributors();
  isLoading.value = false;
});
</script>
