# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    nickname = models.CharField(max_length=30, default="匿名用户")
    userphoto = models.ImageField(default='q1.png')
    follow = models.ManyToManyField('self', related_name='fans', symmetrical=False)#反向查询

    def __str__(self):
        return self.username


# class Follow(models.Model):
#     username = models.CharField(max_length=30)#关注的人
#     nickname = models.CharField(max_length=30, default="匿名用户")
#     userphoto = models.ImageField(upload_to='imgs', default='images/q1.png')
#     followusername = models.CharField(max_length=30)#自己
#     # person = models.ManyToManyField(Person, related_name='collect_article')
#     # img = models.ImageField(upload_to='imgs')
#
#     def __str__(self):
#         return self.username