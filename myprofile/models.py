from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255,null=True , blank=True)
    pan = models.CharField(max_length=10)
    dob = models.CharField(max_length=50,null=True,blank=True)
    phone = models.CharField(max_length=10,null=True,blank=True)
    slug = models.SlugField(unique=True)
    # adding this line so the user can own profiles
    user = models.OneToOneField(User, blank=True, null=True)
