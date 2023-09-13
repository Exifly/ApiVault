<template>
  <div class="custom-props mobile-first border-right" id="sidebar-wrapper">
    <div class="scrollbox">
      <div class="sidebar-heading ms-4">MENU</div>
      <ul class="list-unstyled ps-0 text-black mx-4" role="tablist">
        <li class="mt-2 category-custom" role="tab">
          <ProductHuntBadge />
        </li>
        <li class="sidebar-text-wrapper mt-2 category-custom" role="tab">
          <NuxtLink
            class="flex items-center gap-2 px-2"
            to="/"
            title="Go back to the Homepage"
          >
            <font-awesome-icon
              class=""
              width="12"
              height="12"
              icon="fa-solid fa-house"
            />Home</NuxtLink
          >
        </li>
        <li class="sidebar-text-wrapper mt-2 category-custom" role="tab">
          <a
            class="flex items-center gap-2 px-2"
            title="Checkout our github repository"
            style="text-decoration: none"
            href="https://github.com/Exifly/ApiVault"
            target="_blank"
          >
            <font-awesome-icon
              class=""
              width="12"
              height="12"
              :icon="['fas', 'star']"
            />{{ stargazers }} Stars
          </a>
        </li>
        <li class="sidebar-text-wrapper mt-2 category-custom" role="tab">
          <a
            class="flex items-center gap-2 px-2"
            title="Checkout our github repository"
            style="text-decoration: none"
            href="https://github.com/Exifly/ApiVault"
            target="_blank"
          >
            <font-awesome-icon
              class=""
              width="12"
              height="12"
              :icon="['fab', 'github']"
            />Repository</a
          >
        </li>
        <li class="sidebar-text-wrapper mt-2 category-custom" role="tab">
          <a
            class="flex items-center gap-2 px-2"
            title="Sponsor APIVault"
            style="text-decoration: none"
            href="https://ko-fi.com/apivault"
          >
            <font-awesome-icon
              class=""
              width="12"
              height="12"
              icon="fa-solid fa-hand-holding-dollar"
            />Sponsor</a
          >
        </li>
        <li class="sidebar-text-wrapper mt-2 category-custom" role="tab">
          <NuxtLink
            class="flex items-center gap-2 px-2"
            title="Our contributors"
            style="text-decoration: none"
            to="/contributors"
          >
            <font-awesome-icon
              class=""
              width="12"
              height="12"
              icon="fa-solid fa-users"
            />Contributors</NuxtLink
          >
        </li>
      </ul>
      <div class="sidebar-heading ms-4">CATEGORIES</div>
      <div class="list-group list-group-flush">
        <ul class="list-unstyled ps-0 text-black mx-4" role="tablist">
          <li
            class="sidebar-text-wrapper mt-2 category-custom"
            role="tab"
            v-for="category in categoriesAttributes"
            :key="category.name"
          >
            <NuxtLink
              class="flex items-center gap-2 px-2"
              :title="`${category.name} API List`"
              :to="`/categories/${category.name}`"
            >
              <font-awesome-icon
                class=""
                width="12"
                height="12"
                :icon="category.icon"
              />{{ category.name }}</NuxtLink
            >
          </li>
          <hr />
          <li class="sidebar-heading" role="tab">INFO</li>
          <li
            class="sidebar-text-wrapper sidebar-info-text mt-2 category-custom"
            role="tab"
          >
            API Fetched: <b>{{ api.count }}</b>
          </li>
          <li
            class="sidebar-text-wrapper sidebar-info-text mt-2 category-custom"
            role="tab"
          >
            N. Categories: <b>{{ categoriesAttributes.length }}</b>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { reactive, onMounted } from "vue";
import { categoriesProperties } from "~/utils/categoryMapping";
import ApivaultServices from "~/services/ApivaultServices";
import GithubServices from "~/services/GithubServices";

const stargazers = ref();
const categoriesAttributes = categoriesProperties;
const api = reactive({
  count: 0,
});

onMounted(async () => {
  api.count = await ApivaultServices.countApis();
  stargazers.value = await GithubServices.repoStars().catch((er) => 0);
});
</script>

<style scoped>
::-webkit-scrollbar {
  width: 0px;
}
.scrollbox {
  overflow: scroll;
  height: 89vh;
}
.custom-props {
  background-color: var(--bg-color);
  position: fixed;
  margin-top: 3.4rem;
  height: 100vh;
  width: 20vw;
  font-size: 15px;
}

.category-custom:hover {
  color: rgb(166, 166, 166);
}

.sidebar-text-wrapper {
  color: var(--text-color) !important;
  text-decoration: none;
}

.sidebar-info-text {
  padding: 0.4rem 0.2rem;
}
.sidebar-text-wrapper a {
  color: var(--text-color-sidebar) !important;
  text-decoration: none;
  padding: 0.4rem 0.2rem;
}

.sidebar-text-wrapper:hover {
  color: var(--text-color-hover) !important;
  background-color: var(--bg-card-glass-hover);
  cursor: pointer;
  border-radius: 5px;
}

.sidebar-heading {
  color: var(--text-color-hover);
  font-size: 18px;
  font-weight: 600;
}

.router-link-active {
  background-color: var(--bg-card-glass-hover);
  border-radius: 5px;
}

.search-bar {
  margin-top: 5vh;
  margin-bottom: 5vh;
}

@media (min-width: 1581px) and (min-width: 1800px) {
  .custom-props {
    background-color: var(--bg-color);
    position: fixed;
    margin-left: 1vw;
    height: 100vh;
    width: 11vw;
    font-size: 14px;
  }
}

@media only screen and (max-width: 600px) {
  .mobile-first {
    display: none;
  }
}

@media only screen and (min-width: 1581px) {
  .custom-props {
    background-color: var(--bg-color);
    position: fixed;
    margin-left: 8vw;
    height: 100vh;
    width: 16vw;
    font-size: 14px;
  }
}
</style>
