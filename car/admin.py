from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width=50 style="border-radius:50%">'.format(object.car_photo.url))


    list_display=('id','thumbnail','car_title','model','engine','is_featured')
    list_display_links=('id','thumbnail','car_title','model','engine')
    list_filter=('car_title','engine')
    search_fields=('car_title','engine')


admin.site.register(Car,CarAdmin)
