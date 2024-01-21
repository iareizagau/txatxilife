from django.urls import path, re_path, include
from .views import InterestPointTemplateView
from .views import CreateInterestPoint, UpdateInterestPoint, CreateCamperNightPoint, UpdateCamperNightPoint

app_name = 'maps'

urlpatterns = [
    path('home', InterestPointTemplateView.as_view(), name='home'),
    path('InterestPoint/create', CreateInterestPoint.as_view(), name='CreateInterestPoint'),
    path('InterestPoint/<pk>/update', UpdateInterestPoint.as_view(), name='UpdateInterestPoint'),

    path('CamperNightPoint/create', CreateCamperNightPoint.as_view(), name='CreateInterestPoint'),
    path('CamperNightPoint/<pk>/update', UpdateCamperNightPoint.as_view(), name='UpdateInterestPoint'),
]
