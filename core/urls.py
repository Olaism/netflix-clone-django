from django.urls import include, path
from django.conf import settings
from django.contrib import admin
from django.conf.urls .static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('movies/', include('movies.urls', namespace='movies')),
    path('accounts/', include('users.urls', namespace='users')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
