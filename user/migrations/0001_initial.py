# Generated by Django 3.2.3 on 2021-06-06 05:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=20, null=True, verbose_name='firstname')),
                ('lastname', models.CharField(blank=True, max_length=20, null=True, verbose_name='lastname')),
                ('companyname', models.CharField(blank=True, max_length=50, null=True, verbose_name='companyname')),
                ('zipcode', models.CharField(blank=True, max_length=10, null=True, verbose_name='zipcode')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='city')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='phone')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
        ),
    ]