from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_info_his', null=True, blank=True)
    postname = models.CharField(max_length=50)
    image = models.ImageField(upload_to='instructions/his_img/%Y/%m/%d', blank=True)
    file = models.FileField(upload_to='instructions/his_file/%Y/%m/%d', blank=True)
    text = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.postname
    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])

class Photo(models.Model):
    image = models.ImageField(upload_to='instructions/img/')
