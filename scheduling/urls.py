from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import SchedulingViewSet

router = DefaultRouter()
router.register(r'/',SchedulingViewSet, basename='scheduling')
scheduling_urls = router.urls