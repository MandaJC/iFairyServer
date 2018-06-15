from rest_framework import serializers
from .models import Column


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ('id', 'title', 'content', 'tag', 'likenum', 'dislikenum', 'username', 'nickname','userphoto', 'photo1')



