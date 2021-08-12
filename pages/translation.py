from modeltranslation.translator import register, TranslationOptions

from pages.models import TeamModel


@register(TeamModel)
class TypeTranslationOptions(TranslationOptions):
    fields = ('name', 'position',)
