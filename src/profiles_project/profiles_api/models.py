from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfilesManager(BaseUserManager):
    """"""
    def create_user(self, email, name, password=None):
        """ Create"""

        if not email:
            raise ValuesError('Users must have an email address.')
        email = self.normalize_email(email)
        user = self.model(email = email, name = name)
        #token = Token.objects.create(user=...)
        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_superuser(self, email, name, password):

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using= self._db)
        return user

# Create your models here.
class UserProfiles(AbstractBaseUser, PermissionsMixin):
    """..."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length= 255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserProfilesManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        """ Used to get a user full name """
        return self.name

    def get_short_name(self):
        """ Used to get a user short name """
        return self.name

    def __str__(self):
        return self.email


class ProfileFeedItems(models.Model):

    user_profile = models.ForeignKey('UserProfiles', on_delete = models.CASCADE)
    status_text = models.CharField(max_length = 200)
    create_on = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        """Return the model as a string."""
        return self.status_text
