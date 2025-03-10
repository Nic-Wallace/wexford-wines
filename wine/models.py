from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Colour(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Countries'


class Listing(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    wine_colour = models.ForeignKey(Colour, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    taste_profile = models.TextField(max_length=1000, null=False, blank=False)
    image = CloudinaryField("image", default="placeholder")
    is_public = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
