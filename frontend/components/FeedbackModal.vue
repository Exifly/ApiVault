<template>
  <div
    class="modal fade"
    id="feedbackModal"
    tabindex="-1"
    aria-labelledby="feedbackModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="custom-border-radius glass-card modal-content">
        <div class="py-0 custom-border modal-header">
          <h1
            v-if="!successSubmit"
            class="ps-2 text-wrapper modal-title fs-5"
            id="feedbackModalLabel"
          >
            FEEDBACK
          </h1>
          <h1
            v-else
            class="ps-2 text-wrapper modal-title fs-5"
            id="feedbackModalLabel"
          >
            Feedback Submitted
          </h1>
          <GenericsButton
            @click.prevent="restoreSuccessState"
            class="mobile-wrapper-btn m-0 mt-3 me-2"
            data-bs-dismiss="modal"
            aria-label="Close"
          >
            <font-awesome-icon :icon="['fas', 'xmark']" />
          </GenericsButton>
        </div>
        <div v-if="!notAuth" class="modal-body p-4 pt-2">
          <div v-if="successSubmit">
            <AnimationSuccessCheckmark />
          </div>
          <form v-else>
            <div class="mb-3">
              <div class="mobile-wrapper-section align-items-center">
                <label
                  for="recipient-name"
                  class="text-wrapper modal-title-head col-form-label"
                  >Name: (Optional)</label
                >
                <input
                  v-model="name"
                  type="text"
                  placeholder="Your name"
                  class="inverted-input-box text-wrapper form-control"
                  id="recipient-name"
                />
              </div>
              <div class="mb-3 mt-4">
                <label
                  for="message-text"
                  class="text-wrapper modal-title-head col-form-label"
                  >Email: (Optional)</label
                >
                <input
                  v-model="email"
                  type="text"
                  placeholder="Your email"
                  class="px-3 inverted-input-box text-wrapper form-select"
                  aria-label="Select corse state"
                />
              </div>
            </div>
            <div class="mb-3 mt-4">
              <label
                for="message-text"
                class="text-wrapper modal-title-head col-form-label"
                >Message: *</label
              >
              <textarea
                rows="10"
                placeholder="Your message.."
                v-model="description"
                class="text-wrapper inverted-input-box form-control"
                id="message-text"
              />
            </div>
          </form>
          <p v-if="!isValidInput" class="m-0 mt-3 error-validation">
            Some fields are empty!!
          </p>
        </div>
        <div v-else class="modal-body p-4 pt-2">
          <h3 class="text-wrapper">Please login to submit a Feed</h3>
        </div>
        <div v-if="!notAuth" class="px-4 custom-border modal-footer">
          <p
            v-if="!successSubmit"
            class="text-wrapper"
            style="margin-right: auto; opacity: 70%"
          >
            Fields with * are mandatory!
          </p>
          <p
            v-else
            class="text-wrapper"
            style="margin-right: auto; opacity: 70%"
          >
            Thanks for giving us your feed!
          </p>
          <NuxtLink to="/">
            <GenericsButton
              v-if="successSubmit"
              @click="restoreSuccessState"
              class="mobile-wrapper-footer-btn m-1"
              data-bs-dismiss="modal"
              >Home</GenericsButton
            >
          </NuxtLink>
          <GenericsButton
            @click.prevent="restoreSuccessState"
            class="mobile-wrapper-footer-btn m-1"
            data-bs-dismiss="modal"
            >Close</GenericsButton
          >
          <GenericsButton
            class="mobile-werapper-footer-btn2"
            v-if="!successSubmit"
            style="position: relative"
            @click.prevent="validateInput"
            :isInverted="true"
            :class="['text-wrapper-inverted dm-1', { tremor: !isValidInput }]"
            >Submit</GenericsButton
          >
        </div>
        <div v-else class="px-4 custom-border modal-footer">
          <GenericsButton
            @click.prevent="restoreSuccessState"
            class="mobile-wrapper-footer-btn m-1"
            data-bs-dismiss="modal"
            >Close</GenericsButton
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import ApivaultServices from "~/services/ApivaultServices";
import { Category } from "~/models/types";

const accessToken = useCookie("accessToken");
const name = ref<string>("");
const description = ref<string>("");
const email = ref<string>("");
const successSubmit = ref<boolean>(false);
const notAuth = ref<boolean>(false);

const isValidInput = ref<boolean>(true);
const shakeAnimationState = ref<boolean>(false);
const validateInput = async () => {
  if (name.value === "" || description.value === "" || email.value === "") {
    isValidInput.value = false;
    setTimeout(() => {
      isValidInput.value = true;
      shakeAnimationState.value = true;
    }, 4000);
    return;
  }
  // TODO: handle error codes
  let statuscode = await ApivaultServices.submitFeedback(
    accessToken.value!,
    name.value,
    email.value,
    description.value
  );
  successSubmit.value = true;
};

const restoreSuccessState = () => {
  setTimeout(() => {
    successSubmit.value = false;
  }, 1000);
};

const categories = ref<Category[]>();
onMounted(async () => {
  if (accessToken.value === "" || accessToken.value === null)
    notAuth.value = true;
  categories.value = await ApivaultServices.categories();
});
</script>

<style scoped>
.modal-title-head {
  color: #aeaeae !important;
  font-size: 14px !important;
}
.inverted-input-box {
  background: var(--bg-trending-category);
  border: hidden;
}

.custom-border {
  border: hidden;
}

.custom-border-radius {
  border-radius: 8px;
}

#space-between-form {
  justify-content: space-between;
}

.align-dividers {
  align-self: end;
  margin-bottom: 9px;
}

.error-validation {
  color: red;
}

.tremor {
  animation: shake-animation 4.2s linear;
}

@keyframes shake-animation {
  0% {
    transform: translate(0, 0);
  }
  1.78571% {
    transform: translate(5px, 0);
  }
  3.57143% {
    transform: translate(0, 0);
  }
  5.35714% {
    transform: translate(5px, 0);
  }
  7.14286% {
    transform: translate(0, 0);
  }
  8.92857% {
    transform: translate(5px, 0);
  }
  10.71429% {
    transform: translate(0, 0);
  }
  100% {
    transform: translate(0, 0);
  }
}

@media (max-width: 480px) {
  .mobile-wrapper-btn {
    width: 13%;
  }
  .mobile-wrapper-section {
    width: 100%;
  }
  .mobile-wrapper-footer-btn {
    font-size: small;
    width: 30%;
  }
  .mobile-werapper-footer-btn2 {
    font-size: small;
  }
}
</style>
