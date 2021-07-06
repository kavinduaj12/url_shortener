from django.contrib import admin
from .models import UrlData

# Register your models here.

@admin.register(UrlData)
class UrlDataAdmin(admin.ModelAdmin):
    list_display=['id','url','slug']