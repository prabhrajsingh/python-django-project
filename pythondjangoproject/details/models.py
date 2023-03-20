from django.db import models

# Create your models here.
class enter_detail(models.Model):
    cylinders = models.IntegerField()
    displacement = models.IntegerField()
    horsepower = models.IntegerField()
    weight = models.IntegerField()
    acceleration =models.IntegerField()
    model = models.IntegerField()
    origin = models.IntegerField()
