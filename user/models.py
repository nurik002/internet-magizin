from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

UserModel = get_user_model()


class ProfileModel(models.Model):
    user = models.OneToOneField(UserModel, related_name='profile', on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('firstname'))
    lastname = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('lastname'))
    companyname = models.CharField(max_length=50, blank=True, null=True, verbose_name=_('companyname'))
    zipcode = models.CharField(max_length=10, blank=True, null=True, verbose_name=_('zipcode'))
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name=_('city'))
    email = models.EmailField(blank=True, null=True, verbose_name=_('email'))
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('phone'))

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')
