from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser



class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=400, blank=True, null=True)
    phone_number = models.CharField(max_length=15)  # New field for phone number
    ordersId=models.CharField(max_length=20,blank=True,null=True)
    def __str__(self):
        return self.user.username 
    


class AdditionalItem(models.Model):
    ordersId=models.IntegerField()

    



