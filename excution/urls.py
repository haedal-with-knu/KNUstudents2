from django.urls import path

from .views import *

app_name = 'excution'

urlpatterns= [
    path('<str:category>/', category_all, name='category_all'),
    path('<str:category>/detail/<int:id>', post_detail, name='post_detail'),
    path('introduction/publicity/', publicity, name='publicity'),
    path('introduction/rights/', rights, name='rights'),
    path('introduction/finance/', finance, name='finance'),
    path('introduction/welfare/', welfare, name='welfare'),
    path('introduction/culture/', culture, name='culture'),
    path('introduction/cooperation/', cooperation, name='cooperation'),
    path('introduction/support/', support, name='support'),

]