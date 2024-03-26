from django.db import models
from django.contrib.auth.models import User;
from car.models import CarModel;

# Create your models here.
class OrderModel(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders");
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="order_cars");
    createdAt = models.DateTimeField(auto_now_add = True);