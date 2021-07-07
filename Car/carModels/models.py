from django.db import models

# Create your models here.


class Car(models.Model):
    name= models.CharField(max_length=50)
    type= models.CharField(max_length=50)
    created= models.DateField

    def __str__(self):
        return self.name 

