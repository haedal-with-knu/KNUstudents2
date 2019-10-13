from django.urls import path

from .views import *

app_name = 'operation'

urlpatterns= [
    path('<str:category>/', category_all, name='category_all'),
    path('<str:category>/detail/<int:id>', post_detail, name='post_detail'),
    path('introduction/sangju/', sangju, name='sangju'),
    path('introduction/dongari/', dongari, name='dongari'),
    path('introduction/humanities/', humanities, name='humanities'),
    path('introduction/socialsci/', socialsci, name='socialsci'),
    path('introduction/naturalsci/', naturalsci, name='naturalsci'),
    path('introduction/bizadm/', bizadm, name='bizadm'),
    path('introduction/engineering/', engineering, name='engineering'),
    path('introduction/IT/', IT, name='IT'),
    path('introduction/agriculture/', agriculture, name='agriculture'),
    path('introduction/arts/', arts, name='arts'),
    path('introduction/teachers/', teachers, name='teachers'),
    path('introduction/medicine/', medicine, name='medicine'),
    path('introduction/dentistry/', dentistry, name='dentistry'),
    path('introduction/vet/', vet, name='vet'),
    path('introduction/humaneco/', humaneco, name='humaneco'),
    path('introduction/nursing/', nursing, name='nursing'),
    path('introduction/pharmacy/', pharmacy, name='pharmacy'),
    path('introduction/ecology/', ecology, name='ecology'),
    path('introduction/technology/', technology, name='technology'),
    path('introduction/publicadm/', publicadm, name='publicadm'),
    path('introduction/undecmajor/', undecmajor, name='undecmajor'),
    path('introduction/globalleaders/', globalleaders, name='globalleaders'),

]