from django.db import models

# Create your models here.
class Reservation(models.Model):
    check_in=models.DateField()
    check_out=models.DateField()
    total_price=models.DecimalField(max_digits=8,decimal_places=2)
    status=models.CharField(max_length=10)








