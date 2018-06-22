from django.db import models
from django.utils import timezone

# Create your models here.
class Column(models.Model):#后台编辑
    title = models.CharField(max_length=50, default="未命名")
    content = models.TextField(default="文档待编辑...")#点击后才会显示

    tag = models.CharField(max_length=50, default="美白")

    likenum = models.IntegerField(default=0)
    dislikenum = models.IntegerField(default=0)
    username = models.CharField(max_length=30, default='user')
    nickname = models.CharField(max_length=30, default='匿名')
    userphoto = models.ImageField(default='q1.png')
    photo1 = models.ImageField(default='q1.png')

    def __str__(self):
        return self.title

class Like(models.Model):#点赞名单
    columnId = models.IntegerField(default=0)#id是从1开始的
    title = models.CharField(max_length=50, default="未命名")
    username = models.CharField(max_length=30, default='user')#发表文章用户
    likeuser = models.CharField(max_length=30, default='user')#点赞用户

    def __str__(self):
        return self.title

class Dislike(models.Model):#收藏名单
    columnId = models.IntegerField(default=0)#id是从1开始的
    title = models.CharField(max_length=50, default="未命名")
    username = models.CharField(max_length=30, default='user')#发表文章用户
    dislikeuser = models.CharField(max_length=30, default='user')#收藏文章用户

    def __str__(self):
        return self.title
# Create your models here.
