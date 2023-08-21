from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.posts, name="posts"),
    path("posts/<slug:slug>", views.posts_detail, name="posts_detail"),
]
