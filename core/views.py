from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'usuario': 'rogerio'})


def contact(request):
    return render(request, 'contact.html')
