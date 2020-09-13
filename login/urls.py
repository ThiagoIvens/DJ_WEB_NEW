from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', auth_views.PasswordChangeView.as_view()),
    path('register/', views.register, name='register'),

]