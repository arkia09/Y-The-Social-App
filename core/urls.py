from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("post/", views.post_list, name="post_list"),
    path("create/", views.post_create, name="post_create"),
    path("post/<int:post_id>/delete/", views.post_delete, name="post_delete"),
    path("post/<int:post_id>/edit/", views.post_edit, name="post_edit"),
    path('<int:post_id>/like/', views.toggle_likes, name='toggle_likes'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
]
