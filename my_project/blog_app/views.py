from django.shortcuts import render
from .models import Author, Post


# Create your views here.
def home(request):
    return render(request, 'blog_app/home.html')


def about(request):
    return render(request, 'blog_app/about.html')


def post_list(request):
    authors = Author.objects.all()
    posts = Post.objects.all()

    context = {
        'authors': authors,
        'post_list': posts,
        'username': request.user.username,
    }
    return render(request, 'blog_app/post_list.html', context)


def post_list_by_author(request, author):
    authors = Author.objects.all()
    posts = Post.objects.filter(author=author)

    context = {
        'authors': authors,
        'author': author,
        'post_list': posts,
        'username': request.user.username,
    }
    return render(request, 'blog_app/post_list_author.html', context)


def post_details(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post,
        'username': request.user.username,
    }
    return render(request, 'blog_app/post_details.html', context)


def contact(request):
    return render(request, 'blog_app/contact.html')
