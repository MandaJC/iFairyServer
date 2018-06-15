from django.db import models
from django.utils import timezone
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50, default="未命名")
    content = models.TextField(default="文档待编辑...")#点击后才会显示

    tag = models.CharField(max_length=50, default="mandajc￥")
    tag2 = models.CharField(max_length=50, default="mandajc￥")
    tag3 = models.CharField(max_length=50, default="mandajc￥")
    relative = models.CharField(max_length=50, default="#")

    likenum = models.IntegerField(default=0)
    collectnum = models.IntegerField(default=0)

    username = models.CharField(max_length=30, default='user')
    nickname = models.CharField(max_length=30, default='匿名')

    userphoto = models.ImageField(upload_to="imgs", default='images/q1.png')
    photo1 = models.ImageField(upload_to='imgs', default='images/q1.png')
    photo2 = models.ImageField(upload_to='imgs', default='images/q1.png')
    photo3 = models.ImageField(upload_to='imgs', default='images/q1.png')
    createdate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Like(models.Model):#点赞名单
    articleId = models.IntegerField(default=0)#id是从1开始的
    title = models.CharField(max_length=50, default="未命名")
    username = models.CharField(max_length=30, default='user')#发表文章用户
    likeuser = models.CharField(max_length=30, default='user')#点赞用户

    def __str__(self):
        return self.title

class Collect(models.Model):#收藏名单
    articleId = models.IntegerField(default=0)#id是从1开始的
    title = models.CharField(max_length=50, default="未命名")
    username = models.CharField(max_length=30, default='user')#发表文章用户
    collectuser = models.CharField(max_length=30, default='user')#收藏文章用户

    def __str__(self):
        return self.title
