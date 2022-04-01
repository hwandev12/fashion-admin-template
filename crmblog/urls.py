from django.urls import path
from .views import *

urlpatterns = [
    path("", leads_info, name="home"),
    path("<pk>/", details_lead)
]
