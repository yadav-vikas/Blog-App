from django.db.models.signals import post_save # this object is instantiated when an object is saved (signal gets fired)
from django.contrib.auth.models import User # signal sender
from django.dispatch import  receiver # signal receiver
from .models import Profile

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    """[Creating a user profile for each new User]
        ---- When a user is created post_save signal is generated and it is 
        received by the @receiver then execute function 'create_profile'
        inside the create_profile function >>> if the user is created then create a profile object with user=instance of the user created
    Args:
        sender ([type]): [description]
        instance ([type]): [description]
        created ([type]): [description]
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    """every time a user profile is created it saved that user profile
    Args:
        sender ([type]): [description]
        instance ([type]): [description]
        created ([type]): [description]
    """
    instance.profile.save()