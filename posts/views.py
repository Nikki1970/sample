from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def posts_list(request):
    objects = Post.objects.all()

    context = {
        'posts': objects
    }
    return render(request, 'list.html', context)
