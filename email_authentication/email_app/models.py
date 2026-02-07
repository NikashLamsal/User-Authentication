from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(User):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
            
            return self.email