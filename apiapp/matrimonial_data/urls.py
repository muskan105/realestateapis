from operator import index
from django.contrib import admin
from django.urls import include, path
from matrimonial_data import views

from rest_framework import routers
from .views import index
# from django.urls import re_path
urlpatterns = [
   
    path('Ghar', views.index),
    # path('realestate/search/', views.index, name='realestate'),
    # path('realestate/search/id=<str:search_query>/', views.index, name='realestate'),
    # path('ghar/', ghar_list, name='ghar-list'),
    # path('ghar/', views.index, name='ghar-list'),
#    path('ghar/<str:search_query>/', views.index, name='ghar-list-search'),
#     path('realestate/', views.index, name='realestate'),
#      path('realestate/', ghar_list, name='ghar-list'),
    # path('realestate/search=<str:search_query>/ghar/', views.index, name='realestate-ghar'),
    # path('realestate/search=<str:search_query>/ghar/<str:name>/<str:price>/', views.index, name='realestate-ghar-filtered'),
    # path('ghar/', views.ghar_list, name='ghar-list'),
    # re_path(r'^realestate/search=(?P<search_quecry>[\w\s]+)/ghar/(?P<name>[\w\s]+)/(?P<price>[\w\s-]+)/$', views.index, name='realestate-ghar-filtered'),


 



]