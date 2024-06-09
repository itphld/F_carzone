from django.shortcuts import render
from .models import Team
from car.models import Car

# Create your views here.
def home(request):
    teams=Team.objects.all()
    featured_car=Car.objects.order_by('created_date').filter(is_featured=True)
    show_all=Car.objects.order_by('created_date').all()
    #search_fields=Car.objects.values('model','city','year','fuel_type','engine')
    search_model=Car.objects.values_list('model',flat=True).distinct()
    search_city=Car.objects.values_list('city',flat=True).distinct()
    search_year=Car.objects.values_list('year',flat=True).distinct()
    search_fuel=Car.objects.values_list('fuel_type',flat=True).distinct()
    search_engin=Car.objects.values_list('engine',flat=True).distinct()
    asd={'teams':teams,
        #'search_fields':search_fields,
        'featured_car':featured_car,
        'search_model':search_model,
        'search_city':search_city,
        'show_all':show_all,
        'search_year':search_year,
        'search_fuel':search_fuel,
        'search_engin':search_engin,
        }


    return render(request,'pages/home.html',asd)
def about(request):
    return render(request,'pages/about.html')
def cars(request):
    return render(request,'pages/cars.html')
def services(request):
    return render(request,'pages/services.html')
def contact(request):
    return render(request,'pages/contact.html')
