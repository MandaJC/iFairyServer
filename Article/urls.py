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

    path('tag/', views.ArticleTagListId.as_view())#按搜索输入的tag索引文章列表
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)