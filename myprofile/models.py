from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    pan = models.CharField(max_length=10,unique=True)
    dob = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    slug = models.SlugField(unique=True)
    # adding this line so the user can own profiles
    user = models.OneToOneField(User, blank=True, null=True)

    # _pan = models.CharField(db_column="pan",max_length=10)
    #
    # @property
    # def pan(self):
    #     return self._pan
    #
    # @pan.setter
    # def pan(self, pan):
    #     if (pan[4] == 'P' and pan[9].isdigit() == True and pan[:5].isalpha() == True and
    #                 pan[6:9].isnumeric() == True):
    #         self._pan = pan
    #     else:
    #         logger.warning("Enter PAN details properly.")
