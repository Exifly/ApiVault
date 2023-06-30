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
      <div class="row justify-content-center align-content-center mt-4">
        <div class="col-12 col-md-6">
          <a
            href="https://github.com/Exifly/ApiVault/graphs/contributors"
            target="_blank"
          >
            <GenericsButton
              class="d-flex align-self-center align-items-center justify-content-center"
            >
              <font-awesome-icon class="me-2" :icon="['fab', 'github']" />
              Become a contributor
            </GenericsButton>
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
