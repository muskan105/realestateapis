from operator import index
from django.contrib import admin
from django.urls import include, path
from matrimonial_data import views
from . import views
urlpatterns = [
   
    path('realestate', views.index),
 
    path('realestate/search=<str:search_query>/', views.index, name='realestate'),
    path('realestate/search/id=<str:search_query>/', views.index, name='realestate'),
    #path('realestate/search/<str:id>/', index, name='realestate'),
    #path('home/id=<int:id>/', views.index, name='realestate'),
    #path('home/search=<str:search_query>&id=<int:id>/', views.index, name='realestate_with_query_and_id'),
]
