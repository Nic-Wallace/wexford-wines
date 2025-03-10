from django.shortcuts import render
from .models import Listing

# Create your views here.

def all_wines(request):
    """ View to return the wine listings """

    wine = Listing.objects.all()

    context = {
        'wine': wine,
    }

    return render(request, 'wine/wine.html', context)