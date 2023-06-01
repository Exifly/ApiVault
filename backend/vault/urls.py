from django.urls import path
from vault.api import (
   TrendingCategoriesView,
   CategoryAPIListView,
   RandomAPIListView,
   APIDetailView,
   APICountView,
   APIListView
)

urlpatterns = [
   path('detail/<int:pk>/', APIDetailView.as_view(), name='api_detail'),

   path('random/', RandomAPIListView.as_view()),
   path('count/', APICountView.as_view()),
   path('all/', APIListView.as_view()),


   path('category/<str:category_name>/', CategoryAPIListView.as_view()),
   path('categories/trending/', TrendingCategoriesView.as_view()),
]