from math import ceil

from django.db.models import Max, Min

from django.shortcuts import get_object_or_404, redirect

from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView


from products.forms import CommentFormModel
from products.models import ProductModel, ColorModel, TypeModel, MaterialModel


class ListListView(ListView):
    template_name = 'products.html'
    context_object_name = 'products'

    # paginate_by = 4

    def get_queryset(self):
        qs = ProductModel.objects.order_by('-pk')
        color = self.request.GET.get('color')
        type = self.request.GET.get('type')
        sort = self.request.GET.get('sort')
        price = self.request.GET.get('price')
        material = self.request.GET.get('material')
        if color:
            qs = qs.filter(colors__id=color)
        if type:
            qs = qs.filter(type__id=type)
        if material:
            qs = qs.filter(materials__title=material)
        if sort:
            if sort == 'price':
                qs = qs.order_by('real_price')
            if sort == '-price':
                qs = qs.order_by('-real_price')
        if price:
            price = price.split(';')
            price_from, price_to = price
            qs = qs.filter(real_price__gte=price_from, real_price__lte=price_to)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['colors'] = ColorModel.objects.all()
        context['types'] = TypeModel.objects.all()
        context['materials'] = MaterialModel.objects.all()
        max_price, min_price = ProductModel.objects.aggregate(Max('real_price'), Min('real_price')).values()
        context['max_price'] = ceil(max_price)
        context['min_price'] = ceil(min_price)

        return context


class ProductDetailView(DetailView):
    template_name = 'product.html'
    model = ProductModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.object.type.products.exclude(pk=self.object.pk)[:4]
        return context


class CommentCreateView(CreateView):
    form_class = CommentFormModel

    def get_success_url(self):
        return reverse('shop:product-detail', kwargs={'pk': self.kwargs.get('pk')})

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        form.instance.products = get_object_or_404(ProductModel, pk=pk)
        return super().form_valid(form)


class CartListView(ListView):
    template_name = 'checkout-1.html'
    context_object_name = 'products'

    def get_queryset(self):
        return ProductModel.get_from_cart(self.request)


def add_cart(request, pk):
    cart = request.session.get('cart')
    if not cart:
        cart = []
    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)

    request.session['cart'] = cart
    return redirect(request.GET.get('next', '/'))
