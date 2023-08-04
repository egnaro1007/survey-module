from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GOD = 'god'
    ADMIN = 'admin'
    MANAGER = 'manager'
    USER = 'user'

    PERMISSION_CHOICES = (
        (GOD, 'God'),
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (USER, 'User'),
    )

    permission = models.CharField(max_length=20, choices=PERMISSION_CHOICES, blank=False, null=False)
