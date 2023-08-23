from django import forms

from .models import Category


class SearchPostForm(forms.Form):
    category = forms.CharField(
        required=False,
    )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'slug')
