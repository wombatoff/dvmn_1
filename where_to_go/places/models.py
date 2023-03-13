from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    order = models.IntegerField()

    def __str__(self):
        return self.image.name

    class Meta:
        ordering = ['order']
