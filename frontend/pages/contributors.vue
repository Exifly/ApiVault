<template>
  <NuxtLayout :name="layouts" title="WONDERFUL PEOPLE">
    <template #cardAreaContent>
      <div class="row align-content-center">
        <LoadingEffect v-if="isLoading" />
        <div
          class="col-3 col-lg-1 col-md-2 mb-4 mb-md-4"
          v-for="contributor in contributors"
          :key="contributor.id"
        >
          <WonderfulPerson
            :profile="contributor.html_url"
            :avatarUrl="contributor.avatar_url"
          />
        </div>
      </div>
      <div class="row justify-content-center align-content-center">
        <div class="col-12 col-md-6">
          <GenericsCard
            class="glow-effect mt-2"
            title="❤️ THANK YOU ❤️"
            body="Thanks to everyone on this list! We are so happy to work with you! "
            imageUrl="https://purepng.com/public/uploads/large/heart-icon-jst.png"
            ><GenericsButton
              class="glow-effect d-flex align-self-center justify-content-center"
            >
              <font-awesome-icon :icon="['fab', 'github']" /> </GenericsButton
          ></GenericsCard>
        </div>
      </div>
    </template>
    <template #footerArea>
      <Footer />
    </template>
  </NuxtLayout>
</template>

<script lang="ts" setup>
import { GithubContributor } from "~/models/types";
import GithubService from "~/services/GithubServices";

useHead({
  title: "APIVault contributors",
});

const layouts = "body-content";
let isLoading = ref(true);
let contributors = ref<GithubContributor[]>([]);

onMounted(async () => {
  contributors.value = await GithubService.contributors();
  isLoading.value = false;
});
</script>
