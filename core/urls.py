from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/", views.post_list, name="post_list"),
    path("create/", views.post_create, name="post_create"),
    path("post/<int:post_id>/delete/", views.post_delete, name="post_delete"),
    path("post/<int:post_id>/edit/", views.post_edit, name="post_edit"),
    path("post/<int:post_id>/likes/", views.toggle_likes, name="toggle_likes"),
]
