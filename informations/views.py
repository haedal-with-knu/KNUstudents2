from django.shortcuts import render
from .models import *
from django.core.paginator import  Paginator

# Create your views here.

def category_all(request,category):
    if (category=='bylaw'):
        category='회칙'
        posts = Post_bylaw.objects.all().order_by('-created')
        paginator = Paginator(posts, 10)

        is_paginated = True if paginator.num_pages>1 else False
        page = request.GET.get('page') or 1

        current_page = paginator.page(page)

    else:
        category='안건지/회의록'
        posts = Post_minutes.objects.all().order_by('-created')
        paginator = Paginator(posts, 10)

        is_paginated = True if paginator.num_pages > 1 else False
        page = request.GET.get('page') or 1

        current_page = paginator.page(page)

    all_num = paginator.count-10
    if int(page) == round(paginator.count/10 + 0.5):
        all_num=0
        num = 0
    else:
        num = 10*(int(page)-1)
    p = all_num - num
    return render(request, 'informations/category.html', {'page':p, 'posts': posts, 'category':category, 'current_page': current_page, 'is_paginated':is_paginated})





def post_detail(request, category, id):
    if category == 'minutes':
        cat = '안건지/회의록'
        post = Post_minutes.objects.get(category=category, id=id)
    else:
        cat = '회칙'
        post = Post_bylaw.objects.get(category=category, id=id)
    return render(request, 'informations/detail.html', {'post' : post, 'cat':cat})