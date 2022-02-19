from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import HomePage


urlpatterns = [
    path('', HomePage.as_view()),
    path('admin/', admin.site.urls),
    path('summary_per_hour/', include('summary_per_hour.urls', namespace='summary_per_hour')),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
