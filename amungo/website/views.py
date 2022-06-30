from django.shortcuts import redirect, render

from .config import PAGE_TITLES
from .forms import VisitorMessageForm


def home_page(request):

    if request.method == 'POST':
        form = VisitorMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')

    context = {
        'title': PAGE_TITLES.get('home_page', ''),
        'message_form': VisitorMessageForm()
    }
    return render(request, 'website/index.html', context)


def product_page(request):
    context = {
        'title': PAGE_TITLES.get('product_page', '')
    }
    return render(request, 'website/product.html', context)


def visitor_message_success(request):
    return render(request, 'website/index.html')
