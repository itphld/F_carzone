from django.contrib import admin
from .models import Team,Employee
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width=40 style="border-radius:50%">'.format(object.photo.url))
    list_display=('id','thumbnail','first_name','last_name','designation','created_date','photo')
    list_filter=('designation','first_name')
    thumbnail.short_description='Employee Photo'
    list_display_links=('first_name','last_name','thumbnail')
    search_fields=('first_name','last_name','designation')

class EmployeeAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width=40 style="border-radius:50%">'.format(object.photo.url))
    list_display=('thumbnail','first_name','last_name','email')
    list_display_links=('first_name','thumbnail','last_name')
    thumbnail.short_description='Profile Photo'
    list_filter=('first_name','designation')
    search_fields=('last_name','first_name')


admin.site.register(Team,TeamAdmin)
admin.site.register(Employee,EmployeeAdmin)
