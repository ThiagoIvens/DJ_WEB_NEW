from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'orderItem', views.OrderItemViewSet)
router.register(r'ShippingAddress', views.ShippingAddressViewSet)

urlpatterns = [
	# Loja
	path('', views.index, name="index"),
	path('shop-grid/', views.shop_grid, name="shop-grid"),
	path('shoping-cart/', views.shoping_cart, name="shoping-cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('contact/', views.contact, name="contact"),


	# ordens e atualizar item
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

	# auth
	path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('token/', obtain_auth_token, name='api_token_auth'),
]