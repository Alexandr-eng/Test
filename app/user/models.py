from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from app.user.managers import CustomManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        db_index=True,
        unique=True,
        blank=False,
        max_length=20,
    )
    is_staff = models.BooleanField(
        verbose_name='staff',
        default=False,
    )

    objects = CustomManager()

    USERNAME_FIELD = "username"

    @property
    def is_authenticated(self):
        return True

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"ID: {self.id}, Username: {self.username}"