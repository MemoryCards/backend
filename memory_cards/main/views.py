from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')

def contact(request):
    return render(request, 'main/contact.html')

def about (request): 
    return render(request, 'main/about.html')

def client_panel (request):
    return render(request, 'main/client_panel.html')
