import axios from "axios";

const endpoint = import.meta.env.VITE_API_VAULT_ENDPOINT;

const getAllApi = async () => {
  try {
    return await axios.get(`${endpoint}/api/all`).then((res) => res.data);
  } catch (er) {
    console.error(er);
    return false;
  }
};

export default getAllApi;
