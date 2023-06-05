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
              :icon="cat"
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
      <CardAttributes v-if="isNullProp">
        {{ props.cors ? "CORS" : null }}
      </CardAttributes>
      <CardAttributes :id="props.https ? 'none' : 'warnOrNot'">
        {{ props.https ? "HTTPS" : "Not HTTPS" }}</CardAttributes
      >
      <CardAttributes v-if="props.auth !== ''">
        {{ props.auth !== "" ? `${props.auth}` : null }}</CardAttributes
      >
    </div>
  </div>
</template>

<script lang="ts" setup>
import { categoriesProperties } from "~/utils/categoryMapping";
import { CategoryObject } from "~/models/types";
import { ref, onMounted } from "vue";

const categoryMap: CategoryObject | CategoryObject[] = categoriesProperties;
const props = defineProps({
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
});

const isNullProp = ref<boolean>(false);
if (!props.cors || props.cors === "unknown") {
  isNullProp.value = false;
} else {
  isNullProp.value = true;
}

const cat: any = ref("");
/**
Finds an element in the categoryMap array with a name property
that matches the subtitle property passed in as a prop.
If a match is found, sets the value of cat.value to the icon
property of the matching element.
@returns {String} icon
*/
const iconCategory = () =>
  Array.isArray(categoryMap)
    ? categoryMap.find(
        (el) => el.name === props.subtitle && (cat.value = el.icon)
      )
    : categoryMap;

const getFavicon = (url: string, size: number) => {
  return `https://www.google.com/s2/favicons?domain=${url}&sz=${size}`;
};

onMounted(() => {
  iconCategory?.();
});
</script>

<style scoped>
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
  min-width: 3rem;
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
  border-radius: 12px;
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
    border-radius: 12px;
  }
}

@media only screen and (min-width: 1024px) {
  .glass-card {
    backdrop-filter: blur(16px) saturate(200%);
    -webkit-backdrop-filter: blur(16px) saturate(200%);
    background-color: var(--bg-card-glass);
    border-radius: 12px;
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
