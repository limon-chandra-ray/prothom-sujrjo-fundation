from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager
# Create your models here.
class CustomUser(AbstractBaseUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN','Admin'
        DONAR = 'DONAR','Donar'
        STAFF = 'STAFF', 'Staff'
    base_role = Role.ADMIN

    user_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True,max_length=250)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    role = models.CharField(max_length=30,choices=Role.choices)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']
    objects = CustomUserManager()
    def __str__(self):
        return self.user_name
    
    def has_perm(self,prem,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    
    def save(self,*args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)
