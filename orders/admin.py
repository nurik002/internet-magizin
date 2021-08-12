from django.contrib import admin

from orders.models import OrderModel


@admin.register(OrderModel)
class OrderAdminModel(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'email']
