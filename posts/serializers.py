from rest_framework import serializers
from likes.models import Like
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Translates the Post models values to JSON
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()

    def validate_image(self, image):
        """
        validates images by filesize in megabytes
        as well as width and height in pixels
        """
        if image.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                "Image size is too large, maximum size allowed is 2MB"
                )
        if image.image.height > 4096:
            raise serializers.ValidationError(
                'Images with a height larger than 4096 pixels are not allowed!'
            )
        if image.image.width > 4096:
            raise serializers.ValidationError(
                'Images with a width larger than 4096 pixels are not allowed!'
            )

    def get_is_owner(self, obj):
        """
        Retrieves the owner of the object
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Checks if user has liked a post by
        looking up if user has a like id in the model
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        """
        Defines the fields the API will list
        """
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'like_id',
            'likes_count', 'tags'
        ]
