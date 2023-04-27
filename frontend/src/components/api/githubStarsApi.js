import axios from "axios";

const getStars = async () => {
  try {
    return await axios
      .get("https://api.github.com/repos/exifly/ApiVault")
      .then((res) => res.data);
  } catch (er) {
    console.error(er);
    return false;
  }
};

export default getStars;
