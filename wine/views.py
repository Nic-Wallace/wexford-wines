from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Listing, Colour, Country
from .forms import WineForm


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
                    Q(wine_colour__name__icontains="rose") | Q(wine_colour__name__icontains="rosé") |  # noqa
                    Q(country__name__icontains="rose") | Q(country__name__icontains="rosé")  # noqa
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


def wine_listing(request, wine_id):
    """ View to return a singular wine listing """

    wine = get_object_or_404(Listing, pk=wine_id)

    context = {
        'wine': wine,
    }

    return render(request, 'wine/wine_listing.html', context)


@login_required
def add_listing(request):
    """ Add a listing to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('homepage'))

    if request.method == 'POST':
        form = WineForm(request.POST, request.FILES)
        if form.is_valid():
            wine = form.save()
            messages.success(request, 'Added the wine listing!')
            return redirect(reverse('wine_listing', args=[wine.id]))
        else:
            messages.error(
                request,
                'Failed to add wine listing. Please check the form is valid.')
    else:
        form = WineForm()

    template = 'wine/add_listing.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_listing(request, wine_id):
    """ Edit a wine listing """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('homepage'))

    wine = get_object_or_404(Listing, pk=wine_id)
    if request.method == 'POST':
        form = WineForm(request.POST, request.FILES, instance=wine)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated wine listing!')
            return redirect(reverse('wine_listing', args=[wine.id]))
        else:
            messages.error(
                request,
                'Failed to update listing. Please ensure the form is valid.')
    else:
        form = WineForm(instance=wine)
        messages.info(request, f'You are editing {wine.name}')

    template = 'wine/edit_listing.html'
    context = {
        'form': form,
        'wine': wine,
    }

    return render(request, template, context)


@login_required
def delete_listing(request, wine_id):
    """ Delete a wine listing """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('homepage'))

    wine = get_object_or_404(Listing, pk=wine_id)
    wine.delete()
    messages.success(request, 'Wine listing deleted!')
    return redirect(reverse('wines'))
