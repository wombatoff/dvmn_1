from io import BytesIO

import requests
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand

from ...models import Place, Image


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("json_url", type=str, help="URL of the JSON file")

    def handle(self, *args, **options):
        json_url = options["json_url"]
        response = requests.get(json_url)
        response.raise_for_status()

        data = response.json()

        place = Place(
            title=data["title"],
            description_short=data["description_short"],
            description_long=data["description_long"],
            lng=data["coordinates"]["lng"],
            lat=data["coordinates"]["lat"],
        )
        place.save()

        for order, image_url in enumerate(data["imgs"], start=1):
            image_response = requests.get(image_url)
            image_response.raise_for_status()

            image_file_name = image_url.split("/")[-1]
            image_file = ImageFile(BytesIO(image_response.content), name=image_file_name)

            image = Image(
                place=place,
                image=image_file,
                order=order,
            )
            image.save()

        self.stdout.write(self.style.SUCCESS(f"Successfully loaded data from {json_url}"))
