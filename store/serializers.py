from typing import List, Any

from django.contrib.auth.models import User
from rest_framework import serializers

from store.models import Product, Order, OrderItem, ShippingAddress, Customer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        exclude = []

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        exclude = ['customer']

class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItem
        exclude = []

class ShippingAddressSerializer(serializers.HyperlinkedModelSerializer):
    customer = CustomerSerializer()
    class Meta:
        model = ShippingAddress
        exclude = []

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        exclude = ['customer']