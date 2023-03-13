from django.contrib import admin

from .models import Place


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

