from django.urls import path

from . import views

urlpatterns = [
    path('', views.posts_list, name="posts-list"),
    path('create/', views.post_create, name="post-create"),
    path('<slug:slug>/', views.post_detail, name="post-detail"),
    path('<slug:slug>/edit/', views.post_edit, name="post-edit")
]
