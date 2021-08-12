from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from products.models import ProductModel
from rest.serializers import ProductsListSerializers


class ProductsListAPIView(ListAPIView):
    serializer_class = ProductsListSerializers

    def get_queryset(self):
        qs = ProductModel.objects.all()
        pk = self.kwargs.get('pk')
        if pk:
            qs = qs.filter(pk=pk)
        return qs
