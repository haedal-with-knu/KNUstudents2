from django.shortcuts import render
from .models import Post, Photo
from django.views.generic.list import ListView
# Create your views here.
def intro(request):
    return render(request, 'instructions/intro.html')

def depart(request):
    return render(request, 'instructions/depart.html')

class History(ListView):
    model = Post
    template_name = 'instructions/history.html'
    paginate_by = 6

def his_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'instructions/his_detail.html', {'post' : post})
