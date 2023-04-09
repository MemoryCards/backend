from django.contrib import admin

from .models import Card, Deck, Category, Tag, StudentProfile

admin.site.register(Card)
admin.site.register(Deck)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(StudentProfile)