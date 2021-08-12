from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
urlpatterns += i18n_patterns(
    path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
    path('', include('pages.url', namespace='pages')),
    path('products/', include('products.url', namespace='shop')),
    path('posts/', include('posts.url', namespace='blog')),
    path('profile/', include('user.url', namespace='user')),
    path('orders/', include('orders.url', namespace='orders')),
    path('rest/', include('rest.url', namespace='rest')),

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
