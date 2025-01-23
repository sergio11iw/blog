
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('', views.main),
    path('posts/<int:post_id>', views.post_detail, name='post_detail'),
    path('posts/add', views.post_add, name='post_add'),
]


