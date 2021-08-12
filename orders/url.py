from django.urls import path

from orders.views import OrderCreateView, HistoryListView

app_name = 'orders'
urlpatterns = [
    path('', OrderCreateView.as_view(), name='order_create'),
    path('history/', HistoryListView.as_view(), name='order-history')
]
