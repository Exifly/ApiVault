<script setup>
import CardAttributes from "@/components/CardAttributes.vue";
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
});

let isNullProp = ref(null);
if (props.cors === "no" || props.cors === "unknown") {
  isNullProp.value = false;
} else {
  isNullProp.value = true;
}

let cat = ref("");
const iconCategory = () => {
  categoryMap.find((el) => {
    if (el.name === props.subtitle) {
      cat.value = el.icon;
    }
  });
};

onMounted(() => {
  iconCategory();
  console.log(props.https);
});
</script>

<template>
  <div class="glass-card card">
    <div class="card-header-wrapper">
      <div class="logo-container">
        <img
          src="https://exifly.it/assets/img/no_bg_black%202.png"
          class="favicon-api"
          alt="webLogo"
          style="border-radius: 12px"
        />
      </div>
      <div class="text-wrapper text-wrapper-header-card">{{ title }}</div>
    </div>
    <div class="card-body mt-3">
      <h6 class="text-wrapper card-subtitle mb-2 text-body-secondary">
        <font-awesome-icon class="mx-2" width="12" height="12" :icon="cat" />{{
          subtitle
        }}
      </h6>
      <p class="text-wrapper card-text">
        {{ body }}
      </p>
      <div class="attributes-container">
        <CardAttributes v-if="isNullProp">
          {{ props.cors === "yes" ? "CORS" : null }}
        </CardAttributes>
        <CardAttributes> {{ props.HTTPS ? "HTTP" : "HTTPS" }}</CardAttributes>
        <CardAttributes>{{
          props.auth !== "" ? `Auth: ${props.auth}` : null
        }}</CardAttributes>
      </div>
    </div>
  </div>
</template>

<style scoped>
.glass-card {
  backdrop-filter: blur(16px) saturate(200%);
  -webkit-backdrop-filter: blur(16px) saturate(200%);
  background-color: var(--bg-card-glass);
  /* background-color: rgba(var(--bg-color), 0.78); */
  border-radius: 12px;
  border: 1px solid var(--border-color-cards);
}

.text-wrapper-header-card {
  align-self: center;
  font-weight: 600;
  font-size: 20px;
  margin-left: 0.3vw;
}

.card-header-wrapper {
  border-bottom: 0.3px solid gray;
  display: flex;
  flex-direction: row;
}

.favicon-api {
  background: var(--bg-color);
  border-radius: 12px;
  border: 0.01px solid var(--border-color-cards);
  margin-left: 1vw;
  width: 64px;
  height: 64px;
  align-self: center;
  margin-bottom: -13px;
  margin-top: 12px;
}

.attributes-container {
  display: flex;
  flex-direction: row;
}

@media only screen and (max-width: 600px) {
  .text-wrapper-header-card {
    align-self: center;
    font-weight: 600;
    font-size: 20px;
    margin-left: 3.3vw;
  }
  .favicon-api {
    background: var(--bg-color);
    border-radius: 12px;
    border: 0.01px solid var(--border-color-cards);
    margin-left: 4vw;
    width: 64px;
    height: 64px;
    align-self: center;
    margin-bottom: -13px;
    margin-top: 12px;
  }
}
</style>
