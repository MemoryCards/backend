from django.contrib import admin
from .models.models import Card, Category, Deck

admin.site.register(Card)
admin.site.register(Category)
admin.site.register(Deck)
