from django import forms
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from products.models import TypeModel, MaterialModel, ColorModel, ProductModel, ProductImageModel, ProductCommentModel


class MyTranslation(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(TypeModel)
class TypeAdminModel(MyTranslation):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(MaterialModel)
class MaterialAdminModel(MyTranslation):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


class ColorForm(forms.ModelForm):
    class Meta:
        model = ColorModel
        fields = ['code', 'title']
        widgets = {
            'code': forms.TextInput(attrs={'type': 'color'})
        }


@admin.register(ColorModel)
class ProductColorModelAdmin(admin.ModelAdmin):
    list_display = ['code', 'created_at']
    list_filter = ['created_at']
    form = ColorForm


class ProductImageAdminModel(admin.TabularInline):
    model = ProductImageModel


@admin.register(ProductModel)
class ProductAdminModel(MyTranslation):
    list_display = ['title', 'price', 'discount', 'type', 'created_at']
    list_filter = ['created_at', 'type', ]
    search_fields = ['title', 'price', 'type']
    autocomplete_fields = ['type', 'materials', ]
    readonly_fields = ['real_price']
    inlines = [ProductImageAdminModel]

    def change_view(self, request, **kwargs):
        self.exclude = ('wishlist',)

        return super().change_view(request, **kwargs)


@admin.register(ProductCommentModel)
class ProductCommentAdminModel(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    search_fields = ['name', 'email']
