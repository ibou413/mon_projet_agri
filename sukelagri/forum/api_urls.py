from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListCreateAPIView.as_view(), name='post-list-create'),
    path('comments/', views.CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('categories/', views.CategoryListCreateAPIView.as_view(), name='category-list-create'),
    # Ajoutez d'autres routes API ici
]
