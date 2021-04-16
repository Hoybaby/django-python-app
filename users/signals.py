# this is a signal that gets fired when an object is fired
from django.db.models.signals import post_save

# this is the sender
from django.contrib.auth.models import User

# this is the reciverver
from django.dispatch import receiver

from .models import Profile

# we want a user profile to be created for each new user.

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
        