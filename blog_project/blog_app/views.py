from django.shortcuts import render
from .models import Author, Category, Post


# Create your views here.
def home(requests):
    posts = Post.objects.all().order_by('-create_date')
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


def author_post(requests, author):
    author = Author.objects.get(name=author)
    posts = Post.objects.filter(author=author)
    context = {
        'author': author,
        'posts': posts
    }
    return render(requests, 'blog_app/author_post.html', context)


def category_post(requests, category):
    category = Category.objects.get(name=category)
    posts = Post.objects.filter(category=category)
    context = {
        'category': category,
        'posts': posts
    }
    return render(requests, 'blog_app/category_post.html', context)


def about(requests):
    return render(requests, 'blog_app/about.html')


def contact(requests):
    return render(requests, 'blog_app/contact.html')
