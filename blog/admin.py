from django.contrib import admin
from .models import Post, Comment, Category
# Register your models here.

# Register admin model
# https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#modeladmin-objects


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')  # list of fileds that are displayed on the admin object page
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author', 'category',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Comment, CommentAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_title', 'category_slug')
    list_filter = ('category_title', 'created')
    search_fields = ('category_title', 'category_slug', 'category_description')
    prepopulated_fields = {'category_slug': ('category_title',)}
    raw_id_fields = ('category_parent',)
    ordering = ['created']


admin.site.register(Category, CategoryAdmin)
