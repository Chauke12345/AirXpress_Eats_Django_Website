
"""
URL configuration for AirXpress Eats marketing website.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('publicsite.urls')),
]

# Serve uploaded media from the persistent Railway volume.
if settings.DEBUG or str(settings.MEDIA_ROOT).startswith('/app/data'):
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
