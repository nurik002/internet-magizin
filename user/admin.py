from django.contrib import admin

from user.models import ProfileModel


@admin.register(ProfileModel)
class ProfileAdminModel(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'phone']
    search_fields = ['firstname', 'lastname', 'email', 'phone']
