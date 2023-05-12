<template>
  <div class="glass-card card h-100">
    <div class="card-header-wrapper">
      <div class="card-header-column">
        <div class="text-wrapper text-wrapper-header-card mb-2">
          {{ title }}
        </div>
        <h6 class="text-wrapper card-subtitle mb-2 text-body-secondary">
          <font-awesome-icon
            class="mx-2"
            width="12"
            height="12"
            :icon="cat"
          />{{ subtitle }}
        </h6>
      </div>
      <div class="logo-container">
        <FaviconCardApi :url="getFavicon(faviconSrc, 128)" />
      </div>
    </div>
    <div class="card-body">
      <p class="text-wrapper card-text-wrapper card-text">
        {{ body }}
      </p>
    </div>
    <div class="card-body attributes-container">
      <CardAttributes v-if="isNullProp">
        <font-awesome-icon
          id="icon1"
          class="me-1 icon-color"
          width="12"
          height="12"
          :icon="['fas', 'check']"
        />{{ props.cors === "yes" ? "CORS" : null }}
      </CardAttributes>
      <CardAttributes>
        <font-awesome-icon
          id="icon2"
          class="me-1 icon-color"
          width="12"
          height="12"
          :icon="['fas', 'check']"
        />{{ props.HTTPS ? "HTTP" : "HTTPS" }}</CardAttributes
      >
      <CardAttributes v-if="props.auth !== ''">
        <font-awesome-icon
          id="icon2"
          class="me-1 icon-color"
          width="12"
          height="12"
          :icon="['fas', 'check']"
        />{{ props.auth !== "" ? `${props.auth}` : null }}</CardAttributes
      >
    </div>
  </div>
</template>

<script setup>
import CardAttributes from "@/components/CardAttributes.vue";
import FaviconCardApi from "@/components/FaviconCardApi.vue";
import { inject, ref, onMounted } from "vue";

const categoryMap = inject("categoryMapping");
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
    required: true,
  },
  https: {
    type: Boolean,
    required: true,
  },
  auth: {
    type: String,
    required: true,
  },
  faviconSrc: {
    type: String,
    required: false,
  },
});

let isNullProp = ref(null);
if (props.cors === "no" || props.cors === "unknown") {
  isNullProp.value = false;
} else {
  isNullProp.value = true;
}

let cat = ref("");
/**

Finds an element in the categoryMap array with a name property 
that matches the subtitle property passed in as a prop. 
If a match is found, sets the value of cat.value to the icon 
property of the matching element.
@returns {String} icon
*/
const iconCategory = () => {
  categoryMap.find((el) => {
    if (el.name === props.subtitle) {
      cat.value = el.icon;
    }
  });
};

const getFavicon = (url, size) => {
  return `https://www.google.com/s2/favicons?domain=${url}&sz=${size}`;
};

onMounted(() => {
  iconCategory();
});
</script>

<style scoped>
.glass-card {
  backdrop-filter: blur(16px) saturate(200%);
  -webkit-backdrop-filter: blur(16px) saturate(200%);
  background-color: var(--bg-card-glass);
  border-radius: 12px;
  /* border: 1px solid var(--border-color-cards); */
}

.logo-container {
  align-self: center;
}

#icon1,
#icon2 {
  color: var(--text-color) !important;
}

.text-wrapper-header-card {
  /* align-self: center; */
  font-weight: 600;
  font-size: 20px;
  margin-left: 0.3vw;
}

.text-body-secondary {
  font-weight: 600;
}

.card-text-wrapper {
  font-size: 17.4px;
}

.card-header-wrapper {
  /* border-bottom: 0.3px solid gray; */
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin: 1rem;
  margin-bottom: 0;
}

.card-header-column {
  display: flex;
  flex-direction: column;
}

.attributes-container {
  display: flex;
  flex-direction: row;
}

@media only screen and (min-width: 1500px) {
  .glass-card {
    backdrop-filter: blur(16px) saturate(200%);
    -webkit-backdrop-filter: blur(16px) saturate(200%);
    background-color: var(--bg-card-glass);
    border-radius: 12px;
    /* border: 1px solid var(--border-color-cards); */
  }
}

@media only screen and (min-width: 1024px) {
  .glass-card {
    backdrop-filter: blur(16px) saturate(200%);
    -webkit-backdrop-filter: blur(16px) saturate(200%);
    background-color: var(--bg-card-glass);
    border-radius: 12px;
    /* border: 1px solid var(--border-color-cards); */
  }
}

@media only screen and (max-width: 600px) {
  .text-wrapper-header-card {
    font-weight: 600;
    font-size: 20px;
    margin-left: 2vw;
  }
  .card-text-wrapper {
    font-size: 17.4px;
    margin-left: 2vw;
  }
}

.glass-card:hover {
  background-color: var(--bg-card-glass-hover);
  scale: 1.01;
  transition: scale 0.1s ease-in-out;
}
</style>
