from django.db import models

# Create your models here.
class Room(models.Model):
    room_number=models.CharField(max_length=100)
    capacity=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
