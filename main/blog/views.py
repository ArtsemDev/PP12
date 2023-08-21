from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import ListView

from .models import Category, Post


class CategoryListView(ListView):
    template_name = 'blog/index.html'
    model = Category


class PostListView(ListView):
    template_name = 'blog/post-list.html'
    model = Post
    context_object_name = 'post_list'

    def get_queryset(self):
        category_slug = self.kwargs.get('slug')
        category = get_object_or_404(Category, slug=category_slug)
        return get_list_or_404(Post, category=category)
