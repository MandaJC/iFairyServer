# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from regNlog.models import Person
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.base import ContentFile
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
#注册
def register(request):
    request.encoding = 'utf-8'
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        person = Person.objects.get(username=username)
    except ObjectDoesNotExist:
        Person.objects.create(username=username, password=password)
        return HttpResponse("注册成功")
    else:
        return HttpResponse("用户名重复")

#登录
def login(request):
    request.encoding = 'utf-8'
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        person = Person.objects.get(username=username)
    except ObjectDoesNotExist:
        return HttpResponse("用户不存在")
    else:
        if person.password == password:
            return HttpResponse("登录成功")
        else:
            return HttpResponse("登录失败")

