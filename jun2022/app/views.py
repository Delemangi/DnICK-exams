import string
import random
from django.shortcuts import render, redirect
from .forms import FoodForm
from .models import Food


def index(request):
    return render(request, "index.html")


def outofstock(request):
    context = {}

    if request.method == 'POST':
        form_data = FoodForm(data=request.POST, files=request.FILES)

        if form_data.is_valid():
            food = form_data.save(commit=False)
            food.author = request.user
            food.image = form_data.cleaned_data["image"]
            food.code = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
            food.save()
            return redirect("outofstock")

    context["foods"] = Food.objects.filter(amount=0, category__active=True)
    context["form"] = FoodForm

    return render(request, "outofstock.html", context)
