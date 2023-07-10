<template>
  <NuxtLayout :name="layouts" :title="categorySearched.category">
    <template #heroAreaContent>
      <Hero :heroTitle="heroTitle" />
    </template>
    <template #topAreaContent>
      <SearchBar @search:apiSearch="handleSearchCategory" />
      <Transition>
        <GenericsToastNotification v-if="isAuth" class="mt-3">
          You are not authorized to perform this action. Please signin!
        </GenericsToastNotification>
      </Transition>
    </template>
    <template #cardAreaContent>
      <div class="row" v-if="showList">
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
              class="text-white text-decoration-none"
              :href="api.url"
              target="_blank"
            >
              <CardAPI
                @auth:isAuth="handleAuthState"
                :id="api.id"
                :title="api.name"
                :subtitle="api.category"
                :body="api.description"
                :cors="api.cors"
                :https="api.https"
                :auth="api.auth"
                :faviconSrc="api.url"
                :likesCount="api.likes_count"
                :isLikedByUser="api.liked_by_user"
              />
            </a>
          </div>
        </TransitionGroup>
      </div>
    </template>
    <template #footerArea>
      <Footer />
    </template>
  </NuxtLayout>
</template>

<script lang="ts" setup>
import { APIType } from "../../models/types";
import ApivaultServices from "../../services/ApivaultServices";

const layouts = "body-content";
const route = useRoute();
const categoryTitle = route.params.category as string;
const heroTitle = `Your Free and Public ${categoryTitle} API List`;
const isLoading = ref(true);
const isNullCategory = ref(null);
const isAuth = ref<boolean>(false);
const apiData: Ref<APIType[]> = ref([]);
const apiSearched: Ref<APIType[]> = ref([]);
const accesToken = useCookie("accessToken") || null;
const categorySearched = reactive({
  category: categoryTitle.toUpperCase(),
});
const showList = ref(true);

useHead({
  title: `${route.params.category} APIs List`,
  meta: [
    {
      name: "description",
      content: `A List of your favourite ${route.params.category} APIs. For Free!`,
    },
  ],
});

/* 
  Handler for cardApi auth event emit (return false if user is not authorized) 
  It's needed to handle the notification error
*/
const handleAuthState = (isAuthError: boolean) => {
  if (!isAuthError) isAuth.value = true;
  setTimeout(() => {
    isAuth.value = false;
  }, 4000);
}

const handleSearchCategory = (val: string, title: string) => {
  if (title === undefined) {
    apiSearched.value = apiData.value;
    showList.value = true;
  } else if (val.length > 0) {
    categorySearched.category = title.toUpperCase();
    apiSearched.value = val as any;
    showList.value = true;
  } 
};

onMounted(async () => {
  apiData.value = await ApivaultServices.apiCategoryData(route.params.category, accesToken.value!);
  isNullCategory.value ? apiData.value.length === 0 : false;
  isLoading.value = true
    ? apiData.value === null || apiData.value === undefined
    : false;
 
  if (apiSearched.value === null || apiSearched.value.length === 0) { 
    apiSearched.value = apiData.value;
  }
});
</script>
