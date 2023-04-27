from django.contrib import admin
from django.urls import path, include
from AppKaren.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", inicio),
    path("AppKaren/", include("AppKaren.urls")),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)