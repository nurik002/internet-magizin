from django import template
from django.db.models import Sum

from products.models import ProductModel

register = template.Library()


@register.simple_tag
def get_lang_url(request, lang):
    url = request.path.split('/')
    url[1] = lang

    return '/'.join(url)


@register.simple_tag
def get_price(request, x):
    price = request.GET.get('price')
    if price:
        return price.split(';')[x]
    return 'null'


@register.filter
def in_cart(product, request):
    return product.pk in request.session.get('cart', [])


@register.simple_tag
def count_cart_products(request):
    return len(request.session.get('cart', []))


@register.simple_tag
def sum_cart_products(request):
    cart = request.session.get('cart', [])
    if not cart:
        return 0
    return ProductModel.get_from_cart(request).aggregate(Sum('real_price')).get('real_price__sum', 0)


@register.filter
def len_cart(request):
    return len(request)
