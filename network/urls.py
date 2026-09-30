# network/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, RelationshipViewSet

# Router automatically creates RESTful URLs for our ViewSets
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'relationships', RelationshipViewSet)

urlpatterns = [
    path('', include(router.urls)),
]