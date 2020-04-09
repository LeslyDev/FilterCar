from django.db import models

# Create your models here.


class Car(models.Model):
    manufacturer = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    kpp = models.CharField(max_length=255)
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.model
