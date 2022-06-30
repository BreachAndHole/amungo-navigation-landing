from django.shortcuts import render

from .config import PAGE_TITLES


def home_page(request):
    context = {
        'title': PAGE_TITLES.get('home_page')
    }
    return render(request, 'website/index.html', context)
