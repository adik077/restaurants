from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(null=True, blank=True)
    phone_number = PhoneNumberField()
    notes = models.TextField(max_length=500, null=True,blank=True)

    def __str__(self):
        return self.name

class StoreCookies(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    cookies = models.CharField(max_length=10000)
