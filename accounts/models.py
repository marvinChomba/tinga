from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    pic = models.ImageField(blank=True)

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if(created):
            Profile.objects.creare(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
        instance.profile.save()
