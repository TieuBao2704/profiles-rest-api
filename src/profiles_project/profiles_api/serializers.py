from rest_framework import serializers
from rest_framework.authtoken.models import Token

from . import models

class HelloSerializer(serializers.Serializer):
    """Sertializes a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)


class UserProfilesSerializer(serializers.ModelSerializer):
    """A serializer for our user profiles object."""

    class Meta:
        model = models.UserProfiles
        fields = ('id', 'email', 'name', 'password','token')
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfiles(
            email = validated_data['email'],
            name = validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class ProfileFeedItemViewSet(serializers.ModelSerializer):
    """A serializer for our profile feed item."""
    class Meta:
        model = models.ProfileFeedItems
        fields = ('id','user_profile','status_text','create_on')
        extra_kwargs = {'user_profile' :{'write_only':True}}
