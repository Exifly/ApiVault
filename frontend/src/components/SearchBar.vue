<template>
  <div class="search-bar text-black">
    <label
      ><font-awesome-icon
        class="icon-color"
        :icon="['fas', 'magnifying-glass']"
        style="margin-left: 1vw; margin-right: 1vw"
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
    <!-- <Button value="Categories" /> -->
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from "vue";
import getAllApi from "@/components/api/allApis.js";
import axios from "axios";

const emit = defineEmits(["search:apiSearch"]);
const apiInputSearch = ref("");

// this function filter all apis to get occurrencies in
// category or API name
let a = [];
const apis = computed(() => {
  if (apiInputSearch.value.length >= 4) {
    // start searching as user write something,
    // then send an event to parent with fetched data
    emit(
      "search:apiSearch",
      a.filter(
        (api) =>
          api.API.toLowerCase().includes(apiInputSearch.value.toLowerCase()) |
          api.Category.toLowerCase().includes(
            apiInputSearch.value.toLocaleLowerCase()
          )
      )
    );
  } else {
    emit("search:apiSearch", false);
  }
});

onMounted(async () => {
  a = await getAllApi();
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
  /* justify-content: center; */
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
