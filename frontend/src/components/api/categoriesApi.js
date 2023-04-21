import axios from "axios";

const getApiData = async (category) => {
  try {
    return await axios
      .get(`http://localhost:5001/api/all?categorie=${category}`)
      .then((res) => res.data);
  } catch (er) {
    console.error(er);
    return false;
  }
};

export default getApiData;
