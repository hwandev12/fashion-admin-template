import random
from django.shortcuts import render
from django.core.mail import send_mail
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import OrganiserAndLoginRequiredMixin
from crmblog.models import Spy
from .forms import AgentCreateModel


class AgentListView(OrganiserAndLoginRequiredMixin, generic.ListView):
    template_name = 'agents/lists.html'

    def get_queryset(self):
        organiser = self.request.user.userprofile
        return Spy.objects.filter(organiser=organiser)


class AgentCreateView(OrganiserAndLoginRequiredMixin, generic.CreateView):
    template_name = 'agents/create.html'
    form_class = AgentCreateModel

    def get_success_url(self):
        return reverse('agents:agent-list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_organised = self.request.user.userprofile
        user.save()
        user.set_password(f"{random.randint(0, 10000)}")
        user.save()
        Spy.objects.create(
            user=user,
            organiser=self.request.user.userprofile
        )
        send_mail(
            subject='Agent has been created',
            message='Your New Agent has been created',
            from_email='guli@gmail.com',
            recipient_list=[user.email],
        )
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(OrganiserAndLoginRequiredMixin, generic.DetailView):
    template_name = 'agents/details.html'
    context_object_name = 'agents'

    def get_queryset(self):
        organiser = self.request.user.userprofile
        return Spy.objects.filter(organiser=organiser)


class AgentUpdateView(OrganiserAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/update.html'
    form_class = AgentCreateModel

    def get_success_url(self):
        return reverse('agents:agent-list')

    def get_queryset(self):
        organiser = self.request.user.userprofile
        return Spy.objects.filter(organiser=organiser)


class AgentDeleteView(OrganiserAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/delete.html'
    context_object_name = 'agent'

    def get_success_url(self):
        return reverse('agents:agent-list')

    def get_queryset(self):
        organiser = self.request.user.userprofile
        return Spy.objects.filter(organiser=organiser)
