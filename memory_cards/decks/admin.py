from django.contrib import admin

from .models import Deck


@admin.register(Deck)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['name']