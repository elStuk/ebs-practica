from django.db import models
from django.contrib import admin


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    enable = models.BooleanField(default=True)


class BlagAdmin(admin.ModelAdmin):
    list_display = ('title', 'enable')


class Comments(models.Model):
    title = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
