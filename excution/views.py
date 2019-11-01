from django.shortcuts import render
from .models import *
from django.core.paginator import  Paginator

# Create your views here.

def category_all(request,category):
    if (category=='introduction'):
        category='국별 소개'
        posts = Post_introduction.objects.all().order_by('-created')

        return render(request, 'excution/category.html', {'posts': posts, 'category': category})
    else:
        category='게시판'
        posts = Post_board.objects.all().order_by('-created')
        paginator = Paginator(posts, 10)

        is_paginated = True if paginator.num_pages > 1 else False
        page = request.GET.get('page') or 1

        current_page = paginator.page(page)

        all_num = paginator.count - 10
        if int(page) == round(paginator.count / 10 + 0.5):
            all_num = 0
            num = 0
        else:
            num = 10 * (int(page) - 1)
        p = all_num - num
        return render(request, 'excution/board.html', {'page': p, 'posts': posts, 'category': category, 'current_page': current_page, 'is_paginated': is_paginated})


def post_detail(request, category, id):
    if category == 'board':
        cat = '게시판'
        post = Post_board.objects.get(category=category, id=id)
    else:
        cat = '국별 소개'
        post = Post_introduction.objects.get(category=category, id=id)
    return render(request, 'excution/detail.html', {'post' : post, 'cat':cat})

def publicity(request):
    return render(request, 'excution/publicity.html')
def rights(request):
    return render(request, 'excution/rights.html')
def welfare(request):
    return render(request, 'excution/welfare.html')
def culture(request):
    return render(request, 'excution/culture.html')
def cooperation(request):
    return render(request, 'excution/cooperation.html')
def support(request):
    return render(request, 'excution/support.html')
def finance(request):
    return render(request, 'excution/finance.html')

