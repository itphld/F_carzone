from django.shortcuts import render
from .models import Team
from car.models import Car

# Create your views here.
def home(request):
    teams=Team.objects.all()
    featured_car=Car.objects.order_by('created_date').filter(is_featured=True)
    show_all=Car.objects.order_by('created_date').all()
    asd={'teams':teams,
        'featured_car':featured_car,
        'show_all':show_all,
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
