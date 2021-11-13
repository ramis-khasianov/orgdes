from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'
    email = models.EmailField('email', unique=True, blank=False, null=False)

    def __str__(self):
        return self.email
