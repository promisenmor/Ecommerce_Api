from django.urls import path
from .views import ProductListCreate, ProductDetail, CartListCreate, OrderListCreate, CategoryListCreate, CategoryDetail, UserProfileDetail, ReviewListCreate, PaymentCreate

urlpatterns = [
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('cart/', CartListCreate.as_view(), name='cart-list-create'),
    path('orders/', OrderListCreate.as_view(), name='order-list-create'),
    path('profile/', UserProfileDetail.as_view(), name='user-profile-detail'),
    path('products/<int:product_id>/reviews/', ReviewListCreate.as_view(), name='review-list-create'),
    path('payments/', PaymentCreate.as_view(), name='payment-create'),
]

