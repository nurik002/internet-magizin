from modeltranslation.translator import register, TranslationOptions

from products.models import TypeModel, MaterialModel, ProductModel


@register(TypeModel)
class TypeTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(MaterialModel)
class MaterialTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ProductModel)
class ProductsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
