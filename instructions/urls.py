from django.urls import path

from .views import *

app_name = 'instructions'

urlpatterns=[
    path('', intro, name='intro'),
    path('depart/', depart, name='depart'),
    path('history/', history, name='history'),
    path('history/<int:id>', his_detail, name='his_detail'),
]