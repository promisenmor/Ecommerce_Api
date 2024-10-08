from rest_framework import serializers
from . models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        models = Product
        fields = ['id', 'name', 'decription', 'price', 'stock', 'created_at']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart 
        fields = ['id', 'user', 'items', 'created_at']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'total', 'created_at']
