from django.db import models
from django.utils import timezone


class Place(models.Model):
    # author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=13, decimal_places=10)
    lng = models.DecimalField(max_digits=13, decimal_places=10)
    text = models.TextField()
    # created_date = models.DateTimeField(
    #         default=timezone.now)
    # published_date = models.DateTimeField(
    #         blank=True, null=True)

    def __str__(self):
        return self.title


class Trip(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    places = models.ManyToManyField(Place)

    def __str__(self):
        return self.title
