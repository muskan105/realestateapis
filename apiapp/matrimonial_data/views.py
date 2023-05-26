
from django.shortcuts import render,HttpResponse
from matrimonial_data import mongodb
from django.http import HttpRequest, JsonResponse
from . models import Ghar
from django.db.models import Q

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from matrimonial_data.serializers import GharSerializer
from .filters import GharFilter
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics,viewsets,filters
from .mongodb import getData


# Create your views here.
def index(request):
   getData()
   return JsonResponse({'heloo':'hey'})
  
class GharViewSet(viewsets.ModelViewSet):
    queryset = Ghar.objects.all()
    serializer_class = GharSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        'bhk': ['contains'],
        'price_amount': ['gte', 'lte']
    }
    search_fields = ['price_amount', 'place']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        
        # Get the search_query from the request query parameters
        search_query = self.request.query_params.get('search', None)
        
        # If the search_query is not None, store it in the user's session
        if search_query is not None:
            request.session['search_query'] = search_query
        
        # Try to get the search_query from the user's session
        search_query = request.session.get('search_query', None)
        print(search_query)
        
        # If the search_query is not None, filter the queryset using it
        if search_query is not None:
            queryset = queryset.filter(Q(place__icontains=search_query) | Q(price_amount__icontains=search_query))
       
        filtered_queryset = self.filter_queryset(queryset)

        serializer = self.get_serializer(filtered_queryset, many=True)
        return Response(serializer.data)