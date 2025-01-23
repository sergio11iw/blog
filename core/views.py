from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
def main(request):
    posts = Post.objects.all()
    return render(request, 'main.html', {'posts': posts})
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})
def post_add(request):
    if request.method == 'POST':
        title_data = request.POST.get('title')
        text_data = request.POST.get('text')
        print(title_data)
        print(text_data)
        if text_data and title_data:
            Post.objects.create(text=text_data, title=title_data)
    return render(request, 'post_add.html', {'post_add': post_add})
