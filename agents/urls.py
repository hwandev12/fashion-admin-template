from django.urls import path
from .views import *

app_name = 'agents'

urlpatterns = [
    path('', AgentListView.as_view(), name='agent-list'),
    path("<int:pk>/", AgentDetailView.as_view(), name='agent-info'),
    path("<int:pk>/update/", AgentUpdateView.as_view(), name='update-agent'),
    path("<int:pk>/delete/", AgentDeleteView.as_view(), name='delete-agent'),
    path('agents-create/', AgentCreateView.as_view(), name='agent-create')
]