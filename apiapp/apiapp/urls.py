
from django.contrib import admin
from django.urls import include, path
from matrimonial_data import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('matrimonial_data.urls')),
   
]