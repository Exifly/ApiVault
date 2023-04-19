<script setup>
import { reactive, inject } from "vue";

const categoriesAttributes = inject("categoryMapping");
</script>

<template>
  <div class="custom-props mobile-first border-right" id="sidebar-wrapper">
    <div class="scrollbox">
      <div class="sidebar-heading ms-4">MENU</div>
      <ul class="list-unstyled ps-0 text-black mx-4">
        <li class="sidebar-text-wrapper mt-2 category-custom">
          <router-link class="sidebar-text-wrapper" to="/">
            <font-awesome-icon
              class="mx-2"
              width="12"
              height="12"
              icon="fa-solid fa-house"
            />Home</router-link
          >
        </li>
        <li class="sidebar-text-wrapper mt-2 category-custom">
          <font-awesome-icon
            class="mx-2"
            width="12"
            height="12"
            :icon="['fab', 'github']"
          />Repository
        </li>
        <li class="sidebar-text-wrapper mt-2 category-custom">
          <font-awesome-icon
            class="mx-2"
            width="12"
            height="12"
            icon="fa-solid fa-hand-holding-dollar"
          />Sponsor
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
              class="sidebar-text-wrapper"
              :to="'/categories/' + category.name"
            >
              <font-awesome-icon
                class="mx-2"
                width="12"
                height="12"
                :icon="category.icon"
              />{{ category.name }}</router-link
            >
          </li>
          <hr />
          <li class="sidebar-heading">INFO</li>
          <li class="sidebar-text-wrapper mt-2 category-custom">
            API Fetched: <b>1542</b>
          </li>
          <li class="sidebar-text-wrapper mt-2 category-custom">
            N. Categories: <b>{{ categoriesAttributes.length }}</b>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

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
  margin-top: 8vh;
  height: 100vh;
  width: 20vw;
  font-size: 14px;
}

.category-custom:hover {
  color: rgb(166, 166, 166);
}

.sidebar-text-wrapper {
  color: var(--text-color) !important;
  text-decoration: none;
}

.sidebar-text-wrapper:hover {
  color: var(--text-color-hover) !important;
}

.sidebar-heading {
  color: var(--text-color-hover);
  font-size: 18px;
  font-weight: 600;
}

.search-bar {
  margin-top: 5vh;
  margin-bottom: 5vh;
}

@media (min-width: 1581px) and (min-width: 1800px) {
  .custom-props {
    background-color: var(--bg-color);
    position: fixed;
    margin-top: 8vh;
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
    margin-top: 8vh;
    margin-left: 8vw;
    height: 100vh;
    width: 16vw;
    font-size: 14px;
  }
}
</style>
