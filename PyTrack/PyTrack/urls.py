from django.contrib import admin
from django.urls import path, include
from learning.views import custom_404
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning.urls')),
]

handler404 = custom_404