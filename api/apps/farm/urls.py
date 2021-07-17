from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FarmViewSet, FarmerViewSet

farm_router = DefaultRouter()
farm_router.register('farm', FarmViewSet, basename='farm')
farm_router.register('farmer', FarmerViewSet, basename='farmer')

urlpatterns = [
    path('api/', include(farm_router.urls)),
]
