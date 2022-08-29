from django.contrib import admin


from .models import Card, Category, Tag

@admin.register(Card)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['question']

@admin.register(Category)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Tag)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['name']
