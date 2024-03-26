from django.shortcuts import render, redirect;
from django.views.generic import DetailView, UpdateView;
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from . import models;

# Create your views here.
class CarDetailView(DetailView) :
    model = models.CarModel;
    pk_url_kwarg = 'pk';
    template_name = 'carDetail.html';
    context_object_name = 'car'

@method_decorator(require_POST, name='dispatch')
class CarStockUpdateView(DetailView):
    model = models.CarModel

    def post(self, request, *args, **kwargs):
        car = self.get_object()
        car.stock -= 1
        car.save()
        return redirect('detailPage', pk=car.pk)