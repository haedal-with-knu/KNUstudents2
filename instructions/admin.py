from django.contrib import admin

# Register your models here.
from .models import *

class Post_his(admin.ModelAdmin):
    list_display = ['id','author','updated','postname']
    raw_id_fields = ['author']
    list_filter = ['author']
    search_fields = ['author','postname','created']
    ordering = ['-updated']
    list_editable = ['postname']
admin.site.register(Post, Post_his)
