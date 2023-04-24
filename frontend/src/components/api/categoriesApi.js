import axios from "axios";

const endpoint = import.meta.env.VITE_API_VAULT_ENDPOINT;
const getApiData = async (category) => {
  try {
    return await axios
      .get(`${endpoint}/api/all?categorie=${category}`)
      .then((res) => res.data);
  } catch (er) {
    console.error(er);
    return false;
  }
};

export default getApiData;
