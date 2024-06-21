from django.shortcuts import render

# Create your views here.

def index(request):
    """ View to return the wines page """
    return render(request, 'wines/index.html')