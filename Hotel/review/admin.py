from django.contrib import admin

# Register your models here.
from .models import Review
class ReviewAdmin(admin.ModelAdmin):
    list_display=("rating","comment")
admin.site.register(Review,ReviewAdmin)    
