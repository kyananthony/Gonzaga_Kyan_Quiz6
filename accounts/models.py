from django.contrib.auth.models import AbstractBaseUser , BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, contact_number, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not contact_number:
            raise ValueError('Users must have a contact number')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, contact_number=contact_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, contact_number, password=None):
        user = self.create_user(email, username, contact_number, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser (AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    contact_number = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()  # Correctly instantiate the manager

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'contact_number']

    def __str__(self):
        return self.email