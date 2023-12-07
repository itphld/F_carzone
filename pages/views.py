from django.shortcuts import render
from .models import Team

# Create your views here.
def home(request):
    teams=Team.objects.all()
    asd={'teams':teams}
    return render(request,'pages/home.html',asd)
def about(request):
    return render(request,'pages/about.html')
def cars(request):
    return render(request,'pages/cars.html')
def services(request):
    return render(request,'pages/services.html')
def contact(request):
    return render(request,'pages/contact.html')
