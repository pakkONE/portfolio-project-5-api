from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model that connects the user to the User model
    User also has choices for tagging their posts
    a default image has been provided to access image.url
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/post_images/',
        default='../k08ldncqhxfo8hbef3el',
        blank=True
        )

    FOOTBALL = 'FO'
    ICEHOCKEY = 'IH'
    GOLF = 'GO'
    TENNIS = 'TE'
    PADEL = 'PA'
    OTHER = 'OT'
    TAGS_CHOICES = [
        (FOOTBALL, 'Football'),
        (ICEHOCKEY, 'Ice Hcckey'),
        (GOLF, 'Golf'),
        (TENNIS, 'Tennis'),
        (PADEL, 'Padel'),
        (OTHER, 'Other'),
    ]
    tags = models.CharField(
        max_length=2,
        choices=TAGS_CHOICES,
        default=FOOTBALL,
    )

    class Meta:
        """
        Orders the posts by created date and latest first
        """
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.id} {self.title}"
