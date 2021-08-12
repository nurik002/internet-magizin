from django.contrib.auth import get_user_model
from django.db import models

from products.models import ProductModel
from django.utils.translation import ugettext_lazy as _

UserModel = get_user_model()


class OrderModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='orders', verbose_name=_('user'))
    product = models.ManyToManyField(ProductModel, related_name='orders', verbose_name=_('product'))
    price = models.FloatField(verbose_name=_('price'))

    firstname = models.CharField(max_length=20, verbose_name=_('firstname'))
    lastname = models.CharField(max_length=20, verbose_name=_('lastname'))
    companyname = models.CharField(max_length=50, verbose_name=_('companyname'))
    zipcode = models.CharField(max_length=10, verbose_name=_('zipcode'))
    city = models.CharField(max_length=50, verbose_name=_('city'))
    email = models.EmailField(verbose_name=_('email'))
    phone = models.CharField(max_length=20, verbose_name=_('phone'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')
