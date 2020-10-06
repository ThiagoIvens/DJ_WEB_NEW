from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
import json
import datetime

from .models import *
from django.contrib import auth
from django.contrib.auth.models import User
from rest_framework import viewsets
from store.serializers import UserSerializer, ProductSerializer, ShippingAddressSerializer, OrderItemSerializer, \
 	OrderSerializer


def index(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	products = Product.objects.all()
	context = {'order':order, 'items':items, 'products':products, 'cartItems':cartItems}
	return render(request, 'store/index.html', context)

def shop_grid(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	products = Product.objects.all()
	context = {'order':order, 'items':items, 'products':products, 'cartItems':cartItems}
	return render(request, 'store/shop-grid.html', context)

def shoping_cart(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	products = Product.objects.all()
	context = {'order':order, 'items':items, 'products':products, 'cartItems':cartItems}
	return render(request, 'store/shoping-cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	products = Product.objects.all()
	context = {'order':order, 'items':items, 'products':products, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def contact(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	products = Product.objects.all()
	context = {'order':order, 'items':items, 'products':products, 'cartItems':cartItems}
	return render(request, 'store/contact.html', context)

# vvvvvvvvvvvvvvvvvvvvvvvvvvvv ANTIGO vvvvvvvvvvvvvvvvvvvvvvvvvvvv



def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
		orderItem.save()
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)
		orderItem.save()
	elif action == 'delete':
		orderItem.delete()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item foi adicionado', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		total = float(data['form']['total'])
		order.transaction_id = transaction_id

		if total == order.get_cart_total:
			order.complete = True
		order.save()

		if order.shipping == True:
			ShippingAddress.objects.create(
			customer=customer,
			order=order,
			address=data['shipping']['address'],
			city=data['shipping']['city'],
			state=data['shipping']['state'],
			zipcode=data['shipping']['zipcode'],
			)
	else:
		print('Usuário no está logado...')

	return JsonResponse('Pagamento submetido..', safe=False)


def login_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		# Correct password, and the user is marked "active"
		auth.login(request, user)
		# Redirect to a success page.
		return HttpResponseRedirect("index")
	else:
		# Show an error page
		return HttpResponseRedirect("/account/login/")


def logout_view(request):
	auth.logout(request)
	# Redirect to a success page.
	return HttpResponseRedirect("index")


class UserViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()

class OrderViewSet(viewsets.ModelViewSet):
	serializer_class = OrderSerializer
	queryset = Order.objects.all()

class OrderItemViewSet(viewsets.ModelViewSet):
	serializer_class = OrderItemSerializer
	queryset = OrderItem.objects.all()

class ShippingAddressViewSet(viewsets.ModelViewSet):
	serializer_class = ShippingAddressSerializer
	queryset = ShippingAddress.objects.all()
