from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150, verbose_name='Student Name')
    gender = models.CharField(max_length=30, verbose_name='Gender')
    age = models.CharField(max_length=15, verbose_name='Age')
    cls = models.CharField(max_length=150, verbose_name='Class')
    roll = models.IntegerField(verbose_name='Roll')
    gpa = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name
