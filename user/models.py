from django.contrib.auth.models import AbstractUser
from django.db import models
from user.managers import UserManager

class User(AbstractUser):
    username = None

    name = models.CharField(max_length=150)

    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    class Meta:
        db_table = 'users'
