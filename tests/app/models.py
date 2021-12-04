from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=20)


class Region(models.Model):
    name = models.CharField(max_length=20)


class Country(models.Model):
    name = models.CharField(max_length=20)
    customers = models.ManyToManyField(Customer, related_name='countries')
    region = models.ForeignKey(Region, related_name='countries',  on_delete=models.CASCADE)


class Article(models.Model):
    code = models.CharField(max_length=5, unique=True)
    description = models.CharField(max_length=50, null=True)
    customer = models.ForeignKey(Customer, related_name='articles', on_delete=models.CASCADE)


class Order(models.Model):
    code = models.CharField(max_length=5, unique=True)
    description = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    article = models.ForeignKey(Article, related_name='orders', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
