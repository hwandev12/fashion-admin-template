from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
class Lead(models.Model):
    
    class Meta:
        verbose_name = "Lead"
        verbose_name_plural = "My Leads"
         
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0) 
