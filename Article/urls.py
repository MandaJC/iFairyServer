from django.conf.urls import url
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('headimg/', views.changeHeadImg),#修改用户头像
    # path('nickname/', views.changeNickName),#修改昵称

    path('islike/', views.isLike),#是否已点赞某文章
    path('iscollect/', views.isCollect),#是否已收藏某文章
    path('setlike/', views.setLike),#点赞某文章
    path('setcollect/', views.setCollect),#收藏某文章

    path('list/', views.ArticleList.as_view()),#get获取文章列表，post新增文章
    path('detail/<int:pk>', views.ArticleDetail.as_view()),#get获取指定文章，post修改文章内容

    path('tag/', views.ArticleTagListId.as_view()),#按搜索输入的tag索引文章列表

    path('collectarticlelist/', views.CollectArticleList.as_view()),#获取收藏文章列表
    path('myarticlelist/', views.MyArticleList.as_view()),#获取收藏文章列表

    path('commentpost/', views.CommentPost),#发表评论
    path('commentlist/', views.CommentList.as_view()),#获取收藏文章列表

    path('followuserarticlelist/', views.FollowUserArticleList.as_view()),  # 获取关注用户文章列表
    path('setfollow/', views.setFollow),  # 添加关注用户

    path('selfinfo/', views.selfInfo),  # 获取个人信息

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)