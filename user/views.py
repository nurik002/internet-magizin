from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView

from user.forms import ProfileFormModel
from user.models import ProfileModel


class UserTemplateView(LoginRequiredMixin, UpdateView):
    template_name = 'login.html'
    form_class = ProfileFormModel

    def get_success_url(self):
        return reverse('user:profile')

    def get_object(self, queryset=None):
        profile, created = ProfileModel.objects.get_or_create(user =self.request.user)
        return profile
