from typing import List, Any

from django.contrib.auth.models import User
from rest_framework import serializers

from store.models import Product, Order, OrderItem, ShippingAddress


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        exclude = []

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        exclude = []

class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItem
        exclude = []

class ShippingAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShippingAddress
        exclude = []