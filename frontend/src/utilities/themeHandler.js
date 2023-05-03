export function getTheme() {
  const theme = localStorage.getItem("APIVaultTheme");
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)");

  if (theme !== "dark" && theme !== "light") {
    if (prefersDark) {
      localStorage.setItem("APIVaultTheme", "dark");
    } else {
      localStorage.setItem("APIVaultTheme", "light");
    }
  }

  return localStorage.getItem("APIVaultTheme");
}
