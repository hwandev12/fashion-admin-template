from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path("leads/", leads_info),
    path("<int:pk>/", details_lead),
    path("<int:pk>/update/", update_lead),
    path("create/", create_lead),
]
