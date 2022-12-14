from django.urls import include, path
from django.conf import settings
from django.contrib import admin
from django.conf.urls .static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('movies/', include('movies.urls', namespace='movies')),
    path('accounts/', include('users.urls', namespace='users')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('pages.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
