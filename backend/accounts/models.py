
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, username=username)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, name, username, password):
      user = self.create_user(email, name, password, username)

      user.is_superuser = True
      user.is_admin = True
      user.save()

      return user


# Create your models here.
class UserAccount(AbstractBaseUser, PermissionsMixin):

    username =  models.CharField(max_length=50, unique=True, null=True, blank=False)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name','email']

    def get_full_name(self):
        return self.name
    
    # def get_username(self):
    #     return self.username
    
    def __str__(self):
        return self.email