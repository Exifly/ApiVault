import re

class Search:

   @staticmethod
   def matches_query(text, query):
      """
      Check if the given text contains the query as a substring (case-insensitive).

      :param text: The text to search within.
      :param query: The query to search for.
      :return: True if the query is found in the text, False otherwise.
      """
      return bool(re.search(query, text, re.IGNORECASE))
   
   
   @staticmethod
   def search_entries(data_entries, query, category=None):
      """
      Filter the given data entries based on the search query and an optional category.

      :param data_entries: A list of data entries to filter.
      :param query: The search query to use for filtering.
      :param category: An optional category to filter by (default: None).
      :return: A list of filtered data entries.
      """
      query_lower = query.lower()
      filtered_results = []

      for entry in data_entries:
         if Search.matches_query(entry['API'], query_lower) or Search.matches_query(entry['Description'], query_lower):
               if category is None or Search.matches_query(entry['Category'], category.lower()):
                  filtered_results.append(entry)

      return filtered_results