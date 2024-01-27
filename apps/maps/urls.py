from django.urls import path, re_path, include
from .views import InterestPointsMap, InterestPointDetailView
from .views import CreateInterestPoint, UpdateInterestPoint, CreateCamperNightPoint, UpdateCamperNightPoint

app_name = 'maps'

urlpatterns = [
    path('home', InterestPointsMap.as_view(), name='home'),
    path('InterestPoint/<pk>/detail/', InterestPointDetailView.as_view(), name='InterestPointDetailView'),
    path('InterestPoint/create', CreateInterestPoint.as_view(), name='CreateInterestPoint'),
    path('InterestPoint/<pk>/update', UpdateInterestPoint.as_view(), name='UpdateInterestPoint'),

    path('CamperNightPoint/create', CreateCamperNightPoint.as_view(), name='CreateInterestPoint'),
    path('CamperNightPoint/<pk>/update', UpdateCamperNightPoint.as_view(), name='UpdateInterestPoint'),
]
