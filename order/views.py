from django.shortcuts import render
from django.views.generic import ListView;
from . import models;

# Create your views here.
class ListOrders(ListView) :
    template_name = '../authservice/templates/profile.html';
    model = models.OrderModel;
    context_object_name = 'orders'


def createOrder(request) :
    pass;