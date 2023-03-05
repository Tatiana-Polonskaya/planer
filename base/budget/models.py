from django.db import models

class Caterogy(models.Model):

    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=120)
    date = models.DateField()

    def get_absolute_url(self):
        return f'budget/products/{self.id}'

