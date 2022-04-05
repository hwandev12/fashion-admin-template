from os import name
from django.contrib import admin
from django.urls import path, include
from crmblog.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('', include('crmblog.urls')),
]
