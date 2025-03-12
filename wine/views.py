from django.shortcuts import render, get_object_or_404
from .models import Listing

# Create your views here.


def all_wines(request):
    """ View to return the wine listings """

    wines = Listing.objects.all()

    context = {
        'wines': wines,
    }

    return render(request, 'wine/wine.html', context)


def wine_listing(request, product_id):
    """ View to return a singular wine listing """

    wine = get_object_or_404(Wine, pk=product_id)

    context = {
        'wine': wine,
    }

    return render(request, 'wine/wine_listing.html', context)
