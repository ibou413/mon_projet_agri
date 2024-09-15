from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import CategoryViewSet, ProductViewSet, OrderViewSet, OrderItemViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'reviews', ReviewViewSet)


app_name = 'market'

urlpatterns = [
   
    path('', views.market_home, name='home'),
    path('api/', include(router.urls)),
]
