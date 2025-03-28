# database models

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    # manager for the user

    def create_user(self, email, password=None, **extra_fields):
        # create , save and return new user
        email = self.normalize_email(email)
        user = self.model(email=email ,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser,PermissionsMixin):
    # user in the system
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255 , unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_Staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
