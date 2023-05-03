export function getTheme() {
    const theme = localStorage.getItem("APIVaultTheme");
    const prefersLight = window.matchMedia("(prefers-color-scheme: light)");

    if (theme !== "dark" && theme !== "light") {
        if (prefersLight) {
            localStorage.setItem("APIVaultTheme", "light");
        } else {
            localStorage.setItem("APIVaultTheme", "dark");
        }
    }

    return localStorage.getItem('APIVaultTheme');
}