<script setup>
import ContentBody from "@/layouts/ContentBody.vue";
import SearchBar from "@/components/SearchBar.vue";
import Sidebar from "@/components/Sidebar.vue";
import Footer from "@/components/Footer.vue";
import Navbar from "@/components/Navbar.vue";
import BodyFlex from "@/layouts/BodyFlex.vue";
import Card from "@/components/Card.vue";
import Hero from "@/components/Hero.vue";

// const githubRepoApi = "https://api.github.com/repos/exifly/tweetyfly";
</script>

<template>
  <BodyFlex>
    <header>
      <Navbar />
    </header>
    <Sidebar />
    <ContentBody>
      <template #topAreaContent>
        <SearchBar />
      </template>
      <template #heroAreaContent>
        <Hero />
      </template>
      <template #cardAreaContent>
        <Card />
      </template>
      <template #footerArea>
        <Footer />
      </template>
    </ContentBody>
  </BodyFlex>
</template>
