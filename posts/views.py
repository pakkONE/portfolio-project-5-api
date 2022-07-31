from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from pp5_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    Lists posts and provides user to create post
    """
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True)
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'likes__owner__profile',
    ]
    search_fields = ['title', 'owner__username',]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Allowes the owner of a post to retrieve,
    update or delete the post
    """
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True)
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
