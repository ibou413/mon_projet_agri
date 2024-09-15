from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import PostViewSet, CommentViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet)


app_name = 'forum'

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    
]
