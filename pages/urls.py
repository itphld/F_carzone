from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),

    #path('<int:id>',views.car_deatil,name='car_detail'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    ]
