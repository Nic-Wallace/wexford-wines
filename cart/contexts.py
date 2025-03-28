from django.shortcuts import get_object_or_404
from wine.models import Listing

def cart_contents(request):

    cart_items = []
    total = 0
    wine_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        wine = get_object_or_404(Listing, pk=item_id)
        total += quantity * wine.price
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'wine': wine,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'wine_count': wine_count,
    }

    return context
