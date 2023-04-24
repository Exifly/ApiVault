import axios from "axios";

const endpoint = import.meta.env.VITE_API_VAULT_ENDPOINT;
const apiCount = async () => {
  try {
    return await axios.get(`${endpoint}/api/count`).then((res) => res.data);
  } catch (er) {
    console.error(er);
    return false;
  }
};

export default apiCount;
