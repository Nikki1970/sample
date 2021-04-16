from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


def posts_list(request):
    objects = Post.objects.all()

    context = {
        'posts': objects
    }
    return render(request, 'list.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post
    }
    return render(request, 'detail.html', context)
