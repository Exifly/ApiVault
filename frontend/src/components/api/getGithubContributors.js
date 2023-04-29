import axios from "axios";

const endpoint = "https://api.github.com/repos/exifly/apivault/contributors";
const getContributors = async () => {
  try {
    return await axios.get(endpoint).then((res) => res.data);
  } catch (er) {
    console.error(er);
    return false;
  }
};

export default getContributors;
