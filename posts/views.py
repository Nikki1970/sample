from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db import transaction
from django.views.generic import ListView
from .models import Post
from .forms import PostForm


class PostsListView(ListView):
    template_name = 'list.html'
    model = Post
    context_object_name = 'posts'


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
