import axios from "axios";

const endpoint = import.meta.env.VITE_API_VAULT_ENDPOINT;
const trendCategories = async () => {
  try {
    return await axios
      .get(`${endpoint}/api/categories/trending`)
      .then((res) => res.data);
  } catch (er) {
    console.error(er);
    return false;
  }
};

export default trendCategories;
