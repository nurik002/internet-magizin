from modeltranslation.translator import register, TranslationOptions

from posts.models import AuthorModel, PostModel


@register(AuthorModel)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(PostModel)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
