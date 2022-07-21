from rest_framework import serializers
from .models import Post
from likes.models import Like


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()

    def validate_image(self, image):
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
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'like_id',
            'likes_count', 'tags'
        ]
