"""
Developer: Anilkumar Bathala
email: anilkumar.bathala@yahoo.com
portfolio: https://anilkumar-bathala.github.io/portfolio
Date: 03-09-2023
Description: ____
"""
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('home/', HomeView.as_view(), name='home'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login url
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),  # login refresh token url
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
