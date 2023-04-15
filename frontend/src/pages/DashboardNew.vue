<script setup>
import Card from "@/newComponents/Card.vue";
import Footer from "@/newComponents/Footer.vue";
import Navbar from "../newComponents/Navbar.vue";
import Hero from "../newComponents/Hero.vue";
import SearchBar from "../components/SearchBar.vue";
import Sidebar from "../newComponents/Sidebar.vue";

// const githubRepoApi = "https://api.github.com/repos/exifly/tweetyfly";
</script>

<template>
  <div class="flex-parent">
    <header>
      <Navbar />
    </header>
    <Sidebar />
    <div class="flex-adjust container p-4">
      <div class="hero container">
        <div class="row">
          <div class="col-12 col-lg-12 col-md-12">
            <Hero />
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-12 mb-5">
          <SearchBar />
        </div>
      </div>
      <h1 class="text-wrapper">ALL</h1>
      <div class="row">
        <div class="col-12 col-lg-4 col-md-6 mb-4 mb-md-4">
          <Card />
        </div>
        <div class="col-12 col-lg-4 col-md-6 mb-4 mb-md-4">
          <Card />
        </div>
        <div class="col-12 col-lg-4 col-md-6 mb-4 mb-md-4">
          <Card />
        </div>
        <div class="col-12 col-lg-4 col-md-6 mb-4 mb-md-4">
          <Card />
        </div>
      </div>
      <div class="container mt-5">
        <hr />
        <Footer />
      </div>
    </div>
  </div>
</template>

<style scoped>
hr {
  border-color: var(--hr-color);
}
.flex-parent {
  display: flex;
  flex-direction: row;
  flex-grow: 0;
}

.flex-child {
  flex-direction: column;
  flex-grow: 1;
  top: 25%;
  left: 25%;
}

.flex-adjust {
  margin-left: 22vw;
  margin-top: 7vw;
}

.sidebar {
  width: 25vw;
}

.body-wrap {
  left: 25%;
}

@media only screen and (max-width: 600px) {
  .mobile-first {
    display: none;
  }
  .flex-adjust {
    margin-left: 0vw;
    margin-top: 8vh;
  }
}

@media (min-width: 1581px) {
  .flex-adjust {
    margin-left: 26vw;
    margin-top: 7vw;
  }
}
</style>
