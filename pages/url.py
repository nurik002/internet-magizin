from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from pages.views import HomeTemplateView, ContactCreateView, AboutTemplateView, WishlistListView, add_to_wishlist, \
    search_expenses

app_name = 'pages'
urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('search-expenses/', search_expenses, name='search-expenses'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('wishlist-products/', WishlistListView.as_view(), name='wishlist'),
    path('wishlist-products/<int:pk>', add_to_wishlist, name='add-wishlist'),
    path('', HomeTemplateView.as_view(), name='home')
]
