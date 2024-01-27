# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings
from django.conf.urls.static import static
from apps.maps.views import InterestPointsMap

urlpatterns = [
    path('test', InterestPointsMap.as_view, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("", include("apps.authentication.urls")),  # Auth routes - login / register
    path("", include("apps.home.urls")),  # UI Kits Html files
    path("maps/", include("apps.maps.urls")),
    path('', include('pwa.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
