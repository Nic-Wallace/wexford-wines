from django.shortcuts import render, redirect, reverse, \
                            HttpResponse, get_object_or_404
from django.contrib import messages
from wine.models import Listing


def cart_view(request):
    """ View to return the shopping cart """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified wine to the cart """

    wine = Listing.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated quantity of {wine.name} in cart')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {wine.name} to cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust the quantity of a wine """

    wine = Listing.objects.get(pk=item_id)
    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated quantity of {wine.name} in cart')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {wine.name} from cart')

    request.session["cart"] = cart
    return redirect(reverse("cart_view"))


def remove_from_cart(request, item_id):
    """ Remove the wine from the shopping cart """

    wine = get_object_or_404(Listing, pk=item_id)
    cart = request.session.get("cart", {})

    try:
        cart.pop(item_id)
        messages.success(request, f'Removed {wine.name} from cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(f"Error removing wine: {e}")
        return HttpResponse(status=500)
