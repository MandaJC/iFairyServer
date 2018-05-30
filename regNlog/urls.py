from django.urls import path
from regNlog.views import register, login
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from regNlog import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register/', register),
    path('login/', login),

    path('password/', views.changePassword),
    path('headimg/', views.changeHeadImg),
    path('nickname/', views.changeNickName),

    path('detail/<int:pk>', views.PersonDetail.as_view())
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)