from django.contrib import admin
from regNlog import models

class PersonAdmin(admin.ModelAdmin):
    list_display = ('username', 'nickname')
admin.site.register(models.Person, PersonAdmin)
# Register your models here.
