from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    type = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(to=Manufacturer, on_delete=CASCADE)
    speed = models.PositiveIntegerField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.manufacturer} {self.type}"


class Workshop(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    old_timer = models.BooleanField()

    def __str__(self):
        return self.name


class Repair(models.Model):
    code = models.CharField(max_length=50)
    date = models.DateField()
    description = models.CharField(max_length=50)
    user = models.ForeignKey(to=User, on_delete=CASCADE)
    image = models.ImageField(upload_to="repairs/")
    car = models.ForeignKey(to=Car, on_delete=CASCADE)
    workshop = models.ForeignKey(to=Workshop, on_delete=CASCADE)

    def __str__(self):
        return self.code


class Specialization(models.Model):
    workshop = models.ForeignKey(to=Workshop, on_delete=CASCADE)
    manufacturer = models.ForeignKey(to=Manufacturer, on_delete=CASCADE)

    def __str__(self):
        return f"{self.workshop} - {self.manufacturer}"
