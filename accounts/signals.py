from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile


@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print('User Profile is Created')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except BaseException:
            UserProfile.objects.create(user=instance)
            print('Profile Did not exist, so a new profile is created')


# Approach 1
# post_save.connect(post_save_create_profile_receiver, sender=User)


@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    print(f'{instance.username} -> pre_save Signal is Called')
