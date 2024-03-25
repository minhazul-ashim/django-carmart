from django.db import models
from brand.models import BrandModel;

# Create your models here.
class CarModel(models.Model) :
    name = models.CharField(max_length = 30);
    price = models.FloatField();
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE);
    description = models.CharField(max_length=500);
    stock = models.IntegerField();
    image = models.ImageField(upload_to='uploads/media/', blank=True, null=True);

    def __str__(self):
        return self.name;