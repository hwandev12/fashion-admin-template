from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
    is_organised = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)


class Lead(models.Model):
    class Meta:
        verbose_name = "Lead"
        verbose_name_plural = "Fashion Leads"

    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    organiser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    spy = models.ForeignKey("Spy", null=True, blank=True,
                            on_delete=models.SET_NULL)
    category = models.ForeignKey(
        'Category', blank=True, related_name='leads', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Main Category Model'
    category_name = models.CharField(max_length=30)
    organiser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_name


class Spy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organiser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


def create_post_save(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_post_save, sender=User)
