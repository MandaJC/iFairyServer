from rest_framework import serializers
from .models import Article, Collect, Comment


class ArticleSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(max_length=30, default='')
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'tag', 'tag2', 'tag3', 'relative', 'likenum', 'collectnum', 'username', 'nickname','userphoto', 'photo1', 'photo2', 'photo3', 'createdate')

    def update(self, instance, validated_data):
        instance.nickname = validated_data


class CollectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collect
        fields = ('id', 'collectuser')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','articleId','comment','commentuser','userphoto','nickname','createdate')