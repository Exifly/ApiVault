from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.db.models import Count

from vault.serializers import(
    CategorySerializer,
    APISerializer
)
from random import sample
from vault.models import (
   Category,
   API
)


class RandomAPIListView(generics.ListAPIView):
   """
   API view that returns 9 random APIs.
   """
   serializer_class = APISerializer

   def get_queryset(self):
      """
      API view that returns 9 random APIs.
      """
      return sample(list(API.objects.all()), 9)
   


@method_decorator(cache_page(86400), name='get')
class APIListView(generics.ListAPIView):
   """
   List all APIs.
   """
   queryset = API.objects.all()
   serializer_class = APISerializer



@method_decorator(cache_page(86400), name='get')
class TrendingCategoriesView(generics.ListAPIView):
   """
   API view that returns the top 10 categories by API count.
   """
   serializer_class = CategorySerializer

   def get_queryset(self):
         """
         Returns the top 10 categories by API count.
         """
         return Category.objects.annotate(api_count=Count('api')).order_by('-api_count')[:10]
   


class CategoryAPIListView(generics.ListAPIView):
   """
   API view that returns the APIs based on the category.
   """
   serializer_class = APISerializer

   def get_queryset(self):
      category_name = self.kwargs['category_name']
      category = Category.objects.get(name=category_name)
      return API.objects.filter(category=category)
    


class APICountView(APIView):
    """
    API view that returns the count of API objects in the database.
    """
    def get(self, request):
        """
        Handle GET request and return the count of API objects.

        Returns:
            Response: Response object containing the count of API objects.
        """
        api_count = API.objects.count()
        return Response({"api_count": api_count})



class APIDetailView(RetrieveAPIView):
   """
   Retrieve details of a single API.
   """
   queryset = API.objects.all()
   serializer_class = APISerializer

   def get_object(self):
      """
      Returns the object the view is displaying.
      Also, increments the API's view counter each time the API is retrieved.
      """
      api = super().get_object()
      api.view_count += 1
      api.save()
      return api
   


