from django.shortcuts import render


def index(request):
    """
    View to return the homepage
    """
    template = 'homepage/index.html'
    context = {
        'on_profile_page': True,
    }
    return render(request, template, context)
