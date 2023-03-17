from adminsortable2.admin import SortableAdminMixin, SortableAdminBase, SortableStackedInline
from django.contrib import admin

from .models import Place, Image
from .admin_image_utils import image_preview


class ImageInLine(SortableStackedInline):
    model = Image
    readonly_fields = ('image_preview',)
    ordering = ('order',)
    list_display = (
        'order',
        'place',
        'image_preview',
    )
    image_preview = staticmethod(image_preview)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = (
        'title',
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
    image_preview = staticmethod(image_preview)