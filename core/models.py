from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

class Products(models.Model):
    name = models.CharField(max_length=240,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    img = models.ImageField(upload_to='animation_photos')
    price = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    stock = models.IntegerField()