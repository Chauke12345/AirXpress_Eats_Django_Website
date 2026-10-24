
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('publicsite.urls')),
]

# Serve uploaded partner logos from Railway's persistent media folder.
if str(settings.MEDIA_ROOT).startswith('/app/data'):
    urlpatterns += [
        re_path(
            r'^media/(?P<path>.*)$',
            serve,
            {'document_root': settings.MEDIA_ROOT},
        ),
    ]
elif settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
