from django.utils.html import format_html


def image_preview(obj):
    return format_html('<img src="{}" width="200"/>', obj.image.url)
