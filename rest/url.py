from django.urls import path

from rest.views import ProductsListAPIView

app_name = 'rest'
urlpatterns = [
    path('', ProductsListAPIView.as_view(), name='json'),
    path('<int:pk>', ProductsListAPIView.as_view(), name='json-detail')
]
