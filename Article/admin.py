from django.contrib import admin
from Article import models

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'content','createdate')
    list_filter = ('tag', 'createdate')

admin.site.register(models.Article, ArticleAdmin)
# Register your models here.

class LikeAdmin(admin.ModelAdmin):
    list_display = ('articleId', 'title', 'username', 'likeuser')
    list_filter = ('articleId', 'likeuser')

admin.site.register(models.Like, LikeAdmin)

class CollectAdmin(admin.ModelAdmin):
    list_display = ('articleId', 'title', 'username', 'collectuser')
    list_filter = ('articleId', 'collectuser')

admin.site.register(models.Collect, CollectAdmin)
