<template>
  <div class="search-bar text-black">
    <label
      ><font-awesome-icon
        class="icon-color"
        :icon="['fas', 'magnifying-glass']"
        style="margin-left: 1em; margin-right: 1vw"
      />
      <input
        v-model="apiInputSearch"
        class="input-bar"
        type="search"
        placeholder="Search"
      />
      <p style="color: white !important" v-for="api in apis" :key="api">
        {{ api.API }}
      </p>
    </label>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from "vue";
import getAllApi from "@/components/api/allApis.js";

const emit = defineEmits(["search:apiSearch", "search:apiSearchTitle"]);
const apiInputSearch = ref("");

/**
Computes a filtered list of API data based on the value of apiInputSearch. 
If apiInputSearch has at least 4 characters, emits a "search:apiSearch" event 
with the filtered list of APIs and the apiInputSearch object. Otherwise, emits a 
"search:apiSearch" event with a value of false.
@returns {undefined}
*/
let data = [];
const apis = computed(() => {
  if (apiInputSearch.value.length >= 3) {
    emit(
      "search:apiSearch",
      data.filter(
        (api) =>
          api.API.toLowerCase().includes(apiInputSearch.value.toLowerCase()) |
          api.Category.toLowerCase().includes(
            apiInputSearch.value.toLocaleLowerCase()
          )
      ),
      apiInputSearch
    );
  } else {
    emit("search:apiSearch", false);
  }
});

onMounted(async () => {
  data = await getAllApi();
});
</script>

<style scoped>
@media only screen and (max-width: 600px) {
  .input-bar {
    width: 82.5vw;
  }
}
.icon-color {
  color: var(--icon-color);
}
.search-bar {
  align-items: center;
  border-radius: 16px;
  display: flex;
  justify-content: center;
  transition: all 0.3s ease-in-out;
  width: 100%;
}

.input-bar {
  border-style: transparent;
  border-color: transparent;
  color: var(--text-color);
  flex-grow: 1;
  margin-bottom: 0vh;
  height: 6vh;
}

label {
  --search-radius: 16px;
  --border-width: 2px;
  position: relative;
  overflow: hidden;
  z-index: 0;
  align-self: center;
  align-items: center;
  border-radius: var(--search-radius);
  border: 1px solid transparent;
  background-color: var(--bg-input-field);
  color: #6c757d;
  cursor: text;
  display: grid;
  grid-template: 1fr / auto 1fr;
  gap: 12px;
  width: 100%;
  transition: all 0.1s ease-in-out;
}

label::before {
  content: "";
  height: 1200px;
  width: 100%;
  background: linear-gradient(90deg, var(--bg-input-field), #fe332f);
  position: absolute;
  z-index: -2;
  animation: borderGradient 3.5s linear infinite;
}

label::after {
  content: "";
  height: calc(100% - var(--border-width));
  width: calc(100% - var(--border-width));
  background: var(--bg-input-field);
  top: 50%;
  left: 1px;
  transform: translateY(-50%);
  position: absolute;
  z-index: -1;
  border-radius: calc(var(--search-radius) - var(--border-width));
}

label:focus-within {
  border: 1px solid var(--icon-color);
}

label:focus-within::before,
label:focus-within::after {
  opacity: 0;
}

label > input {
  outline: none;
  border: none;
  background: transparent;
}

@keyframes borderGradient {
  0% {
    transform: rotateZ(1deg);
  }
  100% {
    transform: rotateZ(360deg);
  }
}
</style>
