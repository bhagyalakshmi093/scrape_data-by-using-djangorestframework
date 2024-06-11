from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CryptoDataViewSet

router = DefaultRouter()
router.register(r'crypto', CryptoDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


