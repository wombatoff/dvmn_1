from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInLine(admin.TabularInline):
    model = Image
    list_display = ('id', 'place', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="200"/>')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'placeId',
        'description_short',
        'description_long',
        'lng',
        'lat',
    )
    inlines = [ImageInLine, ]
    empty_value_display = '-пусто-'


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'place',
        'order',
        'image',
    )

    empty_value_display = '-пусто-'
