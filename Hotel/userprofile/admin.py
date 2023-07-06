from django.contrib import admin

# Register your models here.

from .models import Userprofile
class UserprofileAdmin(admin.ModelAdmin):
    list_display=("name","phone_number","adress")
admin.site.register(Userprofile,UserprofileAdmin)   