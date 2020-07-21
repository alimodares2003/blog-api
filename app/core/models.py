from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=64)
    STATUS = (
        (0, 'deactivated'),
        (1, 'active'),
    )
    status = models.IntegerField(choices=STATUS, default=1)
    cdt = models.DateTimeField(auto_now_add=True)
    udt = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=64)
    STATUS = (
        (0, 'deactivated'),
        (1, 'active'),
    )
    status = models.IntegerField(choices=STATUS, default=1)
    cdt = models.DateTimeField(auto_now_add=True)
    udt = models.DateTimeField(auto_now=True)


class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    STATUS = (
        (0, 'deactivated'),
        (1, 'active'),
    )
    status = models.IntegerField(choices=STATUS, default=1)
    cdt = models.DateTimeField(auto_now_add=True)
    udt = models.DateTimeField(auto_now=True)
