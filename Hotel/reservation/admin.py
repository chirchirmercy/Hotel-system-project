from django.contrib import admin

# Register your models here.
from .models import Reservation
class ReservationAdmin(admin.ModelAdmin):
    list_display=("check_in","check_out","total_price","status")
admin.site.register(Reservation,ReservationAdmin)    

