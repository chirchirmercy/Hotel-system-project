from django.contrib import admin

# Register your models here.
from .models import Amenity
class AmenityAdmin(admin.ModelAdmin):
    list_display=["name"]
admin.site.register(Amenity,AmenityAdmin) 
