from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import UserManager as BaseUserManager

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, phonenumber, password=None, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not phonenumber:
            raise ValueError('The given phone must be set')
        user = self.model(phonenumber=phonenumber, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, phonenumber, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', False)
        return self._create_user(phonenumber, password, **extra_fields)

    def create_superuser(self, phonenumber, password=None, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phonenumber, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    phonenumber = models.CharField(max_length=11, unique=True, verbose_name='phonenumber', blank=False, help_text='Enter 11 digits phone number')
    #is_active=False

    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()



#class CustomUser(AbstractUser):
    #REQUIRED_FIELDS = []
    #USERNAME_FIELD = "phonenumber"
    #username = None
    #phonenumber=models.CharField(max_length=12,unique=True)
   # objects = UserManager()


