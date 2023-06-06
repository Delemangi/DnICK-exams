from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class Balloon(models.Model):
    type = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    max_passengers = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.manufacturer} {self.type}"


class Pilot(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    hours = models.PositiveIntegerField()
    role = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Airline(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    outside = models.BooleanField()
    user = models.ForeignKey(to=User, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Flight(models.Model):
    code = models.CharField(max_length=50)
    airport_from = models.CharField(max_length=50)
    airport_to = models.CharField(max_length=50)
    user = models.ForeignKey(to=User, on_delete=CASCADE)
    image = models.ImageField(upload_to="flights/")
    balloon = models.ForeignKey(to=Balloon, on_delete=CASCADE)
    pilot = models.ForeignKey(to=Pilot, on_delete=CASCADE)
    airline = models.ForeignKey(to=Airline, on_delete=CASCADE)

    def __str__(self):
        return self.code


class Collaboration(models.Model):
    airline = models.ForeignKey(to=Airline, on_delete=CASCADE)
    pilot = models.ForeignKey(to=Pilot, on_delete=CASCADE)

    def __str__(self):
        return f"{self.airline} - {self.pilot}"
