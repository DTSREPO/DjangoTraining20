from django.shortcuts import render, redirect
from blog_app import models
from .forms import AuthorCreateForm, CategoryCreateForm, PostCreateForm


# Create your views here.
def dashboard(request):
    return render(request, 'blog_admin_app/dashboard.html')


def author_list(request):
    authors = models.Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'blog_admin_app/author_list.html', context)


def create_author(requests):
    form = AuthorCreateForm(requests.POST or None)
    if requests.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('author-list')

    context = {
        'form': form
    }
    return render(requests, 'blog_admin_app/create_author.html', context)


def category_list(request):
    categories = models.Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'blog_admin_app/category_list.html', context)


def create_category(requests):
    form = CategoryCreateForm(requests.POST or None)
    if requests.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('category-list')

    context = {
        'form': form
    }
    return render(requests, 'blog_admin_app/create_category.html', context)


def post_list(request):
    posts = models.Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog_admin_app/post_list.html', context)


def create_post(requests):
    form = PostCreateForm(requests.POST or None, requests.FILES or None)
    if requests.method == 'POST':
        print(requests.POST)
        if form.is_valid():
            form.save()

            return redirect('post-list')

    context = {
        'form': form
    }
    return render(requests, 'blog_admin_app/create_post.html', context)
