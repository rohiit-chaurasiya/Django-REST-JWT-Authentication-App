"""
@author: Rohit Chaurasia
@brief: JWT Authentication App Views
This module contains Django views for various API endpoints related to JWT authentication.
"""

from .serializers import RegistrationSerializer, VerifyOTPSerializer, MyTokenObtainPairSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from JWT_Authentication_App.emails import *
from JWT_Authentication_App.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.throttling import ScopedRateThrottle
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



"""
TokenObtainPairView extends TokenObtainPairView and uses the custom serializer MyTokenObtainPairSerializer.
It also defines a throttle_scope for login attempts.
"""
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    throttle_scope = 'login'


# class LoginTokenGenerationAPIView(APIView):

#     def post(self, request, *args, **kwargs):
#         serializer = LoginTokenGenerationSerializer(data=request.data)
#         data = {}

#         if serializer.is_valid(raise_exception=True):

#             email = serializer.data['email']
#             password = serializer.data['password']
#             user_obj = User.objects.get(email=email)


#             try:
#                 if user_obj is not None:
#                     access_token = AccessToken.for_user(user=user_obj)
#                     refresh_token = RefreshToken.for_user(user=user_obj)
#                     data['refresh'] = str(access_token)
#                     data['access'] = str(refresh_token)

#             except Exception as e:
#                 return Response({'message':'username or password is incorrect'})

#         return Response(data, status.HTTP_200_OK)


"""
RegistrationAPIView handles user registration, including sending OTP for verification.
"""
class RegistrationAPIView(generics.GenericAPIView):
    '''Registers user'''
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        data = {}
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            send_otp(serializer.data['email'])
            data['response'] = "Registration Successful!"
            refresh = RefreshToken.for_user(user=user)
            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)

        return Response(data, status.HTTP_201_CREATED)

class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()

"""
VerificationAPIView handles the verification of OTP for user email verification.
"""
class VerifyOTPAPIView(generics.GenericAPIView):
    serializer_class = VerifyOTPSerializer  # Set the serializer class

    def post(self, request, *args, **kwargs):
        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data['email']
            otp = serializer.data['otp']
            user_obj = User.objects.get(email=email)

            if user_obj.otp == otp:
                user_obj.is_staff = True
                user_obj.save()
                return Response("verified")
            return Response(serializer.data, status.HTTP_400_BAD_REQUEST)


"""
LogoutAPIView handles blacklisting the refresh token, effectively logging the user out.
"""
class LogoutBlacklistTokenUpdateView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:

            return Response(status=status.HTTP_400_BAD_REQUEST)


class DemoView(APIView):
    # authentication_classes=[JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            return Response("accessed")
        except Exception as e:
            print(e)
            return Response("")

"""
DemoAPIView is an example API view that requires authentication.
"""
class DemoView2(APIView):
    # authentication_classes=[JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            return Response("accessed 2")
        except Exception as e:
            print(e)
            return Response("")