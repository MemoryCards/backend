from django.urls import path

from .views import deck_details, decks_list

app_name = 'decks'

urlpatterns = [
    path('', decks_list, name='all'),
    path('<int:deck_id>', deck_details, name='deck')
]