from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializes the comments to be readable in the API
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Method to tie the comment to the user who created it
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        """
        method to display the time from when the comment was created
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        method to display the time from when the comment was updated
        """
        return naturaltime(obj.updated_at)

    class Meta:
        """
        Defines which fields the API will display
        """
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'post', 'created_at',
            'updated_at', 'content',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializes the Comment Detail view
    """
    post = serializers.ReadOnlyField(source='post.id')
