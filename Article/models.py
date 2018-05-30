from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50, default="未命名")
    content = models.TextField(default="文档待编辑...")#点击后才会显示
    likenum = models.IntegerField(default=0)
    collectnum = models.IntegerField(default=0)
    username = models.CharField(max_length=30, default='user')
    nickname = models.CharField(max_length=30, default='匿名')
    userphoto = models.ImageField(upload_to="imgs", default='images/q1.png')
    photo1 = models.ImageField(upload_to='imgs', default='images/q1.png')
    photo2 = models.ImageField(upload_to='imgs', default='images/q1.png')
    photo3 = models.ImageField(upload_to='imgs', default='images/q1.png')




