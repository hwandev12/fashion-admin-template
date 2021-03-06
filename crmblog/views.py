from multiprocessing import context
from re import template
from django.shortcuts import render, redirect, reverse
from .forms import *
from .models import Lead, Spy, Category
from agents.mixins import OrganiserAndLoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from . import models
from django.shortcuts import get_object_or_404, render


class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = RegisterForm

    def get_success_url(self):
        return reverse('lead:leads')


class HomeView(TemplateView):
    template_name = 'base.html'


class Leads(LoginRequiredMixin, ListView):
    template_name = 'leads_info.html'
    context_object_name = 'leads'

    def get_queryset(self):
        user = self.request.user
        if user.is_organised:
            queryset = models.Lead.objects.filter(organiser=user.userprofile)
        else:
            queryset = models.Lead.objects.filter(organiser=user.spy.organiser)
            queryset = queryset.filter(spy__user=self.request.user)
        return queryset

    # Bu yerda aniqlanmagan agent uchun funksiya yozilgan
    def get_context_data(self, **kwargs):  # Eslab qolish
        context = super(Leads, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organised:
            queryset = Lead.objects.filter(
                organiser=user.userprofile,
                spy__isnull=True
            )
            context.update({
                'unassigned_leads': queryset
            })
            return context
    # Bu yerda aniqlanmagan agent uchun funksiya yozilgan


class DetailsLead(OrganiserAndLoginRequiredMixin, DetailView):
    template_name = 'details.html'
    context_object_name = 'lead'
    queryset = Lead.objects.all()


class CreateLead(OrganiserAndLoginRequiredMixin, CreateView):
    template_name = 'create.html'
    form_class = LeadForm

    def get_success_url(self):
        return reverse('lead:leads')

    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.organiser = self.request.user.userprofile
        lead.save()
        return super(CreateLead, self).form_valid(form)


class UpdateLead(OrganiserAndLoginRequiredMixin, UpdateView):
    template_name = 'update.html'
    form_class = LeadForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('lead:leads')


class DeleteLead(OrganiserAndLoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('lead:leads')

# Agenti aniqlanmagan user lar uchun class based view


class AgentAssignView(OrganiserAndLoginRequiredMixin, FormView):
    template_name = 'assign_agent.html'
    form_class = AgentAssignForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AgentAssignView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            'request': self.request
        })
        return kwargs

    def get_success_url(self):
        return reverse('lead:leads')

    def form_valid(self, form):
        spy = form.cleaned_data['agent']
        lead = Lead.objects.get(id=self.kwargs['pk'])
        lead.spy = spy
        lead.save()
        return super(AgentAssignView, self).form_valid(form)
    # Agenti aniqlanmagan user lar uchun class based view


class CategoryAssignView(LoginRequiredMixin, ListView):
    template_name = 'category.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):  # Eslab qolish
        context = super(CategoryAssignView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organised:
            queryset = Lead.objects.filter(
                organiser=user.userprofile
            )
        else:
            queryset = Category.objects.filter(
                organiser=user.spy.organiser)
        context.update({
            'unassigned_category_quantity': queryset.filter(category__isnull=True).count()
        })
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_organised:
            queryset = Category.objects.filter(
                organiser=user.userprofile)
        else:
            queryset = Category.objects.filter(
                organiser=user.spy.organiser)
        return queryset


class AssignCategoryDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'category_detail.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_organised:
            queryset = Category.objects.filter(
                organiser=user.userprofile)
        else:
            queryset = Category.objects.filter(
                organiser=user.spy.organiser)
        return queryset


class LeadCategoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'category_update.html'
    form_class = LeadCategoryUpdateForm

    def get_queryset(self):
        user = self.request.user
        if user.is_organised:
            queryset = Lead.objects.filter(
                organiser=user.userprofile)
        else:
            queryset = Lead.objects.filter(
                organiser=user.spy.organiser)
        return queryset

    def get_success_url(self):
        return reverse('lead:leads')
