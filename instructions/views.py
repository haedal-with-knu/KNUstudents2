from django.shortcuts import render
from .models import *
from django.views.generic.list import ListView
from django.core.paginator import  Paginator

# Create your views here.
def intro(request):
    return render(request, 'instructions/intro.html')

def depart(request):
    return render(request, 'instructions/depart.html')

#class History(ListView):
 #   model = Post
  #  template_name = 'instructions/history.html'
   # paginate_by = 10


def history(request,):
    posts = Post.objects.all().order_by('-updated')
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
    return render(request, 'instructions/history.html', {'page':p, 'posts': posts, 'current_page': current_page, 'is_paginated':is_paginated})


def his_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'instructions/his_detail.html', {'post' : post})


