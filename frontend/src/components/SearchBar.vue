<template>
  <div class="search-bar text-black ">
    <label class="animation-box"
      ><font-awesome-icon
        class="icon-color"
        :icon="['fas', 'magnifying-glass']"
        style="margin-left: 1em; margin-right: 1vw"
      />
      <input
        v-model="apiInputSearch"
        class="input-bar "
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

.animation-box {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px;
  border: 1px solid #0000;
  border-radius: 16px;
  background: linear-gradient(#060606, #060606) padding-box, linear-gradient(
        var(--angle),
       #e02b0b,#fe957d,#ffffff,#fe957d,#e02b0b,#fe957d
      ) border-box;
  animation: 2s rotate linear infinite;
}

@keyframes rotate {
  to {
    --angle: 360deg;
  }
}

@property --angle {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: false;
}


label {
  align-self: center;
  align-items: center;
  border-radius: 16px;
  background-color: var(--bg-input-field);
  color: #6c757d;
  cursor: text;
  display: grid;
  grid-template: 1fr / auto 1fr;
  gap: 12px;
  width: 95%;
}

label:focus-within {
  border: 0.5px solid var(--icon-color);
}

label > input {
  outline: none;
  border: none;
  background: transparent;
}
</style>
