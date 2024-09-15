from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import ProductViewSet, ReviewViewSet,CategoryViewSet, OrderItemViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
