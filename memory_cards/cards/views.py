from django.shortcuts import render
from .models import Card
#from tags.models import Tag
#from django.core.paginator import Paginator


def cards_list(request):
    list_of_cards = Card.objects.all()
    context = {'cards': list_of_cards}
    return render(request, 'cards/cards.html', context)


def card_details(request, card_id: int):
    details = Card.objects.get(pk=card_id)
    context = {'card_details': details}
    return render(request, 'cards/card_details.html', context)
