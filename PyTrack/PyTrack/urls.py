from django.contrib import admin
from django.urls import path, include
from learning.views import custom_404
from django.conf.urls import handler404
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = custom_404