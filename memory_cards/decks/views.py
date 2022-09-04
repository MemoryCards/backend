from django.shortcuts import render
from .models import Deck
#from .models import Category

def decks_list(request):
    list_of_decks = Deck.objects.all()
    context = {'decks': list_of_decks}
    return render(request, 'cards/decks.html', context)


def deck_details(request, deck_id: int):
    details = Deck.objects.get(pk=deck_id)
    context = {'deck': details}
    return render(request, 'cards/deck.html', context)
