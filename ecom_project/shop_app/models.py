from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    product_image = models.ImageField(blank=True, null=True, upload_to='shop')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.IntegerField(default=0, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductPriceRange(models.Model):
    price = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        price = str(self.price)
        return price
