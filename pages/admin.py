from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from pages.models import ContactModel, BannerModel, InteriorModel, TeamModel


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


@admin.register(ContactModel)
class ContactAdminModel(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email']

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


@admin.register(BannerModel)
class BannerAdminModel(admin.ModelAdmin):
    pass


@admin.register(InteriorModel)
class InteriorAdminModel(admin.ModelAdmin):
    pass


@admin.register(TeamModel)
class InteriorAdminModel(MyTranslation):
    list_display = ['name', 'position']
