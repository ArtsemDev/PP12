from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=24, unique=True, blank=False, null=False)
    slug = models.SlugField(max_length=24, unique=True, blank=False, null=False)


class Post(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    body = models.TextField()
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, db_index=True)
