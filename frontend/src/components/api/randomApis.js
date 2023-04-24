import axios from "axios";

const getApiData = async () => {
  try {
    return await axios
      .get("http://0.0.0.0:5001/api/random")
      .then((res) => res.data);
  } catch (er) {
    console.error(er);
    return false;
  }
};

export default getApiData;
