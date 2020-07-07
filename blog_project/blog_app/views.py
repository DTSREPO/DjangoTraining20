from django.shortcuts import render


# Create your views here.
def home(requests):
    return render(requests, 'blog_app/home.html')


def about(requests):
    return render(requests, 'blog_app/about.html')


def contact(requests):
    return render(requests, 'blog_app/contact.html')
