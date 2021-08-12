from django.urls import path

from user.views import UserTemplateView

app_name = 'user'
urlpatterns = [
    path('', UserTemplateView.as_view(), name='profile'),
]
