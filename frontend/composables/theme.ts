export const useTheme = () => {
  return useState("APIVaultTheme", () =>
  process.client ? localStorage.getItem("APIVaultTheme")! : "dark"
)};
