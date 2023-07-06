from django.db import models

# Create your models here.
class Userprofile(models.Model):
    name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=20)
    adress=models.CharField(max_length=200)