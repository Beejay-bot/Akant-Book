from users.views import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

# Create your models here.

class CustomAccountManager(BaseUserManager):
    def create_user(self,username,email,password, full_name, **other_fields):
        if not email:
            raise ValueError('You must provided the neccessary values required to proceed: email, username,full_name and password')
        other_fields.setdefault('is_active', True)
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, password=password, full_name=full_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,username,password, full_name, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') and other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Super must be assigned to is_staff=True and is_superuser=True'
            )
        return self.create_user(username,email, password,full_name, **other_fields)

class UserModel(AbstractBaseUser, PermissionsMixin):
    email= models.EmailField(_('email address'), unique=True)
    full_name = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=200, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    REQUIRED_FIELDS = ['email', 'full_name']
    USERNAME_FIELD = 'username'

    def __str__(self) -> str:
        return self.username

    @receiver(post_save, sender=get_user_model())
    def user_post_save(sender,request, instance, *args, **kwargs):
        print('User was saved.', instance.id)