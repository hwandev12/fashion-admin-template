from django.urls import path
from .views import *

urlpatterns = [
    path("", leads_info, name="home"),
    path("<int:pk>/", details_lead),
    path("create/", create_lead)
]
