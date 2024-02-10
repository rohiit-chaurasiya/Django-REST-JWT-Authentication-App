"""
@author: Rohit Chaurasia
@brief: This module defines the User model and UserManager for the JWT Authentication App.
"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


"""
This manager provides methods to create regular users and superusers.
"""
class UserManager(BaseUserManager):
    """
    Create a user.
    Args:
        email (str): User's email address.
        user_name (str): User's username.
        password (str): User's password.
        other_fields (dict): Additional fields for the user.
    Returns:
        User: The created user object.
    """
    def create_user(self, email, user_name, password, **other_fields):

        if not email:
            raise ValueError("Provide email")
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


    """
    Create a superuser.
    Args:
        email (str): Superuser's email address.
        user_name (str): Superuser's username.
        password (str): Superuser's password.
        other_fields (dict): Additional fields for the superuser.
    Returns:
        User: The created superuser object.
    """
    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('staff privilege must be assigned to superuser')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('superuser privilege must be assigned to superuser')

        return self.create_user(email, user_name, password, **other_fields)


"""
Custom User Model
This model represents the user in the JWT Authentication App.
"""
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=100, unique=True)
    otp = models.CharField(max_length=10, null=True, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_name