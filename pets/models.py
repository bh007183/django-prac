from tkinter import CASCADE
from django.conf import settings
from django.db import models
 

# Create your models here.
class UserProfile(models.Model):
    phone_number = models.CharField(max_length=255)
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='user_id', null=True)

class Pet(models.Model):
    species = models.CharField(max_length=255)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

