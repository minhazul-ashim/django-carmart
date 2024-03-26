from django.shortcuts import render
from brand.models import BrandModel
from car.models import CarModel

# Create your views here.
def index(request) :
    brands = BrandModel.objects.all();
    cars = CarModel.objects.all();
    
    return render(request, 'index.html', {'brands' : brands, 'cars' : cars, 'total': len(cars) })