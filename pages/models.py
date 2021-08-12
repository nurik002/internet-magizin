from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here

class ContactModel(models.Model):
    name = models.CharField(max_length=30, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'), unique=True)
    message = models.TextField(verbose_name=_('message'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')


class BannerModel(models.Model):
    image = models.ImageField(upload_to='Banner')

    class Meta:
        verbose_name = _('banner')
        verbose_name_plural = _('banners')


class InteriorModel(models.Model):
    image = models.ImageField(upload_to='Interior')

    class Meta:
        verbose_name = _('interior')
        verbose_name_plural = _('interiors')


class TeamModel(models.Model):
    image = models.ImageField(upload_to='team')
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('team')
        verbose_name_plural = _('teams')
