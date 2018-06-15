# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    nickname = models.CharField(max_length=30, default="匿名用户")
    userphoto = models.ImageField(upload_to='imgs', default='images/q1.png')
    # img = models.ImageField(upload_to='img')

    def __str__(self):
        return self.username


class Follow(models.Model):
    username = models.CharField(max_length=30)#关注的人
    nickname = models.CharField(max_length=30, default="匿名用户")
    userphoto = models.ImageField(upload_to='imgs', default='images/q1.png')
    followusername = models.CharField(max_length=30)#自己
    # img = models.ImageField(upload_to='img')

    def __str__(self):
        return self.username