export function setTheme(): string {
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

export const getThemeElements = (theme: globalThis.Ref<string>): boolean => {
  return theme.value === null || theme.value === 'dark';
}

export const setThemeLogoPath = (theme: globalThis.Ref<string>): string => {
  if (theme.value === null || theme.value === undefined) {
    return `/img/apivault-full-dark-nobg.png`;
  }
  return `/img/apivault-full-${theme.value}-nobg.png`;
}

export const setLocalStorage = (theme: globalThis.Ref<string>): boolean => {
  if (theme.value === "dark" || theme.value === undefined) {
    theme.value = "light";
    localStorage.setItem("APIVaultTheme", "light");
    return false;
  } else {
    theme.value = "dark";
    localStorage.setItem("APIVaultTheme", "dark");
    return true;
  }
}