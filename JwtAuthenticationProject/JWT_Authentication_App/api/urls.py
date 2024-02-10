"""
@author: Rohit Chaurasia
@brief: Django URLs Configuration for JWT Authentication App
This module defines the URL patterns for the JWT Authentication App, including views for login, token refresh,
logout, user registration, and other experimental views.

"""

from django.urls import path
from .views import RegistrationAPIView, VerifyOTPAPIView, LogoutBlacklistTokenUpdateView, DemoView, DemoView2, MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('verify/', VerifyOTPAPIView.as_view(), name='verify-otp'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutBlacklistTokenUpdateView.as_view(), name='logout'),
    path('register/', RegistrationAPIView.as_view(), name='registration'),
    path('experiment/',DemoView.as_view(),name='demo'),
    path('experiment2/',DemoView2.as_view(),name='demo2')

]