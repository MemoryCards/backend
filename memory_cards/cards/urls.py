from django.urls import path

from .views import cards_list, card_details

app_name = 'cards'

urlpatterns = [
    path('', cards_list, name='all'),
    path('<int:card_id>', card_details, name='card')
]