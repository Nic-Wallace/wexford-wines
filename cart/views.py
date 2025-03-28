from django.shortcuts import render, redirect, reverse, HttpResponse
from wine.models import Listing


def cart_view(request):
    """ View to return the shopping cart """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified wine to the cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust the quantity of a wine """

    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session["cart"] = cart
    return redirect(reverse("cart_view"))


# def remove_from_cart(request, item_id):
#     """ Remove the item from the shopping cart """

#     cart = request.session.get("cart", {})
#     cart.pop(item_id)

#     request.session["cart"] = cart
#     return HttpResponse(status=200)



def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    wine = get_object_or_404(Listing, pk=item_id)
    try:
        size = None
        if 'wine_size' in request.POST:
            size = request.POST['wine_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]["items_by_size"][size]
            if not cart[item_id]["items_by_size"]:
                cart.pop(item_id)
        else:
            cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(f"Error removing item: {e}")
        return HttpResponse(status=500)
