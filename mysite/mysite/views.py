from django.shortcuts import render


def home(request):
    return render(request, 'mysite/home.html')


def contact(request):
    return render(request, 'join.html', {'title': 'Contact'})
