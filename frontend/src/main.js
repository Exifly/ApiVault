import { createApp, ref } from "vue";
import "./style.css";
import App from "./App.vue";

// bootstrap import
import "bootstrap/dist/css/bootstrap.css";
import bootstrap from "bootstrap/dist/js/bootstrap.bundle.js";

// firebase
import firebase from "firebase";

// fontawesome
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import {
  faAnglesRight,
  faAt,
  faBagShopping,
  faBars,
  faBitcoinSign,
  faBook,
  faBrain,
  faBuildingColumns,
  faCalendar,
  faCalendarCheck,
  faCameraRetro,
  faCheck,
  faCircleUser,
  faCloud,
  faCode,
  faCoins,
  faCube,
  faDatabase,
  faDumbbell,
  faEarthEurope,
  faFilm,
  faGamepad,
  faHandHoldingDollar,
  faHouse,
  faHouseLaptop,
  faIdCard,
  faListOl,
  faListUl,
  faMagnifyingGlass,
  faMobile,
  faMoneyBill,
  faMoneyBillTrendUp,
  faMoon,
  faMusic,
  faNewspaper,
  faNotesMedical,
  faPaintBrush,
  faPaw,
  faPeopleArrows,
  faPizzaSlice,
  faRobot,
  faSeedling,
  faShieldHalved,
  faSpellCheck,
  faSquareCheck,
  faSun,
  faTerminal,
  faUnlockKeyhole,
  faUserSecret,
  faVirusSlash,
  faWrench,
  faCar,
  faVideo,
  faMagnifyingGlassChart,
  faSitemap,
  faShuttleSpace,
  faChartGantt,
  faCloudSunRain,
  fas,
  faB,
} from "@fortawesome/free-solid-svg-icons";
import {
  faFaceLaugh,
  faFlag,
  faFolderOpen,
} from "@fortawesome/free-regular-svg-icons";
import {
  faEthereum,
  faGitAlt,
  faGithub,
  faGithubAlt,
  faGithubSquare,
} from "@fortawesome/free-brands-svg-icons";

import router from "./router/router";
import { categoriesProperties } from "@/utilities/categoryMapping.js";

library.add(
  fas,
  faB,
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
  faBars,
  faPaw,
  faFilm,
  faVirusSlash,
  faPaintBrush,
  faUnlockKeyhole,
  faBitcoinSign,
  faBook,
  faMoneyBill,
  faCalendar,
  faCloud,
  faWrench,
  faEthereum,
  faMoneyBillTrendUp,
  faSquareCheck,
  faCode,
  faSpellCheck,
  faFolderOpen,
  faAt,
  faFaceLaugh,
  faSeedling,
  faCalendarCheck,
  faCoins,
  faPizzaSlice,
  faGamepad,
  faEarthEurope,
  faBuildingColumns,
  faNotesMedical,
  faHouseLaptop,
  faRobot,
  faMusic,
  faNewspaper,
  faDatabase,
  faGithubAlt,
  faIdCard,
  faCircleUser,
  faMobile,
  faCameraRetro,
  faTerminal,
  faBrain,
  faShieldHalved,
  faBagShopping,
  faPeopleArrows,
  faDumbbell,
  faCube,
  faMagnifyingGlassChart,
  faChartGantt,
  faShuttleSpace,
  faSitemap,
  faCar,
  faVideo,
  faCloudSunRain,
  faCheck,
  faHouse,
  faHandHoldingDollar,
  faListOl
);

// firebase config
const firebaseConfig = {
  apiKey: import.meta.env.VITE_FIREBASE_APIKEY,
  authDomain: import.meta.env.VITE_FIREBASE_AUTHDOMAIN,
  projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID,
  storageBucket: import.meta.env.VITE_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: import.meta.env.VITE_FIREBASE_MSG_SENDER_ID,
  appId: import.meta.env.VITE_FIREBASE_APP_ID,
  measurementId: import.meta.env.VITE_FIREBASE_MEASURE_ID,
};

// global variables
const colorScheme = ref("dark");
firebase.initializeApp(firebaseConfig);
createApp(App)
  .use(router)
  .use(bootstrap)
  .provide("categoryMapping", categoriesProperties)
  .provide("colorScheme", colorScheme)
  .component("font-awesome-icon", FontAwesomeIcon)
  .mount("#app");
