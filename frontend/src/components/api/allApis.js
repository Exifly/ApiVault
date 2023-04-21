import axios from "axios";

const getAllApi = async () => {
  try {
    return await axios
      .get(`http://192.168.178.20:5001/api/all`)
      .then((res) => res.data);
  } catch (er) {
    console.error(er);
    return false;
  }
};

export default getAllApi;
