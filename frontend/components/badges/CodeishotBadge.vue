<script setup lang="ts"></script>

<template>
    <div class="codeishot__container">
        <a
            class="codeishot_link_container"
            href="https://codeishot.com"
            target="_blank"
        >
            <div class="codeishot__logo_container">
                <span class="codeishot_left_logo">C0DE</span>
                <span class="codeishot_right_logo">ISH0T</span>
                <font-awesome-icon
                    class="codeishot__link_icon"
                    :icon="['fas', 'arrow-up-right-from-square']"
                />
            </div>
            <span class="codeishot__btn">
                <span class="codeishot__btn_text"
                    >Paste, store and share your code</span
                >
            </span></a
        >
    </div>
</template>

<style scoped>
/* Border
#434c57
Primary
#1c242e
Secondary
#313a46 */
a {
    color: inherit;
    text-decoration: none;
}

a:hover {
    color: white;
    text-decoration: none;
}

.codeishot__container {
    display: flex;
    width: 100%;
}

.codeishot_link_container {
    border: 1px solid #434c57;
    border-radius: 8px;
    background: #1c242e;
    color: #fff;
    display: flex;
    flex-direction: column;
    heigth: 54px;
    gap: 6px;
    width: 100%;
    padding: 10px;
}
.codeishot__btn {
    text-align: left;
    appearance: none;
    display: flex;
    padding-left: 2px;
    padding-top: 3px;
    padding-bottom: 3px;
}
.codeishot__link_icon {
    align-self: center;
    margin-left: auto;
    color: rgb(200, 200, 200);
}
.codeishot__btn_text {
    font-family: Menlo, Monaco, Consolas, "Liberation Mono", "Courier New",
        monospace;
    font-size: 14px;
}
.codeishot__logo_container {
    display: flex;
    flex-direction: row;
    justify-content: start;
    gap: 3px;
}

.codeishot_left_logo {
    font-family: Menlo, Monaco, Consolas, "Liberation Mono", "Courier New",
        monospace;
    font-size: 1rem;
    font-weight: 700;
    line-height: 1.5rem;
}

.codeishot_right_logo {
    border-radius: 0.375rem;
    background-image: linear-gradient(
        to bottom left,
        #0d9488,
        #0891b2,
        #2563eb
    );
    padding-left: 0.25rem;
    padding-right: 0.25rem;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas,
        "Liberation Mono", "Courier New", monospace;
    font-size: 1rem;
    font-weight: 700;
    color: #ffffff;
    box-shadow:
        0 1px 3px 0 rgba(0, 0, 0, 0.1),
        0 1px 2px 0 rgba(0, 0, 0, 0.06);
}
</style>
