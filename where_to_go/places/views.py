from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from geojson import Feature, FeatureCollection, Point

from .models import Place


class PlaceListView(ListView):
    model = Place
    template_name = 'index.html'
    context_object_name = 'places'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        places = self.get_queryset()
        features = []
        for place in places:
            feature = Feature(
                geometry=Point((place.lng, place.lat)),
                properties={
                    'title': place.title,
                    'placeId': place.pk,
                    'detailsUrl': reverse('place', args=(place.pk,)),
                }
            )
            features.append(feature)
        geojson_data = FeatureCollection(features)
        context['geojson_data'] = geojson_data
        return context


class PlaceDetailView(DetailView):
    model = Place

    def get(self, request, *args, **kwargs):
        place = get_object_or_404(Place, pk=kwargs['pk'])
        response_data = {
            'title': place.title,
            'imgs': [image.image.url for image in place.images.all()],
            'description_short': place.description_short,
            'description_long': place.description_long,
        }
        return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})
