# oee_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MachinesViewSet, ProductionLogViewSet

router = DefaultRouter()
router.register(r'machines', MachinesViewSet)
router.register(r'productionlogs', ProductionLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
