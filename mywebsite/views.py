from django.shortcuts import render


def index(request):
    context = {
        'page_title': 'Home',
        'title': 'Home',
        'subtitle': 'Selamat Datang Di My Website',
        'heading': ''

    }
    return render(request, 'index.html', context)
