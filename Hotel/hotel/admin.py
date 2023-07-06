from django.contrib import admin

# Register your models here.
from .models import Hotel
class HotelAdmin(admin.ModelAdmin):
    list_display=("name","location","description","image")
admin.site.register(Hotel,HotelAdmin)    







 
