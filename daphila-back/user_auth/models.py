from django.db import models
from django.contrib.auth.models import AbstractUser

# User Model
class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True,max_length=50)
    phone_number = models.CharField(unique=True,max_length=15)
    password = models.CharField(unique=False,max_length=50)
    verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

