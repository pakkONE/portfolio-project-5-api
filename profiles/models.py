from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model that stores the data about
    each users profile
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../qhazlipjgyvtxieujxrx'
        )

    class Meta:
        """
        sorts the profiles by date created,
        with the latest one first
        """
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    signals to tie the profile to the user who created it
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
