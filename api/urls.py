from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CatViewSet, HealthCheckView

router = DefaultRouter()
router.register(r'cats', CatViewSet, basename='cat')

urlpatterns = [
    path('health/', HealthCheckView.as_view(), name='health-check'),
    path('', include(router.urls)),
]
