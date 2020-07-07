from django.db import models


# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=250, verbose_name='District Name')
    area = models.CharField(max_length=50, verbose_name='Area')
    population = models.CharField(max_length=50, verbose_name='Population')

    def __str__(self):
        return self.name
