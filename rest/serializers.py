from rest_framework import serializers

from products.models import ProductModel, MaterialModel, ColorModel, TypeModel


class MaterialListSerializers(serializers.ModelSerializer):
    """Material List"""

    class Meta:
        model = MaterialModel
        exclude = ['title_en', 'title_ru']


class ColorListSerializers(serializers.ModelSerializer):
    """Colors List"""

    class Meta:
        model = ColorModel
        exclude = ['created_at', 'id']


class TypeListSerializers(serializers.ModelSerializer):
    """Type List"""

    class Meta:
        model = TypeModel
        exclude = ['created_at', 'title_en', 'title_ru']


class ProductsListSerializers(serializers.ModelSerializer):
    """Products List"""
    materials = MaterialListSerializers(many=True)
    colors = ColorListSerializers(many=True)
    type = TypeListSerializers()

    class Meta:
        model = ProductModel
        exclude = ['title_en', 'title_ru', "description_en", "description_ru", 'wishlist', 'discount', 'created_at','price']
