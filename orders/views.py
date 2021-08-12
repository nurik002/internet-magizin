from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from orders.form import OrderFormModel
from products.models import ProductModel


class OrderCreateView(LoginRequiredMixin, CreateView):
    template_name = 'checkout-2.html'
    form_class = OrderFormModel
    success_url = reverse_lazy('orders:order-history')

    def form_valid(self, form):
        products = ProductModel.get_from_cart(self.request)
        form.instance.user = self.request.user
        form.instance.price = ProductModel.get_from_cart(self.request).aggregate(Sum('real_price'))['real_price__sum']
        order = form.save()
        order.product.set(products)

        self.request.session['cart'] = []

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = ProductModel.get_from_cart(self.request)
        context['profile'] = self.request.user.profile
        return context


class HistoryListView(LoginRequiredMixin, ListView):
    template_name = 'history.html'

    def get_queryset(self):
        return self.request.user.orders.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        return context
