from django.db import models

# Create your models here.

class Appartments(models.Model):
    roomSize = models.IntegerField(max_length=4)
    noOfWindows = models.IntegerField(max_length=3)
    isMetro = models.BooleanField(default=False)

class Employee(models.Model):
    Name = models.TextField(max_length=20)
    EmpID = models.TextField(max_length=10)
    Domine =models.TextField(max_length=20)