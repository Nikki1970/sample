from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db import transaction

from .models import Post
from .forms import PostForm


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


def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)

    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post-detail', slug=post.slug)

    context = {
        'post': post,
        'form': form
    }
    return render(request, 'form.html', context)


@transaction.atomic
@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        return redirect('post-detail', slug=obj.slug)

    context = {
        'form': form
    }
    return render(request, 'form.html', context)
