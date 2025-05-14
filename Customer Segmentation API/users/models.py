from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class CustomerUserManager(BaseUserManager):
    
    def create_user(self, email, password,**extra_fields):
        print("create user called")
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        print("create super user called")
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))    

        return self.create_user(email, password, **extra_fields)
             


class Users(AbstractUser):

    objects = CustomerUserManager()
    first_name = None
    last_name = None
    
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(_('email address'),max_length=30,unique=True)
    phone = models.BigIntegerField(unique=True,default=None)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
 


    class Meta:
        db_table = 'users'
      

    def __str__(self):
        return self.email



        
