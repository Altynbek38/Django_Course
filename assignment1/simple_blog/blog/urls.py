from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('posts/', views.post_list, name="posts"),
    path('posts/<int:id>/', views.post_details, name="post_details"),
    path('posts/create/', views.post_create, name="post_create"),
    path('posts/<int:id>/update/', views.post_edit, name="post_update"),
    path('posts/<int:id>/delete/', views.post_delete, name="post_delete"),
    path('posts/<int:id>/comment', views.comment_list, name="comment_list"),
    path('posts/<int:id>/comment/create', views.comment_create, name="comment_add"),
]