from rest_framework import generics
from pp5_api.permissions import IsOwnerOrReadOnly
from .serializers import ProfileSerializer
from .models import Profile


class ProfileList(generics.ListAPIView):
    """
    Lists all profiles.
    Don't need a permissions class as it is only listview
    since signals is used to create the profile
    """
    queryset = Profile.objects.all().order_by('-created_at')
    serializer_class = ProfileSerializer
    search_fields = ['name']


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Allows the profileowner to edit their profile
    """
    queryset = Profile.objects.all().order_by('-created_at')
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
