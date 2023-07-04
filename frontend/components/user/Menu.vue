<template>
  <div class="dropdown">
    <GenericsButton class="font-size-sm" data-bs-toggle="dropdown" aria-expanded="false">
      <img class="img-properties me-2" :src="defaultPic" height="24" width="24">
      {{ username }}
      <font-awesome-icon class="ms-2" :icon="['fas', 'angles-down']" />
    </GenericsButton>
    <ul class="mx-auto dropdown-wrapper-override dropdown-animation dropdown-menu dropdown-menu-dark" style="padding: 10px; width: 100%;">
      <li class="wrapper-hover-effect dropdown-item py-2">
        <p disabled class="m-0 text-header">
          <font-awesome-icon class="me-2" :icon="['fas', 'circle-user']" />
          Profile
        </p>
      </li>
      <li class="py-2">
        <NuxtLink class="ms-0 wrapper-hover-effect dropdown-item" style="text-decoration: none !important;" to="/user/apis">
          <font-awesome-icon class="me-1" :icon="['fas', 'code']" />
          My APIs
        </NuxtLink>
      </li>
      <li class="py-2">
        <a @click.prevent="sendLogoutEvent" class="wrapper-hover-effect dropdown-item" href="#">
          <font-awesome-icon class="me-2" :icon="['fas', 'right-from-bracket']" />
          Logout
        </a>
      </li>
      <hr class="m-1" />
      <li class="py-2 wrapper-hover-effect dropdown-item">
        <p disabled class="m-0 text-header">
          <font-awesome-icon class="me-1" :icon="['fas', 'gears']" />
          Utils
        </p>
      </li>
      <li id="theme-mode" class="d-flex py-2 wrapper-hover-effect dropdown-item">
        <p class="py-2 m-0 text-wrapper">
          <font-awesome-icon class="me-2" :icon="['fas', 'moon']" />
          Dark mode
        </p>
        <GenericsToggle :checked="isChecked" @click.prevent="setModeLocal" style="transform: scale(0.8); margin-top: 4px"/>
      </li>
    </ul>
  </div>
</template>

<script lang="ts" setup>
import ApivaultServices from "~/services/ApivaultServices";
import {
  getThemeElements,
  themeIcons,
  setThemeLogoPath,
  setLocalStorage,
} from "../../utils/themeutils";

const defaultPic = ref<string>("/img/user/user-default-img.png");
let { username } = defineProps({
  username: {
    type: String,
    required: true,
  }
})

const isChecked = ref(true);

/* Theme data definition */
const theme = useTheme();
const iconTheme = ref(themeIcons[theme.value]);
const logoPath = ref(setThemeLogoPath(theme));

let defaultTheme = ref<boolean>(true);
const setModeLocal = (): void => {
  isChecked.value = !isChecked.value;
  if (process.client) {
    setLocalStorage(theme);
    defaultTheme.value = getThemeElements(theme);
  }
  iconTheme.value = themeIcons[theme.value];
  logoPath.value = setThemeLogoPath(theme);
};

const emit = defineEmits(['event:sign_out']);
const sendLogoutEvent = () => {
  emit('event:sign_out');
}

useHead({
  htmlAttrs: {
    class: computed(() => {
      return defaultTheme.value ? "" : "light"
    }),
  },
})

const accessToken = useCookie("accessToken");
onMounted(async () => {
  let userInfo = await ApivaultServices.userInfo(accessToken.value!);
  defaultPic.value = userInfo.picture;

  if (process.client) {
    document.querySelector('.dropdown').addEventListener('click', function(event) {
      event.stopPropagation();
    });
  }
})

</script>

<style scoped>
.dropdown-wrapper-override {
  background: var(--bg-card-glass);
  font-size: 15px !important;
}

.dropdown-animation {
  animation: fadeIn 0.2s !important;
  transition: all 0.2s linear ease-in-out !important;
}

.img-properties {
  border-radius: 100%;
}

.wrapper-hover-effect {
  color: var(--text-color-hover);
}

.wrapper-hover-effect:hover {
  background: none;
  color: var(--text-color) !important;
}

.text-header {
  color: grey;
}

#theme-mode {
  align-items: center;
  justify-content: space-between;
}

@media only screen and (max-width: 680px) {
  .font-size-sm {
    font-size: 14px !important;
  }
  .dropdown-wrapper-override {
    width: 30%;
  }
}
</style>
