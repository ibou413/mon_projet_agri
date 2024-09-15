from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('products/', views.ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('orders/', views.OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('reviews/', views.ReviewListCreateAPIView.as_view(), name='review-list-create'),
    # Ajoutez d'autres routes API ici
]
