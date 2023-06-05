from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    active = models.BooleanField()

    def __str__(self):
        return self.name


class Food(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    category = models.ForeignKey(to=Category, on_delete=CASCADE)
    author = models.ForeignKey(to=User, on_delete=CASCADE)
    image = models.ImageField(upload_to="foods/")
    price = models.FloatField()
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.code})"


class Client(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Sale(models.Model):
    date = models.DateField()
    client = models.ForeignKey(to=Client, on_delete=CASCADE)

    def __str__(self):
        return f"{self.date} - {self.client}"


class ProductSale(models.Model):
    product = models.ForeignKey(to=Food, on_delete=CASCADE)
    quantity = models.PositiveIntegerField()
    sale = models.ForeignKey(to=Sale, on_delete=CASCADE)

    def __str__(self):
        return f"{self.product} ({self.quantity})"
