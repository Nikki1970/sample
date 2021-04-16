from django.urls import path

from . import views

urlpatterns = [
    path('', views.posts_list),
    path('<slug:slug>/', views.post_detail, name="post-detail"),
    path('<slug:slug>/edit/', views.post_edit, name="post-edit")
]
