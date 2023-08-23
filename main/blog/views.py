from django.http import HttpRequest
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.views.generic import ListView

from .models import Category, Post
from .forms import SearchPostForm, CategoryForm


# class CategoryListView(ListView):
#     template_name = 'blog/index.html'
#     model = Category
#
#
# class PostListView(ListView):
#     template_name = 'blog/post-list.html'
#     model = Post
#     context_object_name = 'post_list'
#
#     def get_queryset(self):
#         category_slug = self.kwargs.get('slug')
#         category = get_object_or_404(Category, slug=category_slug)
#         return get_list_or_404(Post, category=category)
#
#
# class PostSearchListView(ListView):
#     template_name = 'blog/form.html'
#     model = Post
#
#     def get_queryset(self):
#         queryset = self.model.objects.filter(is_published=True)
#         if self.request.GET.get('category'):
#             category = Category.objects.filter(name__contains=self.request.GET.get('category').title())
#
#             if category:
#                 category = category[0]
#                 queryset = queryset.filter(category=category)
#         return queryset
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data()
#         form = SearchPostForm()
#         context['form'] = form
#         context['category_form'] = CategoryForm()
#         return context


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = '-date_created'
