from django.db import models

from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200)
    placeId = models.SlugField(max_length=200, unique=True)
    description_short = models.TextField()
    description_long = HTMLField()
    lng = models.FloatField()
    lat = models.FloatField()
    objects = models.Manager()

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField()
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.image.name

    class Meta:
        ordering = ['order']
