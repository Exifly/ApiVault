import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "@/pages/Dashboard.vue";
import Categories from "@/pages/categories/[category].vue";
import Error404View from "@/pages/errors/Error404View.vue";
import Error500View from "@/pages/errors/Error500View.vue";
import ContributorsView from "@/pages/ContributorsView.vue";

// Defining the routes
const routes = [
  {
    path: "/",
    name: "Dashboard",
    component: Dashboard,
  },
  {
    path: "/contributors",
    name: "Contributors",
    component: ContributorsView,
  },
  {
    path: "/categories/:category",
    name: "Category",
    component: Categories,
  },
  // errors
  {
    path: "/error404",
    name: "ErrorNotFound",
    component: Error404View,
  },
  {
    path: "/error500",
    name: "Error",
    component: Error500View,
  },
];

// Creating the router object
const router = createRouter({
  history: createWebHistory(),
  routes: routes,
});

export default router;
