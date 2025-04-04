from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "No wines in the cart")
        return redirect(reverse('wines'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51RAAgd09wTvQ7mf0NR4h4H8TVscbtc3ZvFbygJlI6Luom8nf9uJmDgcji4HHYTolj66sVFjuUiqSgQoaYbx0offr00HQBaQVRk',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
