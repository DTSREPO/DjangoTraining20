from django.shortcuts import render
from .models import Author, Category, Post


# Create your views here.
def home(requests):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(requests, 'blog_app/home.html', context)


def single_post(requests, pid):
    post = Post.objects.get(id=pid)
    context = {
        'post': post
    }
    return render(requests, 'blog_app/single_post.html', context)


def about(requests):
    return render(requests, 'blog_app/about.html')


def contact(requests):
    return render(requests, 'blog_app/contact.html')
