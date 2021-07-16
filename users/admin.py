from core.models import User
from django.contrib import admin
from .models import UserModel
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class UserAdminConfig(UserAdmin):
    search_fields = ('email', "username", "full_name")
    ordering = ('-date_joined',)
    list_filter = ( 'email', 'username', 'full_name', 'is_active', 'is_staff')
    list_display = ( 'email', 'username', 'full_name', 'is_active', 'is_staff')
    fieldsets = (
        (None,{'fields':('email','username', 'full_name',)}),
        ('Permissions', {'fields':('is_staff', 'is_active')}),
    )

admin.site.register(UserModel, UserAdminConfig)