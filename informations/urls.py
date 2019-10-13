from django.urls import path

from .views import *

app_name = 'informations'

urlpatterns= [
    path('<str:category>/', category_all, name='category_all'),
    path('<str:category>/detail/<int:id>', post_detail, name='post_detail'),
]

