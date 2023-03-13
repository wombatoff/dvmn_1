from django.views.generic import ListView
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
                    'placeId': '',
                    'detailsUrl': ''
                }
            )
            features.append(feature)
        geojson_data = FeatureCollection(features)
        context['geojson_data'] = geojson_data
        return context
