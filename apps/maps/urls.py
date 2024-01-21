from django.urls import path, re_path, include
from .views import CreateInterestPoint, UpdateInterestPoint

app_name = 'maps'

urlpatterns = [
    path('InterestPoint/create', CreateInterestPoint.as_view(), name='CreateInterestPoint'),
    path('updateProject/<pk>/', UpdateInterestPoint.as_view(), name='UpdateInterestPoint'),
]
