import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";

// bootstrap import
import "bootstrap/dist/css/bootstrap.css";
import bootstrap from "bootstrap/dist/js/bootstrap.bundle.js";

// fontawesome
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import {
  faAnglesRight,
  faBars,
  faListUl,
  faMagnifyingGlass,
  faMoon,
  faSun,
  faUserSecret,
} from "@fortawesome/free-solid-svg-icons";
import { faFlag } from "@fortawesome/free-regular-svg-icons";
import {
  faGitAlt,
  faGithub,
  faGithubSquare,
} from "@fortawesome/free-brands-svg-icons";

import router from "./router/router";

library.add(
  faUserSecret,
  faFlag,
  faListUl,
  faGithub,
  faGitAlt,
  faGithubSquare,
  faAnglesRight,
  faSun,
  faMagnifyingGlass,
  faMoon,
  faBars
);

createApp(App)
  .use(router)
  .use(bootstrap)
  .component("font-awesome-icon", FontAwesomeIcon)
  .mount("#app");
