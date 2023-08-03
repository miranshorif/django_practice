from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        user = self.models(email = email, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    
    def create_user(self,email=None,password=None,**extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email,password,**extra_fields)
    
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be is_staff True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must be is_superuser True")
        return self._create_user(email,password,**extra_fields)