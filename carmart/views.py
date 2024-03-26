from django.shortcuts import render
from brand.models import BrandModel
from car.models import CarModel

# Create your views here.
def index(request, id = None) :
    brands = BrandModel.objects.all();
    cars = CarModel.objects.all();
    if id is not None :
        brand = BrandModel.objects.get(id = id)
        cars = CarModel.objects.filter(brand = brand)
    
    return render(request, 'index.html', {'brands' : brands, 'cars' : cars, 'total': len(cars) })