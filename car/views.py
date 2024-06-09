from django.shortcuts import render,get_object_or_404
from .models import Car
from django.core.paginator import Paginator,EmptyPage
# Create your views here.
def cars(request):
    cars=Car.objects.order_by('created_date')
    paginator=Paginator(cars,1)
    page=request.GET.get('page')
    paged_cars=paginator.get_page(page)

    data={
    'cars':paged_cars,

    }
    return render(request,'cars/cars.html',data)

def car_detail(request,id):
    single_car=get_object_or_404(Car,pk=id)
    data={'single_car':single_car,}
    return render(request,'cars/car_detail.html',data)





def search(request):
    cars=Car.objects.order_by('-created_date')
    search_model=Car.objects.values_list('model',flat=True).distinct()
    search_city=Car.objects.values_list('city',flat=True).distinct()
    search_year=Car.objects.values_list('year',flat=True).distinct()
    search_condition=Car.objects.values_list('condition',flat=True).distinct()
    search_transmission=Car.objects.values_list('transmission',flat=True).distinct()

    if 'f' in request.GET:
        f=request.GET['f']
        if f:
            cars=cars.filter(fuel_type__iexact=f)
    if 'model' in request.GET:
        model=request.GET['model']
        if model:
            cars=cars.filter(model__icontains=model)
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            cars=cars.filter(description__icontains=keyword)
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            cars=cars.filter(city__icontains=city)
    if 'y' in request.GET:
        y=request.GET['y']
        if y:
            cars=cars.filter(year__iexact=y)
    if 'min_price' in request.GET:
        min_price=request.GET['min_price']
        max_price=request.GET['max_price']
        if max_price:
            cars=cars.filter(price__gte=min_price,price__lte=max_price)
    data={
    'cars':cars,
    'search_model':search_model,
    'search_city':search_city,
    'search_year':search_year,
    'search_condition':search_condition,
    'search_transmission':search_transmission,
    }
    return render(request,'cars/search.html',data)
