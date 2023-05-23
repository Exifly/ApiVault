import { APIType } from "~/models/types";

export const handleSearch = (
  val: any, 
  title: any,
  apiData: Ref<APIType[]>,
  apiSearched: Ref<APIType[]>,
  categorySearched: any,
  categoryTitle: string,
  showList: Ref<boolean>) => {
  if (title === undefined) {
    categorySearched.category = categoryTitle;
    apiSearched.value = apiData.value;
    showList.value = true;
  } else if (val.length > 0) {
    categorySearched.category = title.value.toUpperCase();
    apiSearched.value = val;
    showList.value = true;
  } else {
    categorySearched.category = "NO MATCH";
    apiSearched.value = apiData.value;
    showList.value = false;
  }
};
