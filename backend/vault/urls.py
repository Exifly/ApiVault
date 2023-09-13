from django.urls import path
from vault.api import (
   TrendingCategoriesView,
   AllCategoryAPIListView,
   CategoryAPIListView,
   RandomAPIListView,
   MyPendingApiView,
   APISearchView,
   APICreateView,
   APIDetailView,
   APICountView,
   APIListView,
   MyApiView
)

urlpatterns = [
   path('detail/<int:pk>', APIDetailView.as_view(), name='api_detail'),

   path('search', APISearchView.as_view(), name='api_search'),
   path('random', RandomAPIListView.as_view()),
   path('create', APICreateView.as_view()),
   path('count', APICountView.as_view()),
   path('all', APIListView.as_view()),

   path('my_api', MyApiView.as_view()),
   path('pending/my_api', MyPendingApiView.as_view()),
   
   path('category/<str:category_name>', CategoryAPIListView.as_view()),
   path('categories/trending', TrendingCategoriesView.as_view()),
   path('categories', AllCategoryAPIListView.as_view()),
]