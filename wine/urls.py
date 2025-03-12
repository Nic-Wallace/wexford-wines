from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_wines, name='wine'),
    path('<product_id>', views.wine_listing, name='wine_listing'),
]
