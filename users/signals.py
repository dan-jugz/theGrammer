from django.db.models.signals import post_save

# user will the sender of the signal
from django.contrib.auth.models import User

#import a receiver of the signal
from django.dispatch import receiver

from .models import Profile



