from django.contrib import admin
from .models import Lead, User, Spy, UserProfile

admin.site.register(Lead)
admin.site.register(User)
admin.site.register(Spy)
admin.site.register(UserProfile)

