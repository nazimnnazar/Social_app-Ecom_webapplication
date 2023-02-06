from django.contrib import admin
from . models import*
# Register your models here.

class catgadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']
admin.site.register(Category,catgadmin)

class prodAdmin(admin.ModelAdmin):
    list_display=['name','price','img']
    list_editable=['price','img',]
    prepopulated_fields={'slug':('name',)}
admin.site.register(Products,prodAdmin)