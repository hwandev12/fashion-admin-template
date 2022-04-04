from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Lead, Spy
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
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(request, "create.html", context)


def update_lead(request, pk):
    lead = models.Lead.objects.get(id=pk)
    form = LeadForm(instance=lead)
    if request.method == "POST":
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form, "lead": lead}
    return render(request, "update.html", context)

def delete_lead(request, pk):
    lead = models.Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/')
