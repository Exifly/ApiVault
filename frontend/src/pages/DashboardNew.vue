<script setup>
import Sidebar from "../newComponents/Sidebar.vue";
import Navbar from "../newComponents/Navbar.vue";
import SearchBar from "../components/SearchBar.vue";
import Hero from "../newComponents/Hero.vue";
import CategoryName from "../components/CategoryName.vue";
import Footer from "@/newComponents/Footer.vue";

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
        <div class="col-12 col-lg-4 col-md-6">
          <div class="glass-card card">
            <img
              src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/NGC_4414_%28NASA-med%29.jpg/1200px-NGC_4414_%28NASA-med%29.jpg"
              class="card-img-top"
              alt="..."
              style="border-radius: 12px"
            />
            <div class="card-body">
              <h5 class="text-wrapper card-title">Card title</h5>
              <h6 class="text-wrapper card-subtitle mb-2 text-body-secondary">
                Card subtitle
              </h6>
              <p class="text-wrapper card-text">
                Some quick example text to build on the card title and make up
                the bulk of the card's content.
              </p>
              <CategoryName category="Pippo" />
            </div>
          </div>
        </div>
        <div class="col-12 col-lg-4 col-md-6">
          <div class="glass-card card">
            <img
              src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/NGC_4414_%28NASA-med%29.jpg/1200px-NGC_4414_%28NASA-med%29.jpg"
              class="card-img-top"
              alt="..."
              style="border-radius: 12px"
            />
            <div class="card-body">
              <h5 class="text-wrapper card-title">Card title</h5>
              <p class="text-wrapper card-text">
                Some quick example text to build on the card title and make up
                the bulk of the card's content.
              </p>
              <CategoryName category="Pippo" />
            </div>
          </div>
        </div>
        <div class="col-12 col-lg-4 col-md-6">
          <div class="glass-card card">
            <img
              src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/NGC_4414_%28NASA-med%29.jpg/1200px-NGC_4414_%28NASA-med%29.jpg"
              class="card-img-top"
              alt="..."
              style="border-radius: 12px"
            />
            <div class="card-body">
              <h5 class="text-wrapper card-title">Card title</h5>
              <p class="text-wrapper card-text">
                Some quick example text to build on the card title and make up
                the bulk of the card's content.
              </p>
              <CategoryName category="Pippo" />
            </div>
          </div>
        </div>
        <div class="col-12 col-lg-4 col-md-6 mt-4">
          <div class="glass-card card">
            <img
              src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/NGC_4414_%28NASA-med%29.jpg/1200px-NGC_4414_%28NASA-med%29.jpg"
              class="card-img-top"
              alt="..."
              style="border-radius: 12px"
            />
            <div class="card-body">
              <h5 class="text-wrapper card-title">Card title</h5>
              <p class="text-wrapper card-text">
                Some quick example text to build on the card title and make up
                the bulk of the card's content.
              </p>
              <CategoryName category="Pippo" />
              <CategoryName category="Pippo" />
            </div>
          </div>
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

.glass-card {
  backdrop-filter: blur(16px) saturate(200%);
  -webkit-backdrop-filter: blur(16px) saturate(200%);
  background-color: var(--bg-card-glass);
  /* background-color: rgba(var(--bg-color), 0.78); */
  border-radius: 12px;
  border: 1px solid var(--border-color-cards);
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
