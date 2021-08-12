from datetime import datetime

import pytz
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models

from django.utils.translation import ugettext_lazy as _

# Create your models here.
UserModel = get_user_model()


class TypeModel(models.Model):
    title = models.CharField(max_length=30, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('type')
        verbose_name_plural = _('types')


class MaterialModel(models.Model):
    title = models.CharField(max_length=30, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('material')
        verbose_name_plural = _('materials')


class ColorModel(models.Model):
    code = models.CharField(max_length=30, verbose_name=_('code'))
    title = models.CharField(max_length=30, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _('colors')


class ProductModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    type = models.ForeignKey(TypeModel, on_delete=models.PROTECT, related_name='products', verbose_name=_('type'))
    price = models.FloatField(verbose_name=_('price'))
    wishlist = models.ManyToManyField(UserModel, related_name='wishlist', verbose_name=_('wishlist'))
    discount = models.FloatField(verbose_name=_('discount', ), default=0)
    real_price = models.FloatField(verbose_name=_('real_price'), default=0)
    description = RichTextField(verbose_name=_('description'))
    materials = models.ManyToManyField(
        MaterialModel,
        related_name='products',
        verbose_name=_('material'))
    colors = models.ManyToManyField(ColorModel, related_name='products', verbose_name=_('colors'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def is_new(self):
        delta = datetime.now(pytz.timezone('Asia/Tashkent')) - self.created_at
        return delta.days <= 3

    def is_discount(self):
        return self.discount != 0

    def get_image(self):
        images = self.images.all()
        if images:
            return images.first().image.url

        return '/static/assets/images/No_Image-512.png'

    def get_comment(self):
        return self.comments.order_by('-pk')

    @staticmethod
    def get_from_cart(request):
        cart = request.session.get('cart', [])
        return ProductModel.objects.filter(pk__in=cart)

    @staticmethod
    def get_discount_product(request):
        return ProductModel.objects.filter(discount__gte=0)


class ProductImageModel(models.Model):
    image = models.ImageField(upload_to='product', verbose_name=_('image'))
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_('product'))

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')


# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, related_name='items')
#     product = models.ForeignKey(ProductModel, related_name='order_items', on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField(default=1)
#
#     def __str__(self):
#         return '{}'.format(self.id)


class ProductCommentModel(models.Model):
    name = models.CharField(max_length=30, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    comment = models.TextField(verbose_name=_('comment'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    products = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='comments',
                                 verbose_name=_('products'))


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
