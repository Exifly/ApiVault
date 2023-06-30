<template>
  <div class="dropdown">
    <GenericsButton class="font-size-sm" data-bs-toggle="dropdown" aria-expanded="false">
      <img class="img-properties me-2" :src="profilePic" height="24" width="24">
      {{ username }}
      <font-awesome-icon class="ms-2" :icon="['fas', 'angles-down']" />
    </GenericsButton>
    <ul class="dropdown-wrapper-override dropdown-animation dropdown-menu dropdown-menu-dark">
      <li>
        <NuxtLink class="wrapper-hover-effect dropdown-item" style="text-decoration: none !important;" to="/favourites">
          <font-awesome-icon class="me-2" :icon="['fas', 'bookmark']" />
          My bookmarks
        </NuxtLink>
      </li>
      <hr class="m-1" />
      <li><a @click.prevent="sendLogoutEvent" class="wrapper-hover-effect dropdown-item" href="#">
        <font-awesome-icon class="me-2" :icon="['fas', 'right-from-bracket']" />
        Logout
      </a></li>
    </ul>
  </div>
</template>

<script lang="ts" setup>
const defaultPic = "/img/user/user-default-img.png";

let { username } = defineProps({
  username: {
    type: String,
    required: true,
  },
  profilePic: {
    type: String,
    required: false,
    default: defaultPic, 
  }
})

const emit = defineEmits(['event:sign_out']);
const sendLogoutEvent = () => {
  emit('event:sign_out');
}

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

@media only screen and (max-width: 680px) {
  .font-size-sm {
    font-size: 14px !important;
  }
  .dropdown-wrapper-override {
    width: 30%;
  }
}
</style>
