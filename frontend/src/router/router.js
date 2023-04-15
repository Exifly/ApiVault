import { createRouter, createWebHistory } from "vue-router";
import DashboardNew from "@/pages/DashboardNew.vue";
import Categories from "@/pages/categories/[category].vue";

// Defining the routes
const routes = [
  {
    path: "/",
    name: "Dashboard",
    component: DashboardNew,
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
