from django.shortcuts import render
from .models import Product, Category, Author, ProductPriceRange


# Create your views here.
def home(requests):
    products = Product.objects.all().order_by('-create_date')
    context = {
        'products': products
    }
    return render(requests, 'shop_app/home.html', context)


def product_dtl(requests, pid):
    product = Product.objects.get(id=pid)
    context = {
        'product': product
    }
    return render(requests, 'shop_app/product_detail.html', context)


def category_product(requests, category):
    category = Category.objects.get(name=category)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products
    }
    return render(requests, 'shop_app/category_product.html', context)


def product_filter_price(requests, price):
    # price = ProductPriceRange.objects.get(price=price) # Not Necessary
    products = Product.objects.filter(price__lte=price)
    context = {
        'price': price,
        'products': products
    }
    return render(requests, 'shop_app/product_by_price.html', context)


def about(requests):
    return render(requests, 'shop_app/about.html')


def contact(requests):
    return render(requests, 'shop_app/contact.html')

