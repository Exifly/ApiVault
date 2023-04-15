<script setup>
import CategoryName from './CategoryName.vue';

defineProps({
    title: {
        type: String,
        required: true,
    },
    body: {
        type: String,
        required: true,
    },
    link: {
        type: String,
        required: true,
    },
    category: {
        type: String,
        required: true,
    }
})
</script>

<template>
    <div class="card card-glass">
        <img src="https://static.vecteezy.com/ti/vettori-gratis/p3/2058317-retro-futuristico-anni-80-sfondo-vettoriale.jpg" class="img-preview-api card-img-top" alt="...">
        <div class="title-showcase">
            {{ title }}
        </div>
        <div class="description-showcase">
            {{ body }}
        </div>
        <div class="category-list">
            <CategoryName 
            :category="category"/>
        </div>
    </div>
</template>

<style scoped>
.card-custom {
    background-color: var(--nav-color);
    border-color: transparent;
    border-radius: 16px;
    color: white;
}

.card-glass {
    backdrop-filter: blur(20px) saturate(172%);
    -webkit-backdrop-filter: blur(20px) saturate(172%);
    background-color: var(--nav-color);
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.125);
    color: white;
}

.img-preview-api {
    border-radius: 16px;
}

.title-showcase {
    margin: 0;
    padding: 24px;
    font-size: 30px;
    line-height: 1;
    color: #ffffff;
}

.description-showcase {
    margin: 0;
    padding: 0 24px 24px;
    font-size: 18px;
    line-height: 1.5;
}
</style>