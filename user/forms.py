from django import forms

from user.models import ProfileModel


class ProfileFormModel(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ['user']
