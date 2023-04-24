import axios from "axios";

const endpoint = import.meta.env.VITE_API_VAULT_ENDPOINT;
const getApiData = async () => {
  try {
    return await axios.get(`${endpoint}/api/random`).then((res) => res.data);
  } catch (er) {
    console.error(er);
    return false;
  }
};

export default getApiData;
