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
        return Spy.objects.all()
    
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
    


