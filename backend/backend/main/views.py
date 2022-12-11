from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'test.html'


def test(request):
    return HttpResponse('Test')

