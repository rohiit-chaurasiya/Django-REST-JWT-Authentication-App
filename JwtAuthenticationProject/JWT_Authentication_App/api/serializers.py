"""
@author: Rohit Chaurasia
@brief: Define serializers for JWT Authentication App
MyTokenObtainPairSerializer: A custom serializer for obtaining JWT tokens.
RegistrationSerializer: A serializer for user registration.
VerifyOTPSerializer: A serializer for verifying user's OTP.
"""

from JWT_Authentication_App.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from JWT_Authentication_App.models import User as user


"""
Custom TokenObtainPairSerializer
This serializer extends the TokenObtainPairSerializer provided by rest_framework_simplejwt.
It includes a method to retrieve the token and can be customized further if needed.
"""
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

"""
Serializer for user registration.
This serializer is used for user registration, including validation of passwords and saving
the user object to the database.
"""
class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'user_name', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    """
    Save method to create a new user and store in the database.
    Returns: User: The newly created user object.
    """
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'error': 'passwords did not match'})

        user = User(email=self.validated_data['email'],
                    user_name=self.validated_data['user_name'], is_active=True)
        user.set_password(self.validated_data['password'])
        user.save()
        return user


"""
Serializer for verifying user's OTP.
This serializer is used to validate and verify the OTP during user authentication.
"""
class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()

# class CustomTokenRefreshViewSerializer(TokenRefreshView):
#     def validate(self, attrs):
#         # The default result (access/refresh tokens)
#         data = super(CustomTokenRefreshViewSerializer, self).validate(attrs)
#         # Custom data you want to include
#         data.update({'user': self.user.username})
#         data.update({'id': self.user.id})
#         # and everything else you want to send in the response
#         return data

# class LoginTokenGenerationSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField()

