from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.throttling import UserRateThrottle
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from apivault.mixins import ApiFilterMixin
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import generics
from django.db.models import Count
from rest_framework import status
from django.db.models import Q
from vault.serializers import(
   APICreateSerializer,
   CategoryCountSerializer,
   CategorySerializer,
   APISerializer
)

from random import sample
from vault.models import (
    APIPending,
    Category,
    API
)

class APICreateView(generics.CreateAPIView):
   permission_classes = [permissions.IsAuthenticated]
   serializer_class = APICreateSerializer

   def perform_create(self, serializer):
      serializer.save(owner=self.request.user)


class RandomAPIListView(generics.ListAPIView):
   """
   API view that returns 9 random APIs.
   """
   serializer_class = APISerializer
   throttle_classes = [UserRateThrottle]

   def get_queryset(self):
      """
      API view that returns 9 random APIs.
      """
      return sample(list(API.objects.all()), 9)
   


# @method_decorator(cache_page(86400), name='get')
class APIListView(generics.ListAPIView):
   """
   List all APIs.
   """
   throttle_classes = [UserRateThrottle]
   queryset = API.objects.all()
   serializer_class = APISerializer



@method_decorator(cache_page(86400), name='get')
class TrendingCategoriesView(generics.ListAPIView):
   """
   API view that returns the top 10 categories by API count.
   """
   serializer_class = CategoryCountSerializer
   throttle_classes = [UserRateThrottle]

   def get_queryset(self):
         """
         Returns the top 10 categories by API count.
         """
         return Category.objects.annotate(api_count=Count('api')).order_by('-api_count')[:10]
   


class CategoryAPIListView(ApiFilterMixin, generics.ListAPIView):
   """
   API view that returns the APIs based on the category.
   """
   serializer_class = APISerializer
   throttle_classes = [UserRateThrottle]
   allowed_order_field = ['name', '-likes_count']

   def get_queryset(self):
      category_name = self.kwargs['category_name']
      category = Category.objects.get(name=category_name)
      queryset = API.objects.filter(category=category)
      return self.apply_ordering(queryset)
   

@method_decorator(cache_page(864000), name='get')
class AllCategoryAPIListView(generics.ListAPIView):
   """
   List all Categories.
   """
   throttle_classes = [UserRateThrottle]
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
    

class APICountView(APIView):
    """
    API view that returns the count of API objects in the database.
    """
    throttle_classes = [UserRateThrottle]
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
   throttle_classes = [UserRateThrottle]
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
   

class APISearchView(generics.ListAPIView):
   """
   API view for searching APIs by name and description.
   """
   serializer_class = APISerializer
   throttle_classes = [UserRateThrottle]


   def get_queryset(self):
      query = self.request.query_params.get('query', '')

      return API.objects.filter(
         Q(name__icontains=query) |
         Q(description__icontains=query) |
         Q(category__name__icontains=query)
      )

   
class MyApiView(APIView):
   """
   Retrieve the approved APIs of the logged user.
   """
   permission_classes = [permissions.IsAuthenticated]
   throttle_classes = [UserRateThrottle]

   def get(self, request):
      apis = API.objects.filter(owner=request.user)
      serializer = APISerializer(apis, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
   

class MyPendingApiView(APIView):
   """
   Retrieve the pending APIs of the logged user.
   """
   permission_classes = [permissions.IsAuthenticated]
   throttle_classes = [UserRateThrottle]

   def get(self, request):
      apis = APIPending.objects.filter(owner=request.user)
      serializer = APISerializer(apis, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
   

