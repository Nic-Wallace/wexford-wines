from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_wines, name='wines'),
    path('<int:wine_id>/', views.wine_listing, name='wine_listing'),
    path('add/', views.add_listing, name='add_listing'),
    path('edit/<int:wine_id>/', views.edit_listing, name='edit_listing'),
    path('delete/<int:wine_id>/', views.delete_listing, name='delete_listing'),
]
