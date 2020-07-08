from .models import Author, Category


def sidebar_author(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return context


def sidebar_category(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return context
