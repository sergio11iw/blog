
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('', views.main, name='main'),
    path('posts/<int:post_id>', views.post_detail, name='post_detail'),
]


