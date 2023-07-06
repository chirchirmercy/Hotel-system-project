from django.contrib import admin

# Register your models here.
from .models import Room
class RoomAdmin(admin.ModelAdmin):
    list_display=("room_number","capacity","price")
admin.site.register(Room,RoomAdmin)    






