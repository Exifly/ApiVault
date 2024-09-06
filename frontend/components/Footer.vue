<template>
    <footer
        class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4"
    >
        <p class="col-md-4 mb-0 text-wrapper-no-hover">
            2024 &copy; Exifly
            <br />
            Coded by those
            <NuxtLink
                class="text-wrapper-authors"
                style="text-decoration: none; font-weight: 600"
                to="/contributors"
            >
                wonderful people
            </NuxtLink>
        </p>

        <NuxtLink
            to="/"
            class="col-md-4 d-flex align-items-center justify-content-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none"
        >
            <img :src="logoMode" alt="" width="30" height="30" />
        </NuxtLink>

        <ul class="nav col-md-4 justify-content-end">
            <li class="nav-item">
                <a
                    id="emailSupport"
                    title="Send us an Email"
                    tabindex="3"
                    href="mailto:info@exifly.it"
                    class="nav-link px-2 text-wrapper"
                    target="_blank"
                    >{{ packageJson.version }}</a
                >
            </li>
            <li class="nav-item">
                <a
                    id="githubRepository"
                    title="Check out our github repository"
                    tabindex="4"
                    href="https://github.com/Exifly/ApiVault"
                    class="nav-link px-2 text-wrapper"
                    target="_blank"
                    ><font-awesome-icon :icon="['fab', 'github']"
                /></a>
            </li>
            <li class="nav-item">
                <a
                    title="Send us an Email"
                    tabindex="5"
                    href="mailto:info@exifly.it"
                    class="nav-link px-2 text-wrapper"
                    target="_blank"
                    >Contact</a
                >
            </li>
            <li class="nav-item">
                <a
                    title="Sponsor APIVault"
                    tabindex="6"
                    href="https://ko-fi.com/apivault"
                    class="nav-link px-2 text-wrapper"
                    target="_blank"
                    >Sponsor</a
                >
            </li>
            <li class="nav-item">
                <NuxtLink
                    title="Apivault Cookie Policy"
                    tabindex="7"
                    to="/cookie-policy"
                    class="nav-link px-2 text-wrapper"
                    >Cookie Policy</NuxtLink
                >
            </li>
            <li class="nav-item">
                <NuxtLink
                    title="Apivault Privacy Policy"
                    tabindex="8"
                    to="/privacy-policy"
                    class="nav-link px-2 text-wrapper"
                    >Privacy Policy</NuxtLink
                >
            </li>
        </ul>
    </footer>
</template>

<script setup lang="ts">
import packageJson from '../package.json'

const theme = useState('APIVaultTheme', () =>
    process.client ? localStorage.getItem('APIVaultTheme')! : 'dark'
)

const logoMode = computed(() => {
    if (theme!.value === 'dark' || theme.value === null) {
        return '/img/apivault-dark-nobg.png'
    }
    return '/img/apivault-light-nobg.png'
})
</script>

<style scoped>
.text-wrapper {
    color: var(--text-color);
}

.text-wrapper:hover {
    color: var(--text-color-hover);
}

.text-wrapper-no-hover {
    color: var(--text-color);
}

.text-wrapper-authors {
    color: rgb(3, 155, 178);
}

.text-wrapper-authors:hover {
    color: rgb(0, 201, 232);
}
</style>
