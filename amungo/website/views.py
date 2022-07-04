from django.shortcuts import redirect, render
from django.contrib import messages

from .config import PAGE_TITLES
from .forms import VisitorMessageForm
from .services import send_visitor_message
from .exceptions import SendMessageError


def home_page(request):
    form = VisitorMessageForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        try:
            send_visitor_message(
                sender_name=form.cleaned_data.get('name', 'name_unreadable'),
                sender_email=form.cleaned_data.get('email', 'email_unreadable'),
                text=form.cleaned_data.get('message', '')
            )
        except SendMessageError:
            messages.error(
                request,
                'Your message wasn\'t sent due to internall erorr. Please, try to send it again.'
            )

        return redirect('home_page')

    context = {
        'title': PAGE_TITLES.get('home_page', ''),
        'message_form': form
    }
    return render(request, 'website/index.html', context)


def product_page(request):
    context = {
        'title': PAGE_TITLES.get('product_page', '')
    }
    return render(request, 'website/product.html', context)
