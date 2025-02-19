from django.shortcuts import render

# Create your views here.

def index(request):
    """ View to return the homepage """
    return render(request, 'homepage/templates/index.html')