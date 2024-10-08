from django.urls import path
from .views import ProductListCreate, ProductDetail, CartListCreate, OrderListCreate

urlpatterns = [
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('cart/', CartListCreate.as_view(), name='cart-list-create'),
    path('orders/', OrderListCreate.as_view(), name='order-list-create')
]