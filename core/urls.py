from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/", views.post_list, name="post_list"),
    path("create/", views.post_create, name="post_create"),
    path("delete/", views.post_delete, name="post_delete"),
]
