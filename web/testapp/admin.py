from django.contrib import admin
from testapp.models import Empmodel
# Register your models here.
class Empadmin(admin.ModelAdmin):
    list_display=['name','type','date']
admin.site.register(Empmodel,Empadmin)
