from .models import Category, ProductPriceRange


def sidebar_category(requests):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return context


def sidebar_price_range(requests):
    all_price_range = ProductPriceRange.objects.all()
    context = {
        'price_ranges': all_price_range
    }
    return context
