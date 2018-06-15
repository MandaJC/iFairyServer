from Column.models import Column, Like, Dislike
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from rest_framework import generics
from .serializers import ColumnSerializer
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def isLike(request):#是否已赞
    columnId = int(request.POST.get('columnId'))
    print(columnId)
    title = request.POST.get('title')
    username = request.POST.get('username')
    likeuser = request.POST.get('likeuser')
    user = Like.objects.filter(columnId = columnId,likeuser=likeuser)
    if len(user)>0:
        return HttpResponse("已点赞")
    else:
        return HttpResponse("未点赞")

def isDislike(request):#是否已收藏
    columnId =int(request.POST.get('columnId'))
    title =request.POST.get('title')
    username =request.POST.get('username')
    dislikeuser =request.POST.get('dislikeuser')
    user = Dislike.objects.filter(columnId = columnId,dislikeuser=dislikeuser)
    if len(user)>0:
        return HttpResponse("已踩")
    else:
        return HttpResponse("未踩")

def setLike(request):#增加赞
    columnId = int(request.POST.get('columnId'))
    title = request.POST.get('title')
    username = request.POST.get('username')
    likeuser = request.POST.get('likeuser')
    user = Like.objects.filter(columnId=columnId, likeuser=likeuser)
    if len(user) == 0:#避免误增
        Like.objects.create(columnId=columnId, title=title, username=username, likeuser=likeuser)
        number = Column.objects.get(pk = columnId).likenum
        Column.objects.filter(pk = columnId).update(likenum=number+1)
    return HttpResponse("点赞成功")

def setDislike(request):#增加收藏
    columnId =int(request.POST.get('columnId'))
    title =request.POST.get('title')
    username =request.POST.get('username')
    dislikeuser =request.POST.get('dislikeuser')
    user = Dislike.objects.filter(columnId=columnId, dislikeuser=dislikeuser)
    if len(user) == 0:#避免误增
        Dislike.objects.create(columnId=columnId, title=title,username = username, dislikeuser=dislikeuser)
        number = Column.objects.get(pk = columnId).dislikenum
        Column.objects.filter(pk = columnId).update(dislikenum=number+1)
    return HttpResponse("踩成功")


class ColumnTagListId(APIView):
    def post(self, request, format=None):
        columns = Column.objects.filter(tag=request.POST.get('tag'))#.values('id')
        serializer = ColumnSerializer(columns, many=True)
        if(columns.count()==0):
            return HttpResponse("Tag不存在")
        return Response(serializer.data)

class ColumnList(APIView):
    def get(self, request, format=None):
        columns = Column.objects.all().order_by("-likenum")
        serializer = ColumnSerializer(columns, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ColumnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ColumnDetail(APIView):
    def get_object(self, pk):
        try:
            return Column.objects.get(pk=pk)
        except Column.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        column = self.get_object(pk)
        serializer = ColumnSerializer(column)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        column = self.get_object(pk)
        serializer = ColumnSerializer(column, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        column = self.get_object(pk)
        serializer = ColumnSerializer(column, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        column = self.get_object(pk)
        column.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)