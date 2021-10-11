from .models import Profile,User,Avatar
from django.dispatch import receiver
from django.db.models.signals import post_save



def update_user_profile(sender, instance, created, **kwargs):
    """
    Signals the Profile about User creation.
    """
    if not Profile.objects.filter(user=instance).exists():
        Profile.objects.create(user=instance)
    if not Avatar.objects.filter(profile=Profile.objects.get(user=instance)).exists():
        Avatar.objects.create(profile=Profile.objects.get(user=instance))

    instance.profile.save()

post_save.connect(update_user_profile,sender=User)


