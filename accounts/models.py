from email.policy import default
from enum import unique
from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('member', 'Member'),
        ('admin', 'Admin')
    ]
    email = models.EmailField(unique=True, null=True)    
    role = models.CharField(max_length= 30, choices = ROLE_CHOICES, default='member')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
        
    
    