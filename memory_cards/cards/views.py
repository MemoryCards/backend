from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Card, Tag, Category
#from tags.models import Tag
#from django.core.paginator import Paginator


def cards_list(request):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    list_of_cards = Card.objects.all()
    context = {'cards': list_of_cards, 'tags': tags, 'categories': categories}
    return render(request, 'cards/cards.html', context)


def card_details(request, card_id: int):
    tags = Tag.objects.all()
    category = Category.objects.all()
    details = Card.objects.get(pk=card_id)
    context = {'card_details': details, 'tags': tags, 'category': category }
    return render(request, 'cards/card_details.html', context)

def add_user_card(request):
    return
