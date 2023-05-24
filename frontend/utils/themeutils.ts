export function getTheme(): string {
  const theme = localStorage.getItem("APIVaultTheme");
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)");
  if (process.client) {
    if (theme !== "dark" && theme !== "light") {
      if (prefersDark.matches) {
        localStorage.setItem("APIVaultTheme", "dark");
      } else {
        localStorage.setItem("APIVaultTheme", "light");
      }
    }
  }
    return localStorage.getItem("APIVaultTheme")!;
}

export const themeIcons: { [key: string]: string } = {
  light: "fa-solid fa-sun",
  dark: "fa-solid fa-moon",
};

export const setThemeElements = (theme: globalThis.Ref<string>): void => {
  if (theme.value === null) {
    document.querySelector("body")?.setAttribute("data-theme", "dark");  
  }
  document.querySelector("body")?.setAttribute("data-theme", theme.value);
}

export const setThemeLogoPath = (theme: globalThis.Ref<string>): string => {
  return `/img/apivault-full-${theme.value}-nobg.png`;
}

/**
This code generates a string that represents the mode of the theme,
either "Light Mode" or "Dark Mode", depending on the theme.value
*/
export const setIconThemeText = (theme: globalThis.Ref<string>): string => {
  return theme.value
    ? theme.value[0].toUpperCase() +
        theme.value.slice(1, theme.value.length) +
        " Mode"
    : " Mode"
}

export const setLocalStorage = (theme: globalThis.Ref<string>): void => {
  if (theme.value === "dark" || theme.value === undefined) {
    theme.value = "light";
    localStorage.setItem("APIVaultTheme", "light");
  } else {
    theme.value = "dark";
    localStorage.setItem("APIVaultTheme", "dark");
  }
}