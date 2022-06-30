from django.shortcuts import render

from .config import PAGE_TITLES


def home_page(request):
    context = {
        'title': PAGE_TITLES.get('home_page', '')
    }
    return render(request, 'website/index.html', context)


def product_page(request):
    context = {
        'title': PAGE_TITLES.get('product_page', '')
    }
    return render(request, 'website/product.html', context)


def visitor_message_success(request):
    return render(request, 'website/index.html')