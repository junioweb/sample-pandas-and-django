from django.db import models
from django.core.validators import MaxValueValidator


class Country(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Wine(models.Model):
    description = models.TextField()
    designation = models.CharField(max_length=255, blank=True)
    province = models.CharField(max_length=255, blank=True)
    region_1 = models.CharField(max_length=60, blank=True)
    region_2 = models.CharField(max_length=60, blank=True)
    variety = models.CharField(max_length=60, blank=True)
    winery = models.CharField(max_length=60)
    price = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    title = models.CharField(max_length=60)
    taster_name = models.CharField(max_length=60, blank=True)
    taster_twitter_handle = models.CharField(max_length=30, blank=True)
    points = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
