from rest_framework import generics, permissions
from pp5_api.permissions import IsOwnerOrReadOnly
from .serializers import LikeSerializer
from .models import Like


class LikeList(generics.ListCreateAPIView):
    """
    User can create a like for a post
    """
    queryset = Like.objects.all().order_by('-created_at')
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Provides the user ability to remove a like from a post
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
