from django.db import models
from django.contrib.auth.models import AbstractUser
from user_model.manager import Custommanager
# Create your models here.
class Customuser(AbstractUser):
    phone_number = models.CharField(unique=True,max_length=100)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(choices = (('Male','Male'),('Female','Female')),default="Male",max_length=100)
      
    profile_picture = models.ImageField(upload_to="profile/images/")

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = Custommanager()

    