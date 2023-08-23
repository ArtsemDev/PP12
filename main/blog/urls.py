from django.urls import path, register_converter

from .views import PostListView
from .converters import ULIDConverter


register_converter(converter=ULIDConverter, type_name='uuuu')


urlpatterns = [
    path('', PostListView.as_view(), name='blog_index'),
]
