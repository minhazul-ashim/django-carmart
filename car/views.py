from django.shortcuts import render, redirect;
from django.views.generic import DetailView, UpdateView;
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from . import models;
from comment.forms import CommentForm;
from comment.models import CommentModel;
from order.models import OrderModel

# Create your views here.
class CarDetailView(DetailView) :
    model = models.CarModel;
    pk_url_kwarg = 'pk';
    template_name = 'carDetail.html';
    context_object_name = 'car';

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        context['comments'] = CommentModel.objects.all();
        return context;

@method_decorator(require_POST, name='dispatch')
class CarStockUpdateView(DetailView):
    model = models.CarModel
    def post(self, request, *args, **kwargs):
        car = self.get_object()
        car.stock -= 1
        car.save()

        user = request.user
        order = OrderModel.objects.create(user=user, car=car)
        return redirect('detailPage', pk=car.pk)