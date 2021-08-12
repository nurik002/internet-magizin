from django.urls import path
from django.views.decorators.cache import cache_page

from products.views import ListListView, ProductDetailView, CommentCreateView, add_cart, CartListView

app_name = 'shop'
urlpatterns = [
    path('', cache_page(60)(ListListView.as_view()), name='products'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('add_to_card/<int:pk>', add_cart, name='add_cart'),
    path('product-commment/<int:pk>', CommentCreateView.as_view(), name='product-comment'),
    path('card', CartListView.as_view(), name='card'),
]
