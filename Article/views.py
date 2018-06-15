from Article.models import Article, Like, Collect
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from rest_framework import generics
from .serializers import ArticleSerializer
from django.core.exceptions import ObjectDoesNotExist

# class PartyList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
# class PartyDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# def changeHeadImg(request):
    # article = Article.objects.filter(username=request.POST.get('username')).update(userphoto=request.FILES.get('userphoto'))
    # return HttpResponse("头像修改成功")

# def changeNickName(request):
    # article = Article.objects.filter(username=request.POST.get('username')).update(nickname=request.POST.get('nickname'))
    # return HttpResponse("昵称修改成功")

def isLike(request):#是否已赞
    articleId = int(request.POST.get('articleId'))
    print(articleId)
    title = request.POST.get('title')
    username = request.POST.get('username')
    likeuser = request.POST.get('likeuser')
    user = Like.objects.filter(articleId = articleId,likeuser=likeuser)
    if len(user)>0:
        return HttpResponse("已点赞")
    else:
        return HttpResponse("未点赞")

def isCollect(request):#是否已收藏
    articleId =int(request.POST.get('articleId'))
    title =request.POST.get('title')
    username =request.POST.get('username')
    collectuser =request.POST.get('collectuser')
    user = Collect.objects.filter(articleId = articleId,collectuser=collectuser)
    if len(user)>0:
        return HttpResponse("已收藏")
    else:
        return HttpResponse("未收藏")

def setLike(request):#增加赞
    articleId = int(request.POST.get('articleId'))
    title = request.POST.get('title')
    username = request.POST.get('username')
    likeuser = request.POST.get('likeuser')
    user = Like.objects.filter(articleId=articleId, likeuser=likeuser)
    if len(user) == 0:#避免误增
        Like.objects.create(articleId=articleId, title=title, username=username, likeuser=likeuser)
        number = Article.objects.get(pk = articleId).likenum
        Article.objects.filter(pk = articleId).update(likenum=number+1)
    return HttpResponse("点赞成功")

def setCollect(request):#增加收藏
    articleId =int(request.POST.get('articleId'))
    title =request.POST.get('title')
    username =request.POST.get('username')
    collectuser =request.POST.get('collectuser')
    user = Collect.objects.filter(articleId=articleId, collectuser=collectuser)
    if len(user) == 0:#避免误增
        Collect.objects.create(articleId=articleId, title=title,username = username, collectuser=collectuser)
        number = Article.objects.get(pk = articleId).collectnum
        Article.objects.filter(pk = articleId).update(collectnum=number+1)
    return HttpResponse("收藏成功")

class ArticleTagListId(APIView):
    def post(self, request, format=None):
        articles = Article.objects.filter(tag=request.POST.get('tag'))#.values('id')
        serializer = ArticleSerializer(articles, many=True)
        if(articles.count()==0):
            return HttpResponse("Tag不存在")
        return Response(serializer.data)

class ArticleList(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all().order_by("-createdate")
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetail(APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)