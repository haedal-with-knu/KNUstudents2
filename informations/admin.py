from django.contrib import admin
from .models import *
# Register your models here.


class Post_bylaw_Admin(admin.ModelAdmin):
    list_display = ['id','category','author','created','title']
    raw_id_fields = ['author']
    list_filter = ['category','author']
    search_fields = ['author','title','created']
    ordering = ['-created']
    list_editable = ['category','title']
admin.site.register(Post_bylaw, Post_bylaw_Admin)

class Post_minutes_Admin(admin.ModelAdmin):
    list_display = ['id','category','author','created','title']
    raw_id_fields = ['author']
    list_filter = ['category','author']
    search_fields = ['author','title','created']
    ordering = ['-created']
    list_editable = ['category','title']
admin.site.register(Post_minutes, Post_minutes_Admin)