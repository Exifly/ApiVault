export function setTheme(): string {
  const theme = localStorage.getItem("APIVaultTheme");
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)");
  
  if (!theme || (theme !== "dark" && theme !== "light")) {
    if (prefersDark.matches) {
      localStorage.setItem("APIVaultTheme", "dark");
      return "dark";
    } else {
      localStorage.setItem("APIVaultTheme", "light");
      return "light";
    }
  }
  
  return theme;
}

export function setThemeValue(color: string): void {
  if (process.client) localStorage.setItem("APIVaultTheme", color);
}

export const themeIcons: { [key: string]: string } = {
  light: "fa-solid fa-sun",
  dark: "fa-solid fa-moon",
};

export const getThemeElements = (theme: globalThis.Ref<string>): boolean => {
  return theme.value === null || theme.value === 'dark';
}

export const setThemeLogoPath = (theme: globalThis.Ref<string>): string => {
  const value = theme.value;
  return value === null || value === undefined ? "/img/apivault-full-dark-nobg.png" : `/img/apivault-full-${value}-nobg.png`;
}


export const setLocalStorage = (theme: globalThis.Ref<string>): boolean => {
  const value = theme.value;
  const newTheme = value === "dark" || value === undefined ? "light" : "dark";
  theme.value = newTheme;
  localStorage.setItem("APIVaultTheme", newTheme);
  return newTheme === "dark";
}
