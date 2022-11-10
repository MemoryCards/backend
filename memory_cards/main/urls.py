from django.urls import path

from .views import home, about, contact, client_panel

app_name = 'main'


urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('client_panel', client_panel, name='client_panel')
]
