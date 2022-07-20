from rest_framework import generics
from pp5_api.permissions import IsOwnerOrReadOnly
from .serializers import ProfileSerializer
from .models import Profile


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all().order_by('-created_at')
    serializer_class = ProfileSerializer
    search_fields = ['name']


class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all().order_by('-created_at')
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
