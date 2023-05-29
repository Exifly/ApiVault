<template>
  <div class="custom-props mobile-first border-right" id="sidebar-wrapper">
    <div class="scrollbox">
      <div class="sidebar-heading ms-4">MENU</div>
      <ul class="list-unstyled ps-0 text-black mx-4">
        <li class="sidebar-text-wrapper mt-2 category-custom">
          <router-link class="flex items-center gap-2 px-2" to="/">
            <font-awesome-icon
              class=""
              width="12"
              height="12"
              icon="fa-solid fa-house"
            />Home</router-link
          >
        </li>
        <li class="sidebar-text-wrapper mt-2 category-custom">
          <a
            class="flex items-center gap-2 px-2"
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
        <li class="sidebar-text-wrapper mt-2 category-custom">
          <a
            class="flex items-center gap-2 px-2"
            style="text-decoration: none"
            href="https://www.buymeacoffee.com/exifly"
          >
            <font-awesome-icon
              class=""
              width="12"
              height="12"
              icon="fa-solid fa-hand-holding-dollar"
            />Sponsor</a
          >
        </li>
        <li class="sidebar-text-wrapper mt-2 category-custom">
          <router-link
            class="flex items-center gap-2 px-2"
            style="text-decoration: none"
            to="/contributors"
          >
            <font-awesome-icon
              class=""
              width="12"
              height="12"
              icon="fa-solid fa-users"
            />Contributors</router-link
          >
        </li>
      </ul>
      <div class="sidebar-heading ms-4">CATEGORIES</div>
      <div class="list-group list-group-flush">
        <ul class="list-unstyled ps-0 text-black mx-4">
          <li
            class="sidebar-text-wrapper mt-2 category-custom"
            v-for="category in categoriesAttributes"
            :key="category"
          >
            <router-link
              class="flex items-center gap-2 px-2"
              :to="'/categories/' + category.name"
            >
              <font-awesome-icon
                class=""
                width="12"
                height="12"
                :icon="category.icon"
              />{{ category.name }}</router-link
            >
          </li>
          <hr />
          <li class="sidebar-heading">INFO</li>
          <li
            class="sidebar-text-wrapper sidebar-info-text mt-2 category-custom"
          >
            API Fetched: <b>{{ api.count }}</b>
          </li>
          <li
            class="sidebar-text-wrapper sidebar-info-text mt-2 category-custom"
          >
            <!-- N. Categories: <b>{{ categoriesAttributes.length }}</b> -->
            N. Categories: <b>{{ categoriesAttributes.length }}</b>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, onMounted } from "vue";
import { categoriesProperties } from "~/utils/categoryMapping";
import ApivaultServices from "~/services/ApivaultServices";

const categoriesAttributes = categoriesProperties;
const api = reactive({
  count: 0,
});

onMounted(async () => {
  api.count = await ApivaultServices.countApis();
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
