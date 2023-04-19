import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "@/pages/Dashboard.vue";
import Categories from "@/pages/categories/[category].vue";
import { inject } from "vue";

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
  // errors
  {
    path: "/error404",
    name: "ErrorNotDound",
    component: import("@/pages/errors/Error404View.vue"),
  },
  {
    path: "/error500",
    name: "Error",
    component: import("@/pages/errors/Error500View.vue"),
  },
];

// Creating the router object
const router = createRouter({
  history: createWebHistory(),
  routes: routes,
});

export default router;
