<template>
  <form @submit.prevent="searchForApi">
    <div class="search-bar text-black" >
      <label>
        <LoadingEffectSmall v-if="loadingState" class="ms-2" />
        <font-awesome-icon
          v-else
          class="icon-color"
          :icon="['fas', 'magnifying-glass']"
          style="margin-left: 1em; margin-right: 1vw"
        />
        <input
          v-model="query"
          class="input-bar"
          type="search"
          placeholder="Search"
        />
      </label>
    </div>
  </form>
</template>

<script lang="ts" setup>
import ApivaultServices from "~/services/ApivaultServices";

const emit = defineEmits(["search:apiSearch", "search:apiSearchTitle"]);
const accessToken = useCookie("accessToken");
const loadingState = ref<boolean>(false);

/**
Computes a filtered list of API data based on the value of apiInputSearch. 
If apiInputSearch has at least 4 characters, emits a "search:apiSearch" event 
with the filtered list of APIs and the apiInputSearch object. Otherwise, emits a 
"search:apiSearch" event with a false value.
@returns {undefined}
*/
const query = ref<string>("");
const searchForApi = async () => {
  loadingState.value = true;
  if (query.value.length < 3) { loadingState.value = false; return };
  const response = await ApivaultServices.search(query.value, accessToken.value!);

  switch (response.length) {
    case 0:
      emit("search:apiSearch", false);
      loadingState.value = false;
      break;
    default:
      emit("search:apiSearch", response, query.value);
      loadingState.value = false;
      break;
  }
}
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
  border-radius: 8px;
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
  height: 1rem;
}

label {
  --search-radius: 8px;
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
  height: 3rem;
}

label:focus-within::before {
  content: "";
  height: 1200px;
  width: 100%;
  background: linear-gradient(90deg, var(--bg-input-field), #fe332f);
  position: absolute;
  z-index: -2;
  animation: borderGradient 3.5s linear infinite;
}

label:focus-within::after {
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

label > input {
  outline: none;
  border: none;
  background: transparent;
  padding: 1rem 0;
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
