<template>
  <NuxtLayout :name="layouts" title="Pending APIs">
    <template #topAreaContent>
      <Transition>
        <GenericsToastNotification v-if="isAuth" class="mt-3">
          You are not authorized to perform this action. Please signin!
        </GenericsToastNotification>
      </Transition>
    </template>
    <template #cardAreaContent>
      <GenericsButton
        data-bs-toggle="modal" data-bs-target="#submitApiModal"
        v-if="noPendingApiFound"
        class="d-flex align-self-center align-items-center justify-content-center"
      >
        <font-awesome-icon class="me-2" :icon="['fas', 'folder-plus']" />
        No API found, add new one
      </GenericsButton>
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
      <!-- My APIs section -->
      <h1 class="text-wrapper">My APIs</h1>
      <hr v-if="!noApiFound" />
      <GenericsButton
        data-bs-toggle="modal" data-bs-target="#submitApiModal"
        v-if="noApiFound"
        class="d-flex align-self-center align-items-center justify-content-center"
      >
        <font-awesome-icon class="me-2" :icon="['fas', 'folder-plus']" />
        No API found, add new one
      </GenericsButton>
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
            v-for="api in myApis"
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
import { APIType } from "~/models/types";
import ApivaultServices from "~/services/ApivaultServices";

const layouts = "body-content";
const isLoading = ref(true);
const isNullCategory = ref(true);
const isAuth = ref<boolean>(false);
const pendingApis: Ref<APIType[]> = ref([]);
const myApis: Ref<APIType[]> = ref([]);
const apiSearched: Ref<APIType[]> = ref([]);
const accessToken = useCookie("accessToken") || null;
const showList = ref(true);
const noApiFound = ref<boolean>(false);
const noPendingApiFound = ref<boolean>(false);

useHead({
  title: 'My personal APIs List',
  meta: [
    {
      name: "description",
      content: `A List of my personal APIs!`,
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

const router = useRouter();
onMounted(async () => {
  if (!accessToken.value || accessToken.value === null || accessToken.value === "") router.push('/');
  pendingApis.value = await ApivaultServices.pendingApis(accessToken.value!);
  myApis.value = await ApivaultServices.myApis(accessToken.value!);
  if (pendingApis.value.length === 0) noPendingApiFound.value = true;
  if (myApis.value.length === 0) noApiFound.value = true;

  isNullCategory.value ? pendingApis.value.length === 0 : false;
  isLoading.value = true
    ? pendingApis.value === null || pendingApis.value === undefined
    : false;
 
  if (apiSearched.value === null || apiSearched.value.length === 0) { 
    apiSearched.value = pendingApis.value;
  }
});
</script>
