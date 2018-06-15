from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'tag', 'tag2', 'tag3', 'relative', 'likenum', 'collectnum', 'username', 'nickname','userphoto', 'photo1', 'photo2', 'photo3', 'createdate')
    # title = serializers.CharField(max_length=50, default="未命名")
    # content = serializers.Text(default="文档待编辑...")  # 点击后才会显示
    # likenum = serializers.IntegerField(default=0)
    # collectnum = serializers.IntegerField(default=0)
    # username = serializers.CharField(max_length=30)
    # userphoto = serializers.ImageField(upload_to="imgs")
    # photo1 = serializers.ImageField(upload_to='imgs')
    # photo2 = serializers.ImageField(upload_to='imgs')
    # photo3 = serializers.ImageField(upload_to='imgs')
    #
    #
    #
    # def create(self, validated_data):
    #     title = validated_data['title']
    #     content = validated_data['content']
    #     username = validated_data['username']
    #     userphoto = validated_data['userphoto']
    #     photo1 = validated_data['photo1']
    #     photo2 = validated_data['photo2']
    #     photo3 = validated_data['photo3']
    #     article = Article(title=title, content=content, username=username, userphoto=userphoto, photo1=photo1, photo2=photo2, photo3=photo3)
    #     article.save()
    #     return article
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.likenum = validated_data.get('likenum', instance.likenum)
    #     instance.collectnum = validated_data.get('collectnum', instance.collectnum)
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.userphoto = validated_data.get('userphoto', instance.userphoto)
    #     instance.photo1 = validated_data.get('photo1', instance.photo1)
    #     instance.photo2 = validated_data.get('photo2', instance.photo2)
    #     instance.photo3 = validated_data.get('photo3', instance.photo3)
    #     instance.save()
    #     return instance


