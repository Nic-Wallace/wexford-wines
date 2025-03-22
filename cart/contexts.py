from decimal import Decimal
from django.conf import settings

def cart_contents(request):

    cart_items = []
    total = 0
    wine_count = 0

    context = {
        'cart_items': cart_items,
        'total': total,
        'wine_count': wine_count,
    }

    return context