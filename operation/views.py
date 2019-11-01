from django.shortcuts import render
from .models import *
from django.core.paginator import  Paginator

# Create your views here.
def intro(request):
    category = '단위별 소개'
    return render(request, 'operation/category.html')

def category_all(request,category):
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
    return render(request, 'operation/board.html',
                  {'page':p,'posts': posts, 'current_page': current_page, 'is_paginated': is_paginated})

def post_detail(request, category, id):
    if category == 'board':
        cat = '게시판'
        post = Post_board.objects.get(category=category, id=id)
    else:
        cat = '단위별 소개'
        post = Post_introduction.objects.get(category=category, id=id)
    return render(request, 'operation/detail.html', {'post' : post, 'cat':cat})

def sangju(request):
    return render(request, 'operation/sangju.html')
def dongari(request):
    return render(request, 'operation/dongari.html')
def humanities(request):
    return render(request, 'operation/humanities.html')
def socialsci(request):
    return render(request, 'operation/socialsci.html')
def naturalsci(request):
    return render(request, 'operation/naturalsci.html')
def bizadm(request):
    return render(request, 'operation/bizadm.html')
def engineering(request):
    return render(request, 'operation/engineering.html')
def IT(request):
    return render(request, 'operation/IT.html')
def agriculture(request):
    return render(request, 'operation/agriculture.html')
def arts(request):
    return render(request, 'operation/arts.html')
def teachers(request):
    return render(request, 'operation/teachers.html')
def medicine(request):
    return render(request, 'operation/medicine.html')
def dentistry(request):
    return render(request, 'operation/dentistry.html')
def vet(request):
    return render(request, 'operation/vet.html')
def humaneco(request):
    return render(request, 'operation/humaneco.html')
def nursing(request):
    return render(request, 'operation/nursing.html')
def pharmacy(request):
    return render(request, 'operation/pharmacy.html')
def ecology(request):
    return render(request, 'operation/ecology.html')
def technology(request):
    return render(request, 'operation/technology.html')
def publicadm(request):
    return render(request, 'operation/publicadm.html')
def undecmajor(request):
    return render(request, 'operation/undecmajor.html')
def globalleaders(request):
    return render(request, 'operation/globalleaders.html')
