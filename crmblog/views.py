from multiprocessing import context
from re import template
from django.shortcuts import render, redirect, reverse
from .models import Lead, Spy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from django.shortcuts import get_object_or_404, render
from .forms import *


class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = RegisterForm
    
    def get_success_url(self):
        return reverse('lead:leads')

class HomeView(TemplateView):
    template_name = 'base.html'


class Leads(LoginRequiredMixin, ListView):
    template_name = 'leads_info.html'
    queryset = models.Lead.objects.all()
    context_object_name = 'leads'


class DetailsLead(LoginRequiredMixin, DetailView):
    template_name = 'details.html'
    context_object_name = 'lead'
    queryset = models.Lead.objects.all()
    
class CreateLead(LoginRequiredMixin, CreateView):
    template_name = 'create.html'
    form_class = LeadForm
    
    def get_success_url(self):
        return reverse('lead:leads')
    
class UpdateLead(LoginRequiredMixin, UpdateView):
    template_name = 'update.html'
    form_class = LeadForm
    queryset = models.Lead.objects.all()
    
    def get_success_url(self):
        return reverse('lead:leads')

class DeleteLead(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    queryset = models.Lead.objects.all()
    
    def get_success_url(self):
        return reverse('lead:leads')
