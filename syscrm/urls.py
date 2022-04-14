from os import name
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import(
     LoginView,
     LogoutView,
     PasswordResetView,
     PasswordResetDoneView
)
from crmblog.views import HomeView, SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('password-reset-view/', PasswordResetView.as_view(), name='password_reset_view'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('', include('crmblog.urls')),
    path('agents/', include('agents.urls')),
]
