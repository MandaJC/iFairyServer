from rest_framework import serializers
from .models import Person, Follow


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'username', 'password', 'nickname', 'userphoto')

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ('id', 'username', 'nickname', 'userphoto', 'followusername')