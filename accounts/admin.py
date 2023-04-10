from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile


# Register your models here.
class UserAdmin(UserAdmin):
    list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'is_staff', 'role', 'is_active']
    list_display_links = ['email', 'username']
    search_fields = ['username', 'email']
    list_filter = ['first_name', 'last_name']
    ordering = ['-date_joined']
    readonly_fields = ['last_login', 'last_login', 'date_joined']

    # required fields because of custom user admin model
    filter_horizontal = []
    fieldsets = []
    list_filter = []


admin.site.register(User, UserAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'country', 'state', 'city', 'pin_code']
    list_display_links = ['user']
    list_filter = ['country', 'state', 'city']


admin.site.register(UserProfile, UserProfileAdmin)
