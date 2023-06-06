from django.shortcuts import render, redirect
from . import forms
from . import models


def index(request):
    return render(request, "index.html")


def flights(request):
    if request.method == "POST":
        form_data = forms.FlightForm(data=request.POST, files=request.FILES)

        if form_data.is_valid():
            flight = form_data.save(commit=False)
            flight.user = request.user
            flight.image = form_data.cleaned_data["image"]
            flight.save()
            return redirect("flights")

    context = {
        "flights": models.Flight.objects.filter(user=request.user, airport_from="Skopje").all(),
        "form": forms.FlightForm
    }

    return render(request, "flights.html", context)
