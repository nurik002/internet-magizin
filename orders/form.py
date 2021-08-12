from django import forms

from orders.models import OrderModel


class OrderFormModel(forms.ModelForm):
    class Meta:
        model = OrderModel
        exclude = ['user', 'product', 'price', 'created_at']
