from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Listing

# Create your views here.


def all_wines(request):
    """ View to return the wine listings """

    wines = Listing.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter search term")
                return redirect(reverse('wines'))
            
            queries = Q(name__icontains=query)
            wines = wines.filter(queries)

    context = {
        'wines': wines,
        'search_term': query,
    }

    return render(request, 'wine/wine.html', context)


def wine_listing(request, product_id):
    """ View to return a singular wine listing """

    wine = get_object_or_404(Listing, pk=product_id)

    context = {
        'wine': wine,
    }

    return render(request, 'wine/wine_listing.html', context)
