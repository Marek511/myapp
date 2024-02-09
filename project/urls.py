from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from quotes.views import main


urlpatterns = [
    path('', include('quotes.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
