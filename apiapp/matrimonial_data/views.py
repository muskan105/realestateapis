from django.shortcuts import render,HttpResponse
from matrimonial_data import mongodb
from django.http import HttpRequest, JsonResponse
from . models import Ghar
from django.db.models import Q
# import folium

# Create your views here.
def index(request, search_query=None):
    if not search_query:
        query_params = request.GET
        search_query = query_params.get('search', None)

    ghars = Ghar.objects.all()
    if search_query:
          
        ghars = ghars.filter(Q(name__icontains=search_query) | Q(price__icontains=search_query) | Q(id__icontains=search_query))

    return JsonResponse({"data":[x for x in ghars.values()]})
    # locations = []
    # for ghar in ghars:
    #     locations.append({
    #         'lat': ghar.latitude,
    #         'lng': ghar.longitude,
            
    #     })

    # # create a map object and add a tile layer
    # map = folium.Map(location=[27.7172, 85.3240], zoom_start=12)
    # folium.TileLayer('cartodbpositron').add_to(map)

    # # add markers for each location
    # for loc in locations:
    #     folium.Marker(location=[loc['lat'], loc['lng']],
    #                   popup=f"<strong>{loc['name']}</strong><br>Price: {loc['price']}"
    #                  ).add_to(map)

    # # get the map as HTML and return it as a response
    # map_html = map.get_root().render()
    # return render(request, 'index.html', {'map_html': map_html})
    # # return JsonResponse({"data":[x for x in ghars.values()]})
    




    