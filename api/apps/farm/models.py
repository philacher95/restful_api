from django.db import models


# Create your models here.

class Farm(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey('Farmer', blank=True, null=True, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f" {self.name} : {self.location}"


class Farmer(models.Model):
    Gender = [
        ('m', 'Male'),
        ('f', 'Female')
    ]
    name = models.CharField("Fullname", max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100, choices=Gender)

    def __str__(self):
        return f" {self.name} "
