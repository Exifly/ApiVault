<template>
  <nav class="glass-nav navbar-custom navbar navbar-expand-lg fixed-top">
    <div class="container-fluid">
      <NuxtLink
        to="/"
        class="navbar-text-wrapper navbar-brand"
        title="Go back to the Homepage"
      >
        <img :src="logoPath" alt="logo" width="150" />
      </NuxtLink>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span>
          <font-awesome-icon
            icon="fa-solid fa-bars"
            style="color: var(--text-color)"
        /></span>
      </button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
        <ul class="navbar-nav align-items-center" role="tablist">
          <li class="mobile-wrapper navbar-text-wrapper ms-2 mt-2" role="tab" style="padding-bottom: 7px;">
            <GenericsButton class="text-wrapper-inverted" :isInverted="true" data-bs-toggle="modal" data-bs-target="#submitApiModal">
                <font-awesome-icon class="me-2" :icon="['fas', 'folder-plus']" /> Submit API
            </GenericsButton>
          </li>
          <li
            style="padding: 0;"
            class="no-margin navbar-text-wrapper ms-2 mt-2"
            role="tab"
          >
            <GoogleSignInButton
              style="margin: 0 !important;"
              v-if="!isLogged"
              @success="handleLoginSuccess"
              @error="handleLoginError"
              :auto-select="false"
              theme="filled_black"
              size="large"
              text="signin"
              locale="en"
              shape="square"
            ></GoogleSignInButton>
            <UserMenu 
              @event:sign_out="() => logout()"
              v-if="isLogged"
             :username="user"
            />
          </li>
          <hr />
          <div id="scrollb" class="scrollbox">
            <div class="d-block d-sm-none">
              <h5 class="navbar-text-wrapper navbar-header-wrapper">MENU</h5>
              <li
                class="nav-item navbar-text-wrapper mt-2 category-custom"
                role="tab"
              >
                <NuxtLink
                  class="navbar-text-wrapper flex items-center gap-2"
                  to="/"
                >
                  <font-awesome-icon
                    class=""
                    width="12"
                    height="12"
                    icon="fa-solid fa-house"
                  />Home</NuxtLink
                >
              </li>
              <li
                class="nav-item navbar-text-wrapper mt-2 category-custom"
                role="tab"
              >
                <a
                  title="check out our github repository"
                  class="navbar-text-wrapper flex items-center gap-2"
                  style="text-decoration: none"
                  href="https://github.com/Exifly/ApiVault"
                >
                  <font-awesome-icon
                    class=""
                    width="12"
                    height="12"
                    :icon="['fab', 'github']"
                  />Repository</a
                >
              </li>
              <li
                class="nav-item navbar-text-wrapper mt-2 category-custom"
                role="tab"
              >
                <a
                  title="Sponsor APIVault"
                  class="navbar-text-wrapper flex items-center gap-2"
                  style="text-decoration: none"
                  href="https://ko-fi.com/apivault"
                >
                  <font-awesome-icon
                    class=""
                    width="12"
                    height="12"
                    icon="fa-solid fa-hand-holding-dollar"
                  />Sponsor</a
                >
              </li>
              <li
                class="nav-item navbar-text-wrapper mt-2 category-custom"
                role="tab"
              >
                <NuxtLink
                  title="Our Contributors"
                  class="navbar-text-wrapper flex items-center gap-2"
                  to="/contributors"
                >
                  <font-awesome-icon
                    class=""
                    width="12"
                    height="12"
                    icon="fa-solid fa-users"
                  />Contributors</NuxtLink
                >
              </li>
              <hr />
              <h5 class="navbar-text-wrapper navbar-header-wrapper">
                CATEGORIES
              </h5>
              <li
                class="nav-item navbar-text-wrapper mt-2 category-custom"
                role="tab"
                v-for="category in categoriesProperties"
                :key="category.name"
              >
                <NuxtLink
                  :title="`${category.name} APIs`"
                  class="navbar-text-wrapper flex items-center gap-2"
                  :to="`/categories/${category.name}`"
                >
                  <font-awesome-icon
                    class=""
                    width="12"
                    height="12"
                    :icon="category.icon"
                  />{{ category.name }}</NuxtLink
                >
              </li>
            </div>
          </div>
        </ul>
      </div>
    </div>
  </nav>
  <GenericsModal title="Submit your API" />
</template>

<script lang="ts" setup>
import {
  GoogleSignInButton,
  type CredentialResponse,
} from "vue3-google-signin";

import { categoriesProperties } from "../utils/categoryMapping";
import ApivaultServices from "~/services/ApivaultServices";

const router = useRouter();

/* Cookies definition */
const cookie = useCookie("sessionGoogle", {
  maxAge: 60 * 60,
});
const accessTokenCookie = useCookie("accessToken", {
  maxAge: 60 * 60 * 360,
});
const userCookie = useCookie("usernames");

const user = ref();
const isLogged = ref<boolean>(false);

/**
This is needed to set the default theme class for first
visit on the website and to inject google signin api script.
*/
useHead({
  script: [
    {
      async: true,
      src: "https://accounts.google.com/gsi/client",
      defer: true,
    },
  ],
});

/* handle success event */
const handleLoginSuccess = async (response: CredentialResponse) => {
  const { credential } = response;
  isLogged.value = true;
  cookie.value = credential;
  await sendTokenToBackend(cookie.value!);
  router.go(0); // force refresh the page to sync user data correctly
};

/* handle an error event */
const handleLoginError = () => {
  console.error("Login failed");
};

/* reset all cookie value and data used for handling user state */
const logout = () => {
  cookie.value = "";
  isLogged.value = false;
  userCookie.value = "";
  accessTokenCookie.value = "";
  router.go(0);
};

/* checks if cookie.value is not an empty string */
const checkLoggedIn = (): void => {
  isLogged.value = !!accessTokenCookie.value && accessTokenCookie.value !== "";
};

/* wrapper function to override username information */
const setUserInfo = () => {
  user.value = userCookie.value;
};

/* decode the token and send it to django backend */
const sendTokenToBackend = async (token: String) => {
  await ApivaultServices.sendOAuthConfigToDjango(token)
    .then((res) => {
      accessTokenCookie.value = res.tokens.access;
      userCookie.value = res.username;
      setUserInfo();
    })
    .catch((err) => {
      console.error(err);
      isLogged.value = false;
    });
};

onBeforeMount(() => {
  checkLoggedIn();
  user.value = userCookie.value;
});

const theme = useTheme();
const iconTheme = ref();
const logoPath = computed(() => {
  return theme.value === "light" ? "/img/apivault-full-light-nobg.png" : "/img/apivault-full-dark-nobg.png";
});

onMounted(() => {
  iconTheme.value = themeIcons[theme.value];
});
</script>

<style scoped>
::-webkit-scrollbar {
  width: 0px;
}

.scrollbox {
  overflow: scroll;
  height: 0;
}

.navbar-custom {
  margin-left: 10px;
  background-color: var(--bg-color);
}

.navbar-text-wrapper {
  color: var(--text-color) !important;
  text-decoration: none;
  padding: 0.3rem 0.2rem;
  border-radius: 5px;
}

.navbar-text-wrapper-inverted {
  color: var(--bg-color) !important;
  text-decoration: none;
}

.navbar-header-wrapper {
  font-weight: 600;
}

.glass-nav {
  backdrop-filter: blur(16px) saturate(200%);
  -webkit-backdrop-filter: blur(16px) saturate(200%);
  background-color: rgba(var(--bg-color), 0.76);
}

.custom-radius {
  border-radius: var(--border-radius);
}

.custom-props-navbar {
  position: fixed;
  width: 100%;
}

.nav-item:hover {
  cursor: pointer;
  color: var(--nav-item-hover);
  background-color: var(--bg-card-glass-hover);
  border-radius: 5px;
}

@media (min-width: 1025px) and (max-width: 1280px) {
  .navbar-custom {
    height: 8vh;
  }
}

@media (min-width: 1572px) {
  .navbar-custom {
    max-width: calc(100vw - (11.3vw * 2));
    margin: auto;
  }
}

@media only screen and (max-width: 680px) {
  .mobile-wrapper {
    margin-left: 0 !important;
    padding-left: 0;
  }
  .glass-nav {
    background-color: var(--bg-color);
  }
  .scrollbox {
    overflow: scroll;
    height: 73vh !important;
  }
  .align-items-center {
    align-items: normal !important;
  }
}
</style>
