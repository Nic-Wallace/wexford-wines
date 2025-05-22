from django.shortcuts import render
from .models import FAQ


def faqs(request):
    """
    FAQs view
    """
    faqs = FAQ.objects.all()
    template = 'faqs/faqs.html'
    context = {
        'faqs': faqs,
    }
    return render(request, template, context)
