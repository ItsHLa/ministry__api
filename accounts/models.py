from django.contrib.auth.models import Group, PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a name address')
        user = self.model(
            email=self.normalize_email(email),## make email to lower case
            username=username
        )## creating user
        user.set_password(password)## set password
        user.save(using=self._db)

        return user

    def create_superuser(self,username,email,password):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

## is_active is_staff is_superuser are required to be overridden
## USERNAME_FILED defines what field is based on login

class User(AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(unique=True,verbose_name='email', max_length=60)
    username = models.CharField(unique=False ,max_length=60)
    date_joined = models.DateTimeField(auto_now_add=True,verbose_name='date_joined')
    last_login = models.DateTimeField(auto_now=True,verbose_name='last_login')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    objects=UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username' ]

    def __str__(self):
        return self.username
    def has_perm(self, perm, obj=None):
        return self.is_superuser
    def has_module_perms(self, perm, obj=None):
        return True
    def has_role(self,role):
        return self.groups.filter(name=role).exists()