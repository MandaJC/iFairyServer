from django.contrib import admin
from regNlog import models

class PersonAdmin(admin.ModelAdmin):
    list_display = ('username', 'nickname')
    list_filter = ('username', )
admin.site.register(models.Person, PersonAdmin)
# Register your models here.
class FollowAdmin(admin.ModelAdmin):
    list_display = ('username', 'followusername')
    list_filter = ('username', 'followusername')
admin.site.register(models.Follow, FollowAdmin)