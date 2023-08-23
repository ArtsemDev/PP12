from django.db import models
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(max_length=24, unique=True, blank=False, null=False)
    slug = models.SlugField(max_length=24, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Post(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    body = models.TextField(null=True, blank=True)
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, db_index=True)
    date_created = models.DateTimeField(default=now)
    is_published = models.BooleanField(default=False)

    @property
    def date(self):
        return self.date_created.strftime('%H:%M %d %m %Y')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
