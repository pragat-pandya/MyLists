from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class MyAccountManager (BaseUserManager):
  def create_user (self, first_name, last_name, username, password=None):
    if not username:
      raise ValueError('You must provide an username')
    
    user = self.model (
      first_name = first_name,
      last_name = last_name, 
      username = username
    )

    user.set_password(password)
    user.save (using=self._db)
    return user
  
  def create_superuser (self, first_name, last_name, username, password):
    user = self.create_user (
      first_name = first_name,
      username = username,
      last_name = last_name,
      password = password
    )

    user.is_admin = True
    user.save(using=self._db)
    return user

class Account (AbstractBaseUser):
  first_name = models.CharField (max_length=50)
  last_name = models.CharField (max_length=50)
  username = models.CharField (max_length=50)

  is_admin = models.BooleanField (default=False)
  
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
  USERNAME_FIELD = 'username'

  objects = MyAccountManager()