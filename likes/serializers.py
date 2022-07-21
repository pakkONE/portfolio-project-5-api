from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    serializes the like model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """
        Defines which data to display to the API
        """
        model = Like
        fields = ['id', 'created_at', 'owner', 'post']

    def create(self, validated_data):
        """
        Method to make sure a user can not like a post
        that the user already has liked
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
