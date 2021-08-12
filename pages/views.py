import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, ListView

from pages.forms import ContactFormsModel
from pages.models import InteriorModel, BannerModel, TeamModel
from posts.models import PostModel
from products.models import ProductModel


class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactFormsModel

    def form_valid(self, form):
        name = form.cleaned_data['name']
        form.save()
        return JsonResponse({'name': name}, status=200)

    def form_invalid(self, form):
        return JsonResponse({'errors': form.errors}, status=404)

    def get_success_url(self):
        return reverse('pages:contact')


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = ProductModel.objects.order_by('-pk')[:6]
        context['posts'] = PostModel.objects.order_by('-pk')[:3]
        context['interior'] = InteriorModel.objects.all()
        context['banner'] = BannerModel.objects.all()
        return context


class AboutTemplateView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = TeamModel.objects.all()
        return context


class WishlistListView(LoginRequiredMixin, ListView):
    template_name = 'wishlist.html'
    context_object_name = 'products'

    def get_queryset(self):
        return self.request.user.wishlist.all()


@login_required
def add_to_wishlist(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    user = request.user
    if user in product.wishlist.all():
        product.wishlist.remove(user)
    else:
        product.wishlist.add(user)

    return redirect(request.GET.get('next', '/'))


def search_expenses(request):
    # if request.method == 'POST':
    search_str = request.GET.get('q')
    expenses = ProductModel.objects.filter(
        Q(title__icontains=search_str) |
        Q(type__title__icontains=search_str) |
        Q(materials__title__icontains=search_str) |
        Q(description__icontains=search_str))
    data = expenses.values()
    return JsonResponse(list(data), safe=False)
