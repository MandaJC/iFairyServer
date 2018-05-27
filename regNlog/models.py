# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    # img = models.ImageField(upload_to='img')

    # def __str__(self):
    #     return self.name
