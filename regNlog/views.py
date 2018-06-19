# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from regNlog.models import Person
from django.core.exceptions import ObjectDoesNotExist

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
from regNlog.serializers import PersonSerializer

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os

from Article.models import Article, Like, Comment, Collect
# Create your views here.
#注册
def register(request):
    request.encoding = 'utf-8'
    username = request.POST.get('username')
    nickname = request.POST.get('nickname')
    password = request.POST.get('password')
    try:
        person = Person.objects.get(username=username)
    except ObjectDoesNotExist:
        Person.objects.create(username=username, password=password, nickname=nickname)
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
            return HttpResponse("登录失败")#密码错误

# def getNickName(request):
#     request.encoding = 'utf-8'
#     username = request.POST.get('username')
#     try:
#         person = Person.objects.get(username=username)
#     except ObjectDoesNotExist:
#         return HttpResponse("用户不存在")
#     else:
#         return HttpResponse(person.nickname)

#
def changePassword(request):
    person = Person.objects.filter(username=request.POST.get('username')).update(password=request.POST.get('password'))
    return HttpResponse("密码修改成功")

def changeHeadImg(request):
    username=request.POST.get('username')
    userphoto = request.FILES.get('userphoto')
    path=default_storage.save('imgs/'+userphoto.name, ContentFile(userphoto.read()))
    tmp_file = os.path.join(settings.MEDIA_ROOT, path)
    person = Person.objects.filter(username=username).update(userphoto=path)
    Article.objects.filter(username=username).update(userphoto=userphoto)
    Comment.objects.filter(commentuser=username).update(userphoto=userphoto)
    # return HttpResponse(path)
    return HttpResponse("头像修改成功")

def changeNickName(request):
    username=request.POST.get('username')
    nickname=request.POST.get('nickname')
    Person.objects.filter(username=username).update(nickname=nickname)
    Article.objects.filter(username=username).update(nickname=nickname)
    Like.objects.filter(username=username).update(nickname=nickname)
    # Collect.objects.filter(username=username).update(nickname=nickname)
    Comment.objects.filter(commentuser=username).update(nickname=nickname)
    return HttpResponse("昵称修改成功")

class PersonList(APIView):
    def get(self, request, format=None):
        Persons = Person.objects.all()
        serializer = PersonSerializer(Persons, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # person = Person.objects.filter(username=request.POST.get('username')).update()
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
class PersonDetail(APIView):
    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Person = self.get_object(pk)
        serializer = PersonSerializer(Person)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        Person = self.get_object(pk)
        serializer = PersonSerializer(Person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Person = self.get_object(pk)
        Person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
