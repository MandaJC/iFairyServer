from django.db import models
from django.utils import timezone
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50, default="未命名")
    content = models.TextField(default="文档待编辑...")#点击后才会显示

    tag = models.CharField(max_length=50, null=True, blank=True)
    tag2 = models.CharField(max_length=50, null=True, blank=True)
    tag3 = models.CharField(max_length=50, null=True, blank=True)
    relative = models.CharField(max_length=50, default="#")

    likenum = models.IntegerField(default=0)
    collectnum = models.IntegerField(default=0)

    username = models.CharField(max_length=30, default='user')
    nickname = models.CharField(max_length=30, default='匿名')

    userphoto = models.ImageField( default='q1.png')
    photo1 = models.ImageField(default='q1.png')
    photo2 = models.ImageField(default='q1.png')
    photo3 = models.ImageField(default='q1.png')
    createdate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-createdate']


class Like(models.Model):#点赞名单
    articleId = models.IntegerField(default=0)#id是从1开始的
    title = models.CharField(max_length=50, default="未命名")
    username = models.CharField(max_length=30, default='')#发表文章用户
    nickname = models.CharField(max_length=30, default='')
    likeuser = models.CharField(max_length=30, default='')#点赞用户

    def __str__(self):
        return self.title

class Collect(models.Model):#收藏名单 #没有头像
    #articleId = models.IntegerField(default=0)#id是从1开始的
    collectuser = models.CharField(max_length=30, default='')#收藏文章用户
    article=models.ManyToManyField(Article, related_name='collect_article')#反向查询

    def __str__(self):
        return self.collectuser

# class Collect(models.Model):#收藏名单 #没有头像
#     articleId = models.IntegerField(default=0)#id是从1开始的
#     title = models.CharField(max_length=50, default="未命名")
#     username = models.CharField(max_length=30, default='')#发表文章用户
#     nickname = models.CharField(max_length=30, default='')
#     collectuser = models.CharField(max_length=30, default='')#收藏文章用户
#
#     def __str__(self):
#         return self.title


class Comment(models.Model):
    articleId = models.IntegerField(default=0)  # id是从1开始的
    comment = models.TextField(default="评论待编辑...")#评论内容
    commentuser = models.CharField(max_length=30, default='user')#评论人名字

    createdate = models.DateTimeField(default=timezone.now)

    userphoto = models.ImageField(default='images/q1.png')#评论人头像
    nickname = models.CharField(max_length=30, default='匿名')#评论人昵称

    # title = models.CharField(max_length=50, default="未命名")
    # username = models.CharField(max_length=30, default='user')

    def __str__(self):
        return self.articleId