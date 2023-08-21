from django.urls import path, register_converter

from .views import CategoryListView, PostListView
from .converters import ULIDConverter


register_converter(converter=ULIDConverter, type_name='uuuu')


urlpatterns = [
    path('<slug:slug>/', PostListView.as_view(), name='blog_post_list'),
    path('', CategoryListView.as_view(), name='blog_index'),
    # path('<ulid:post_ulid>/', )
]
