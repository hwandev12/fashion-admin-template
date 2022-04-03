from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Lead
from . import models
from django.shortcuts import get_object_or_404
from .forms import *


def home(request):
    return render(request, "base.html")


def leads_info(request):
    leads = Lead.objects.all()
    context = {"leads": leads}
    return render(request, "leads_info.html", context)


def details_lead(request, pk):
    lead = get_object_or_404(models.Lead, id=pk)
    context = {"lead": lead}
    return render(request, "details.html", context)


def create_lead(request):
    form = Lead_form()
    if request.method == "POST":
        form = Lead_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            last_name = form.cleaned_data["last_name"]
            age = form.cleaned_data["age"]
            email = form.cleaned_data["email"]
            spy = models.Spy.objects.first()
            models.Lead.objects.create(
                name=name, last_name=last_name, email=email, age=age, spy=spy
            )
            return redirect("/")
    context = {"form": form}
    return render(request, "create.html", context)

def update_lead(request, pk):
    form = Lead.objects.get(id=pk)
    context = {
        "form": form
    }
    return render(request, 'update.html', context)
