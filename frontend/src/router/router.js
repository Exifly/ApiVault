import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "@/pages/Dashboard.vue";
import Categories from "@/pages/categories/[category].vue";

// Defining the routes
const routes = [
  {
    path: "/",
    name: "Dashboard",
    component: Dashboard,
  },
  {
    path: "/categories/:category",
    name: "Category",
    component: Categories,
  },
];

// Creating the router object
const router = createRouter({
  history: createWebHistory(),
  routes: routes,
});

export default router;
