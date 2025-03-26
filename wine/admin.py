from django.contrib import admin
from .models import Listing, Colour, Country

admin.site.register(Colour)
admin.site.register(Country)


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = (
        "name", "wine_colour", "country", "taste_profile", "is_public",
    )
    list_filter = (
        "wine_colour__name", "country__name",
    )
