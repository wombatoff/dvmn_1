from django.utils.html import format_html


def image_preview(place_image):
    return format_html('<img src="{}" height ="200"/>', place_image.image.url)
