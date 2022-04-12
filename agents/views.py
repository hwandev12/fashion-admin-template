from re import template
from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from crmblog.models import Spy
from .forms import AgentCreateModel

class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = 'agents/lists.html'
    
    def get_queryset(self):
        organiser = self.request.user.userprofile
        return Spy.objects.filter(organiser=organiser)
    
class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'agents/create.html'
    form_class = AgentCreateModel
    
    def get_success_url(self):
        return reverse('agents:agent-list')
    
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.profile = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)
class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'agents/details.html'
    context_object_name = 'agents'
    
    def get_queryset(self):
        organiser = self.request.user.userprofile
        return Spy.objects.filter(organiser=organiser)
    
class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/update.html'
    form_class = AgentCreateModel
    
    def get_success_url(self):
        return reverse('agents:agent-list')
    
    def get_queryset(self):
        organiser = self.request.user.userprofile
        return Spy.objects.filter(organiser=organiser)
    
class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/delete.html'
    context_object_name = 'agent'
    
    def get_success_url(self):
        return reverse('agents:agent-list')
    
    def get_queryset(self):
        organiser = self.request.user.userprofile
        return Spy.objects.filter(organiser=organiser)
    


