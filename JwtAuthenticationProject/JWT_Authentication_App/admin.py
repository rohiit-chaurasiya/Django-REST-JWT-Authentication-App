"""
@author: Rohit Chaurasia
@brief: This module contains the Django admin configuration for the User model in the JWT Authentication App.
"""

from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


# # Register your models here.

"""
This class extends the default UserAdmin and customizes it for the User model in the JWT Authentication App.
"""
class UserAdminConfig(UserAdmin):
    # model = User

    search_fields = ('email', 'user_name')
    ordering = ('start_date',)

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    # list_filter = ('email','user_name','is_active','is_staff')
    list_display = ('email', 'id', 'user_name', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'user_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),

    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'password1', 'password2', 'is_staff', 'is_active'),
        }),

    )


"""
Register the User model with the custom admin configuration
"""
admin.site.register(User, UserAdminConfig)