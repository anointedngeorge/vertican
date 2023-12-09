from django.db import models
from django.contrib.auth.models import Group, User
from django.contrib.auth.models import (
    AbstractBaseUser, 
    PermissionsMixin,
    BaseUserManager,
    UserManager
)
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField

GROUP_ROLES = [
    ('client','Client'),
    ('consultant','Consultant')
]


class CustomUserManager(UserManager):
    
    def _create_user(self, username, password, email, **extra_fields):
        if not email:
            raise ValueError("You have not provided a vaild email address")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(username, password, **extra_fields)

        

class User(AbstractBaseUser, PermissionsMixin):
    # id = models.BigAutoField(editable=False, primary_key=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=300, blank=True, null=True)
    email = models.EmailField(verbose_name='email address',
                              null=True,
                              unique=True, 
                              error_messages="Email Already Taken"
                              )
    username = models.CharField(max_length=300, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    roles = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True, related_name='roles_rel')
    date_joined = models.DateTimeField(auto_now_add=timezone.now(), editable=False)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
 
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return f"{self.email} {self.username}"

    def get_full_name(self):
        return f"{self.email} {self.username}"
    
    # def get_username(self):
    #     return f"{self.email} {self.username}"
    #     # return self.email
    
    def get_short_name(self):
        return self.email.split('@')[0]

    def natural_key(self):
        return f"{self.email} {self.username}"


