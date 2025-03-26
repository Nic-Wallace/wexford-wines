from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Listing, Colour, Country

# Create your views here.


def all_wines(request):
    """ View to return the wine listings """

    wines = Listing.objects.all()
    colours = Colour.objects.all()
    countries = Country.objects.all()
    query = None
    colours = None
    countries = None

    if request.GET:
        if 'colour' in request.GET:
            colours = request.GET['colour'].split(',')
            wines = wines.filter(wine_colour__name__in=colours)
            colours = Colour.objects.filter(name__in=colours)

        if 'country' in request.GET:
            countries = request.GET['country'].split(',')
            wines = wines.filter(country__name__in=countries)
            countries = Country.objects.filter(name__in=countries)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter search term")
                return redirect(reverse('wines'))
            
            if query.lower() in ("rose", "rosé"):
                # Search for both "rose" and "rosé" in multiple fields
                queries = (
                    Q(name__icontains="rose") | Q(name__icontains="rosé") |
                    Q(wine_colour__name__icontains="rose") | Q(wine_colour__name__icontains="rosé") |
                    Q(country__name__icontains="rose") | Q(country__name__icontains="rosé")
                )
            else:
                queries = (
                    Q(name__icontains=query) |
                    Q(wine_colour__name__icontains=query) |
                    Q(country__name__icontains=query)
                )
            wines = wines.filter(queries)

    context = {
        'wines': wines,
        'search_term': query,
        'current_colours': colours,
        'current_countries': countries
    }

    return render(request, 'wine/wine.html', context)


def wine_listing(request, product_id):
    """ View to return a singular wine listing """

    wine = get_object_or_404(Listing, pk=product_id)

    context = {
        'wine': wine,
    }

    return render(request, 'wine/wine_listing.html', context)
