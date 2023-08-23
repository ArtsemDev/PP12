from django.contrib import admin

from .models import Category, Post


@admin.action(description='Опубликовать')
def make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='Снять с публикации')
def make_unpublished(modeladmin, request, queryset):
    queryset.update(is_published=False)


class PostStackedInline(admin.StackedInline):
    model = Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_editable = ('slug', )
    search_fields = ('name', 'slug')
    prepopulated_fields = {
        'slug': ('name', )
    }
    inlines = (PostStackedInline, )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')
    date_hierarchy = 'date_created'
    list_filter = ('category', )
    prepopulated_fields = {
        'slug': ('title', )
    }
    readonly_fields = ('date_created', )
    actions = (make_published, make_unpublished)
    fieldsets = (
        (
            'Основное',
            {
                'fields': ('title', 'body'),
            }
        ),
        (
            'Дополнительное',
            {
                'fields': (
                    'category',
                    'date_created',
                    'is_published',
                    'slug'
                )
            }
        )
    )
