from django.contrib import admin
from .models import Listing, Colour, Country

# Register your models here.
admin.site.register(Listing)
admin.site.register(Colour)
admin.site.register(Country)

# do i need to implement this line?
# @admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = (
        "name", "colour", "country", "taste_profile", "is_public",
    )
    list_filter = (
        "colour__name", "country__name",
    )
