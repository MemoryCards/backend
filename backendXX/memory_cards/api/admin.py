from django.contrib import admin
from .models.models import Card, Category, Deck






class CardAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'question', 'answer', 'deck')
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Card, CardAdmin)

class DeckAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Deck, DeckAdmin)
admin.site.register(Category,DeckAdmin)