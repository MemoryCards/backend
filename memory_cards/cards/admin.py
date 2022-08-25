from django.contrib import admin


from .models import Card

@admin.register(Card)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['question']
    #date_hierarchy = 'publish'
    #list_filter = ['title']
    #prepopulated_fields = {"slug": ("title",)}