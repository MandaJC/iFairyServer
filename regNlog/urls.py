from django.urls import path
from regNlog.views import register, login
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from regNlog import views

urlpatterns = [
    path('register/', register),
    path('login/', login),
]

urlpatterns = format_suffix_patterns(urlpatterns)