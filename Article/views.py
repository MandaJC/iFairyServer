from Article.models import Article, Like, Collect, Comment
from regNlog.models import Person
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from .serializers import ArticleSerializer, CommentSerializer
from django.core.exceptions import ObjectDoesNotExist

def selfInfo(request):
    username = request.POST.get('username')
    user = Person.objects.get(username=username)
    fansnum = user.fans.count()
    follownum = user.follow.count()
    collect = Collect.objects.get(collectuser=username)
    collectnum =collect.article.count()
    articlenum = Article.objects.filter(username=username).count()
    headimg = user.userphoto.name
    nickname = user.nickname
    return JsonResponse({"fansnum":fansnum, "follownum":follownum, "collectnum":collectnum, "articlenum":articlenum, "nickname":nickname, "headimg":headimg})


def setFollow(request):
    followuser = request.POST.get('username')
    fansuser = request.POST.get('fansuser')#客户端登录用户
    follow = Person.objects.get(username=followuser)
    fans = Person.objects.get(username=fansuser)
    fans.follow.add(follow)
    return HttpResponse("关注成功")

class FollowUserArticleList(APIView):#获取收藏列表
    def post(self, request, format=None):
        username = request.POST.get('username')
        fans = Person.objects.get(username=username)
        totalfollow = fans.follow.all()
        list=[]
        for i in totalfollow:
            list.append(Article.objects.filter(username=i.username))
        outset = list[0]
        for i in list:
            outset = outset | i
        outset = outset.distinct()
        serializer = ArticleSerializer(outset, many=True)
        return Response(serializer.data)

class CommentList(APIView):#获取收藏列表
    def post(self, request, format=None):
        articleId = int(request.POST.get('articleId'))
        comments = Comment.objects.filter(articleId=articleId).order_by("-createdate")
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

def CommentPost(request):  # 获取收藏列表
    # def post(self, request, format=None):#有毒，这个不能单独修改一个属性，大概要用数据库的级联操作吧，以后再测试，先暴力全改
        # data = request.data#含articleId和comment
        commentuser = request.POST.get('commentuser')
        articleId = int(request.POST.get('articleId'))
        # return HttpResponse(articleId)
        comment = request.POST.get('comment')
        nickname = Person.objects.get(username=commentuser).nickname
        userphoto = Person.objects.get(username=commentuser).userphoto
        Comment.objects.create(articleId=articleId, commentuser=commentuser, comment=comment,nickname=nickname,userphoto=userphoto)
        return HttpResponse("发表评论成功")

        # serializer = CommentSerializer(data=data)
        # if serializer.is_valid():
        #     serializer.save()
        #     Comment.objects.filter(commentuser=commentuser).update(nickname=nickname)
        #     Comment.objects.filter(commentuser=commentuser).update(userphoto=userphoto)
        #     # return Response(serializer.data, status=status.HTTP_201_CREATED)
        #     return HttpResponse("发表评论成功")
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CollectArticleList(APIView):#获取收藏列表
    def post(self, request, format=None):
        collectuser = request.POST.get('collectuser')
        b = Collect.objects.get(collectuser=collectuser)
        data=b.article.all()
        serializer = ArticleSerializer(data, many=True)
        return Response(serializer.data)

class MyArticleList(APIView):#获取收藏列表
    # def get(self, request, format=None):
    #     articles = Article.objects.all().order_by("-createdate")
    #     serializer = ArticleSerializer(articles, many=True)
    #     return Response(serializer.data)
    def post(self, request, format=None):
        username = request.POST.get('username')
        data = Article.objects.filter(username=username)
        serializer = ArticleSerializer(data, many=True)
        return Response(serializer.data)

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
    collectuser =request.POST.get('collectuser')
    user = Collect.objects.filter(collectuser=collectuser)
    if user.count()>0:
        # user = Collect.objects.get(collectuser=collectuser)
        test=user[0].article.all().filter(pk=articleId)
        if test.count()>0:
            return HttpResponse("已收藏")
        else:
            return HttpResponse("未收藏")
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
    collectuser =request.POST.get('collectuser')
    a=Article.objects.get(pk=articleId)
    user = Collect.objects.filter(collectuser=collectuser)
    if len(user) == 0:#避免误增
        Collect.objects.create(collectuser=collectuser)
    b=Collect.objects.get(collectuser=collectuser)
    b.article.add(a)
    number = a.collect_article.count()#反向查询
    Article.objects.filter(pk = articleId).update(collectnum=number)
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

    def post(self, request, format=None):#有毒，这个不能单独修改一个属性，大概要用数据库的级联操作吧，以后再测试，先暴力全改
        data = request.data
        # data2 = Article(data, )
        username = request.POST.get('username')
        nickname = Person.objects.get(username=username).nickname
        userphoto = Person.objects.get(username=username).userphoto
        serializer = ArticleSerializer(data=data)
        # serializer = serializer.update(serializer.instance, nickname)
        # serializer['nickname'] =
        if serializer.is_valid():
            serializer.save()
            Article.objects.filter(username=username).update(nickname=nickname)
            Article.objects.filter(username=username).update(userphoto=userphoto)
            Like.objects.filter(username=username).update(nickname=nickname)
            # Collect.objects.filter(username=username).update(nickname=nickname)
            Comment.objects.filter(commentuser=username).update(nickname=nickname)
            Comment.objects.filter(commentuser=username).update(userphoto=userphoto)
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