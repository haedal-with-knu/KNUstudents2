from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post_introduction(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_operation_introduction')
    category = models.CharField(max_length=50, choices=(('introduction', 'introduction'),), blank=False)
    title = models.CharField(max_length=200, db_index=True)
    text = models.TextField(blank=True)
    photo = models.ImageField(upload_to = 'info_photo/%Y/%m/%d', blank=True)
    file = models.FileField(upload_to='info_file/%Y/%m/%d', blank=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Post_board(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_operation_board')
    category = models.CharField(max_length=50, choices=(('board', 'board'),), blank=False)
    title = models.CharField(max_length=200, db_index=True)
    text = models.TextField(blank=True)
    photo = models.ImageField(upload_to = 'info_photo/%Y/%m/%d', blank=True)
    file = models.FileField(upload_to='info_file/%Y/%m/%d', blank=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title