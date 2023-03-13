from django.contrib import admin

from .models import Place, Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description_short',
        'description_long',
        'lng',
        'lat',
    )

    empty_value_display = '-пусто-'


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'place',
        'order',
        'image',
    )

    empty_value_display = '-пусто-'
