from django.urls import path

from .views import MainView, test

urlpatterns = [
    path('main/', MainView.as_view()),
    path('test', test)
]
