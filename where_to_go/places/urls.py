from django.urls import path

from .views import PlaceListView, PlaceDetailView

urlpatterns = [
    path('', PlaceListView.as_view(), name='index'),
    path('<int:pk>/', PlaceDetailView.as_view(), name='place'),
]
