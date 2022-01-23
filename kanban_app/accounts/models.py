from django.db import models
from django.contrib.auth.models import AbstractUser


#user model

class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        )
        
class Profile(models.Model):
    full_name = models.CharField(max_length=200, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
   

    def __str__(self):
        return f"{self.full_name} Profile"
