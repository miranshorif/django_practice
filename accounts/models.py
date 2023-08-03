from typing import Optional
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
# Create your models here.

class CustomAccountManager(BaseUserManager):
    def create_user(self, email, zep_code, password):
        user = self.model(email=email, zep_code=zep_code, password=password)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, zep_code, password):
        user = self.model(email=email, zep_code=zep_code, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user
    
    def get_by_natural_key(self, email_):
        print(email_)
        return self.get(email = email_)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    zip_code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['zip_code', 'password']
    
    objects = CustomAccountManager()
    
    def get_short_name(self):
        return self.email
    
    def natural_key(self):
        return self.email
    
    def __str__(self):
        return self.email
