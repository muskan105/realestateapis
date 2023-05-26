

from django.contrib import admin
from django.urls import include, path
from matrimonial_data import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('ghar',views.GharViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('matrimonial_data.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/',include(router.urls)) 
    
]

