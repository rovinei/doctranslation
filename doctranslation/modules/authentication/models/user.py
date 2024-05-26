from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from doctranslation.modules.common.models import BaseModel


class UserQuerySet(models.QuerySet):
    pass


class UserManager(models.Manager.from_queryset(UserQuerySet), BaseUserManager):
    def _create_user(self, email, password, is_superuser, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_active=True,
            is_superuser=is_superuser,
            **extra_fields,
        )

        user.set_password(password)
        user.save()

        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, **extra_fields)

    def make_random_password(
            self,
            length=20,
            allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789"~!@#$%^&*()_+={}[]|:;<>,.?/',
    ):
        return super().make_random_password(
            length=length,
            allowed_chars=allowed_chars,
        )


class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    username = models.CharField(max_length=128, unique=True, null=True, blank=True, default=None)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    last_accessed_at = models.DateTimeField(blank=True, null=True, default=None)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def is_staff(self):
        return self.is_superuser
