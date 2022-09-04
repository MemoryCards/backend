from django.shortcuts import render
from .models import Deck
from cards.models import Card


def decks_list(request):
    list_of_decks = Deck.objects.all()
    context = {'decks': list_of_decks}
    return render(request, 'cards/decks.html', context)


def deck_details(request, deck_id: int):
    details = Deck.objects.get(pk=deck_id)
    card_details = Card.objects.filter(deck_id=details.id)
    context = {'deck': details, 'cards': card_details}
    return render(request, 'cards/deck.html', context)
