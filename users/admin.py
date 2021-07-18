from django.contrib import admin
from .models import UserModel
# Register your models here.

class UserConfig(admin.ModelAdmin):
    list_display = ['username', 'email', 'full_name', 'is_staff', 'date_joined']
    search_fields = ['username', 'email', 'full_name', 'is_staff', 'date_joined']
    list_filter = ['is_staff', 'date_joined', 'is_superuser']


admin.site.register(UserModel, UserConfig)