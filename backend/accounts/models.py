
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, major, password=None):
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, major=major)
        
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_admin = True
        
        user.is_superuser = True
        user.save()
        return user


# Create your models here.
class UserAccount(AbstractBaseUser, PermissionsMixin):
    SOCIAL_CHOICE = (('instagram', 'instagram'),
                     ('linkedin', 'linkedin'), ('resume', 'resume'))

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    major = models.CharField(max_length=50)
    # social_media = models.CharField( max_length=50, choices =  SOCIAL_CHOICE)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name', 'major']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def get_major(self):
      return self.major

    def __str__(self):
        return self.email
