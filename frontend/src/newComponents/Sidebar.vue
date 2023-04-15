<script setup>
const categories = [
  "Animals",
  "Anime",
  "Anti-Malware",
  "Art & Design",
  "Authentication & Authorization",
  "Blockchain",
  "Books",
  "Business",
  "Calendar",
  "Cloud Storage & File Sharing",
  "Continuous Integration",
  "Cryptocurrency",
  "Currency Exchange",
  "Data Validation",
  "Development",
  "Dictionaries",
  "Documents & Productivity",
  "Email",
  "Entertainment",
  "Environment",
  "Events",
  "Finance",
  "Food & Drink",
  "Games & Comics",
  "Geocoding",
  "Government",
  "Health",
  "Jobs",
  "Machine Learning",
  "Music",
  "News",
  "Open Data",
  "Open Source Projects",
  "Patent",
  "Personality",
  "Phone",
  "Photography",
  "Programming",
  "Science & Math",
  "Security",
  "Shopping",
  "Social",
  "Sports & Fitness",
  "Test Data",
  "Text Analysis",
  "Tracking",
  "Transportation",
  "URL Shorteners",
  "Vehicle",
  "Video",
  "Weather",
];
</script>

<template>
  <div class="custom-props mobile-first border-right" id="sidebar-wrapper">
    <div class="scrollbox">
      <div class="sidebar-heading ms-4">YOU LIKE</div>
      <ul class="list-unstyled ps-0 text-black mx-4">
        <li class="sidebar-text-wrapper mt-2 category-custom">Pippo</li>
        <li class="sidebar-text-wrapper mt-2 category-custom">Pluto</li>
        <li class="sidebar-text-wrapper mt-2 category-custom">Topolino</li>
      </ul>
      <div class="sidebar-heading ms-4">CATEGORIES</div>
      <div class="list-group list-group-flush">
        <ul class="list-unstyled ps-0 text-black mx-4">
          <li
            class="sidebar-text-wrapper mt-2 category-custom"
            v-for="category in categories"
            :key="category"
          >
            <router-link
              class="sidebar-text-wrapper"
              :to="'/categories/' + category"
              >{{ category }}</router-link
            >
          </li>
          <hr />
          <li class="sidebar-heading">INFO</li>
          <li class="sidebar-text-wrapper mt-2 category-custom">
            API Fetched: <b>1542</b>
          </li>
          <li class="sidebar-text-wrapper mt-2 category-custom">
            N. Categories: <b>{{ categories.length }}</b>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>
::-webkit-scrollbar {
  width: 5px;
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
  width: 23vw;
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
</style>
