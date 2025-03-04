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
    name = models.CharField(max_length=60, null=False blank=False)
    colour = 
    country = 
    taste_profile = 
    image = 
    is_public = 

