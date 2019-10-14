from django.db.models.signals import post_save

# user will the sender of the signal
from django.contrib.auth.models import User

#import a receiver of the signal
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    '''
    post_save:is the signal that is fired after and objecte is saved

    User:model is the sender of the signal

    receiver:is the create profile function that fetches the signal and performs some task

    instance:is the instance of User class

    created : if user was created

    Profile.objects.create(user=instance):create a profile obj with the instance of the user that was created

    '''
    if created:
    Profile.objects.create(user=instance)

