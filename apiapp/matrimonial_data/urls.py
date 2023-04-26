from django.contrib import admin
from django.urls import include, path
from matrimonial_data import views

urlpatterns = [
    path('home', views.index),
]