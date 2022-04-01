from django.shortcuts import render
from .models import Lead
from . import models
from django.shortcuts import get_object_or_404


def leads_info(request):
    leads = Lead.objects.all()
    context = {"leads": leads}
    return render(request, "leads_info.html", context)

def details_lead(request, pk):
    lead = get_object_or_404(models.Lead, id=pk)
    return render(request, 'details.html')
