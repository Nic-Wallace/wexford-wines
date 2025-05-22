from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterForm


def newsletter(request):
    """
    newsletter view
    """
    form = NewsletterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscribed to newsletter!')
            return redirect('homepage')
        else:
            messages.error(request, 'ERROR, please try again.')
    template = 'newsletter/newsletter.html'
    context = {
        'form': form,
        'on_profile_page': True,
    }
    return render(request, template, context)
