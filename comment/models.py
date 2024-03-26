from django.db import models
from car.models import CarModel;

# Create your models here.
class CommentModel(models.Model) :
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="comments");
    name = models.CharField(max_length = 30);
    comment = models.CharField(max_length = 150);
    createdAt = models.DateTimeField(auto_now_add = True);