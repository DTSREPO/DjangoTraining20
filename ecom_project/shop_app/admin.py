from django.contrib import admin
from .models import Author, Category, Product, ProductPriceRange

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductPriceRange)

