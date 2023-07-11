<template>
  <div class="glass-card card h-100">
    <div class="card-header-wrapper">
      <div class="card-header-column">
        <div class="text-wrapper text-wrapper-header-card mb-2">
          {{ title }}
        </div>
        <p
          style="padding: 3px"
          class="text-wrapper card-subtitle mb-2 pe-2 category-container text-body-secondary"
        >
          <NuxtLink :to="`/categories/${subtitle}`" class="subtitle-link">
            <font-awesome-icon
              class="mx-2 icon-color"
              width="12"
              height="12"
              :icon="categoriesDict[subtitle]"
            />{{ subtitle }}
          </NuxtLink>
        </p>
      </div>
      <div>
        <FaviconCardApi :url="getFavicon(faviconSrc, 128)" />
      </div>
    </div>
    <div class="padding-wrapper card-body">
      <p class="text-wrapper card-text-wrapper card-text">
        {{ body }}
      </p>
    </div>
    <div class="card-body attributes-container">
      <CardAttributes v-if="cors"> CORS </CardAttributes>
      <CardAttributes :id="https ? 'none' : 'warnOrNot'">
        {{ https ? "HTTPS" : "Not HTTPS" }}</CardAttributes
      >
      <CardAttributes v-if="auth !== ''">
        {{ auth?.toUpperCase() }}</CardAttributes
      >
      <GenericsLikeButton
        v-if="!isPending"
        @like:isClicked="likeInteractionHandler"
        :likedByUser="likedByUser"
        :isAuthState="isAuthState"
        style="margin-left: auto !important; text-decoration: none"
      />
      <GenericsLikeNumber v-if="!isPending" :class="{ animate: animate }">
        {{ like }}
      </GenericsLikeNumber>
      <!-- <GenericsBookmarkButton style="text-decoration: none" /> -->
    </div>
  </div>
</template>

<script lang="ts" setup>
import { categoriesDict } from "~/utils/categoryMapping";
import ApivaultServices from "~/services/ApivaultServices";

let {
  id,
  title,
  subtitle,
  body,
  cors,
  https,
  auth,
  faviconSrc,
  isLikedByUser,
  likesCount,
} = defineProps({
  id: {
    type: Number,
    required: true,
  },
  title: {
    type: String,
    required: true,
  },
  subtitle: {
    type: String,
    required: true,
  },
  body: {
    type: String,
    required: true,
  },
  cors: {
    type: undefined,
    required: false,
  },
  https: {
    type: Boolean,
    required: false,
  },
  auth: {
    type: String,
    required: false,
  },
  faviconSrc: {
    type: String,
    required: true,
  },
  isLikedByUser: {
    type: Boolean,
    required: true,
  },
  likesCount: {
    type: Number,
    required: false,
  },
  isPending: {
    type: Boolean,
    required: false,
  },
});

let likedByUser = ref(isLikedByUser);

/* Definitions for auth handling */
const emit = defineEmits(["auth:isAuth"]);
const accessToken = useCookie("accessToken");
const isAuthState = ref<boolean>(false);

/* Handle the isClicked event returned by LikeButton component */
const like = ref<number>(likesCount!);
const animate = ref<boolean>(false);

/* This event is needed to spawn the noAuth error message */
const emitAuthError = () => {
  likedByUser.value = false;
  emit("auth:isAuth", false);
};

/* Handle interaction API (like/dislike) */
const likeInteractionHandler = async () => {
  let statusCode: Number;
  if (likedByUser.value) {
    statusCode = await ApivaultServices.dislike(id, accessToken.value!);
  } else {
    statusCode = await ApivaultServices.like(id, accessToken.value!);
  }

  switch (statusCode) {
    case 201:
      like.value++;
      likedByUser.value = true;
      break;
    case 204:
      like.value--;
      likedByUser.value = false;
      break;
    case 401:
      emitAuthError();
      break;
    default:
      likedByUser.value = false;
      console.error(`Status code error: ${statusCode}`);
      break;
  }
};

/* Call google services api to get favicon image */
const getFavicon = (url: string, size: number) => {
  return `https://www.google.com/s2/favicons?domain=${url}&sz=${size}`;
};
</script>

<style scoped>
.animate {
  animation: moveUp 0.2s;
}

@keyframes moveUp {
  0% {
    transform: translateY(0%);
  }

  50% {
    transform: translateY(-45%);
  }

  100% {
    transform: translateY(0%);
  }
}

#warnOrNot {
  background: var(--bg-attribute-warn) !important;
  color: var(--text-attribute-warn) !important;
}

.warn-attribute p {
  color: var(--text-attribute-warn) !important;
}

.icon-color {
  color: var(--icon-color);
}

.padding-wrapper {
  padding: 12px !important;
}

.category-container {
  align-self: start;
  border-radius: 4px;
  background: var(--bg-trending-category);
  color: var(--text-card-color) !important;
  font-size: small;
  margin-left: 0;
  margin-right: 4px;
  margin-top: auto;
  max-width: 15rem;
  justify-content: center;
}

.category-container:hover {
  background: var(--bg-card-glass-hover);
  transition: background 0.1s ease-in-out;
}

.glass-card {
  backdrop-filter: blur(16px) saturate(200%);
  -webkit-backdrop-filter: blur(16px) saturate(200%);
  background-color: var(--bg-card-glass);
  border-radius: 8px;
  border: 1px solid var(--border-color-cards);
  transition-property: scale, background-color;
  transition: 0.3s ease !important;
}

#icon1,
#icon2 {
  color: var(--text-color) !important;
}

.text-wrapper-header-card {
  font-weight: 600;
  font-size: 18px;
}

.text-body-secondary {
  font-weight: 600;
}

.card-text-wrapper {
  font-size: 15px;
}

.card-header-wrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin: 12px;
  margin-bottom: 0;
}

.card-header-column {
  display: flex;
  flex-direction: column;
}

.attributes-container {
  display: flex;
  flex-direction: row;
  padding: 12px;
}

.subtitle-link {
  color: var(--text-card-color);
  text-decoration: none;
}

@media only screen and (min-width: 1500px) {
  .glass-card {
    backdrop-filter: blur(16px) saturate(200%);
    -webkit-backdrop-filter: blur(16px) saturate(200%);
    background-color: var(--bg-card-glass);
    border-radius: 8px;
  }
}

@media only screen and (min-width: 1024px) {
  .glass-card {
    backdrop-filter: blur(16px) saturate(200%);
    -webkit-backdrop-filter: blur(16px) saturate(200%);
    background-color: var(--bg-card-glass);
    border-radius: 8px;
  }
}

@media only screen and (max-width: 600px) {
  .text-wrapper-header-card {
    font-weight: 600;
    font-size: 20px;
    margin-left: 2vw;
  }
  .card-text-wrapper {
    font-size: 15px;
    margin-left: 2vw;
  }
}

.glass-card:hover {
  border: solid 1px var(--icon-color);
  transition: scale 0.1s ease-in-out;
}
</style>
