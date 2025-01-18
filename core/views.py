from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
def main(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        title_data = request.POST['title']
        text_data = request.POST['text']
        if title_data and text_data:
             Post.objects.create(title=title_data, text=text_data)
    return render(request, 'main.html', {'posts': posts})
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})

# Create your views here.
