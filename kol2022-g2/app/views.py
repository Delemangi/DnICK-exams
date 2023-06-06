from django.shortcuts import render, redirect
from . import forms
from . import models


def index(request):
    return render(request, "index.html")


def repairs(request):
    if request.method == "POST":
        form_data = forms.RepairForm(data=request.POST, files=request.FILES)

        if form_data.is_valid():
            repair = form_data.save(commit=False)
            repair.user = request.user
            repair.image = form_data.cleaned_data["image"]
            repair.save()
            return redirect("repairs")

    context = {
        "form": forms.RepairForm,
        "repairs": models.Repair.objects.filter(user=request.user, car__type="Sedan")
    }

    return render(request, "repairs.html", context)
