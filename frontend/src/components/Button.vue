<script setup>

defineProps({
    value: {
        type: String,
        required: true
    }
})
</script>

<template>
    <button class="btn btn-custom mx-3" value="{{ value }}">{{ value }}</button>
</template>

<style scoped>
.btn-custom {
    background-color: var(--nav-color);
    border-radius: 8px;
    color: white;
    height: 6vh;
    margin-bottom: 3vh;
}
</style>