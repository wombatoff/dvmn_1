from adminsortable2.admin import SortableAdminMixin, SortableAdminBase, SortableStackedInline
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInLine(SortableStackedInline):
    model = Image
    readonly_fields = ('image_preview',)
    ordering = ('order',)
    list_display = (
        'order',
        'place',
        'image_preview',
    )

    def image_preview(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="200"/>')


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
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
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = (
        'place',
        'image_preview',
        'order',
        'image',
    )
    empty_value_display = '-пусто-'
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="200"/>')
