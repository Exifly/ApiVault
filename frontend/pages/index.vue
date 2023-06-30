<template>
  <NuxtLayout :name="layouts" :title="categorySearched.category">
    <template #heroAreaContent>
      <Hero />
    </template>
    <template #topAreaContent>
      <SearchBar @search:apiSearch="handleSearchDashboard" />
      <Transition>
        <GenericsToastNotification v-if="isAuth" class="mt-3">
          You are not authorized to perform this action. Please signin!
        </GenericsToastNotification>
      </Transition>
    </template>
    <template #trendingCategories>
      <h1 id="title-trending" class="text-wrapper mb-3">TRENDING</h1>
      <div class="trend-container mb-3" v-if="!isLoading">
        <TransitionGroup name="cards">
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
                :icon="categoriesDict[category.name]"
              />{{ category.name }}
              <span class="api_count mx-1">({{ category.api_count }})</span>
            </NuxtLink>
          </TrendCategory>
        </TransitionGroup>
      </div>
      <div class="trend-container mb-3" v-else>
        <TransitionGroup name="cards">
          <TrendCategory
            class="skeleton-box"
            style="height: 30px"
            v-for="category in 10"
            :key="category"
          />
        </TransitionGroup>
        <hr />
      </div>
    </template>
    <template #cardAreaContent>
      <div class="row">
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
              v-if="showList"
              :href="api.url"
              target="_blank"
              style="text-decoration: none"
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
      <div class="row mt-4">
        <LoadMoreButton
          class="mb-4"
          v-if="showLoadMore"
          @click="handleLoadMore"
          :isLoading="isLoadingState"
        />
      </div>
      <hr />
      <section id="sponsorSection" class="sponsor-section">
        <h1
          id="title-sponsor"
          class="text-wrapper mb-3"
          style="text-align: center"
        >
          WE ARE SUPPORTED BY THOSE <br />
          AMAZING FRIENDS
        </h1>
        <a href="#">
          <GenericsButton class="mt-2 sponsor-button">
            <font-awesome-icon class="me-2" :icon="['fas', 'heart']" /> Become a
            sponsor
          </GenericsButton>
        </a>
      </section>
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

// adding cookie script
useHead({
  script: [
    {
      src: "https://app.enzuzo.com/apps/enzuzo/static/js/__enzuzo-cookiebar.js?uuid=f59a7360-00b5-11ee-a49e-231d479eb14f",
    },
  ],
});

// layout name
const layouts: string = "body-content";

// trending and random data
const trendCategoriesList = ref<TrendingCategory[]>();
const apiData: any = ref([]);

// search bar data
const apiSearched: Ref<APIType[]> = ref([]);
const categorySearched = reactive({
  category: "RANDOM",
});

/* auth state */
const isAuth = ref<boolean>(false);
const accessToken = useCookie("accessToken");

/* 
  Handler for cardApi auth event emit (return false if user is not authorized) 
  It's needed to handle the notification error
*/
const handleAuthState = (isAuthError: boolean) => {
  if (!isAuthError) isAuth.value = true;
  setTimeout(() => {
    isAuth.value = false;
  }, 4000);
};

// loading state animation
const isLoading = ref(true);
const showList = ref(true);

// loading more state
let isLoadingState = ref(false);
let hasMoreData = ref(true);

// wrapper for handleSearch function
const handleSearchDashboard = (val: string, title: string) => {
  handleSearch(
    val,
    title,
    apiData,
    apiSearched,
    categorySearched,
    "RANDOM",
    showList
  );
};

// this computed property is used for manage the data state for load more
const showLoadMore = computed(() => {
  return (
    hasMoreData.value &&
    categorySearched.category === "RANDOM" &&
    !isLoading.value
  );
});

// this function is used to handle the load more event
const handleLoadMore = async () => {
  isLoadingState.value = true;
  setTimeout(async () => {
    const newData = await ApivaultServices.randomApis(accessToken.value!);
    const filteredData = newData.filter((newItem) => {
      return !apiSearched.value.some(
        (existingItem: any) => existingItem.url === newItem.url
      );
    });
    if (filteredData.length === 0) {
      hasMoreData.value = false;
      isLoadingState.value = false;
    } else {
      apiSearched.value = [...apiSearched.value, ...filteredData];
      isLoadingState.value = false;
    }
  }, 200);
};

onBeforeMount(async () => {
  trendCategoriesList.value = await ApivaultServices.getTrendingCategories()!;
  apiData.value = await ApivaultServices.randomApis(accessToken.value!);
  isLoading.value = true
    ? apiData.value === null || apiData.value === ""
    : false;

  if (apiSearched.value === null || apiSearched.value.length === 0) { 
    apiSearched.value = apiData.value;
  }
});

onMounted(async () => {
  showList.value = true;
});
</script>

<style scoped>
.sponsor-section {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}

.sponsor-section h1 {
  font-size: 24px;
}

.sponsor-section .sponsor-button {
  font-size: 14px;
  width: 100%;
}

@media only screen and (max-width: 600px) {
  #title-trending {
    display: none;
  }
  .trend-container {
    display: none !important;
  }
  .sponsor-section .sponsor-button {
    font-size: 20px;
    width: 100%;
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
