from django.shortcuts import redirect, render
from django.contrib import messages

from .config import PAGE_TITLES
from .forms import VisitorMessageForm
from .services import send_visitor_message, get_boards_photos_for_home_page
from .exceptions import SendMessageError


def home_page(request):
    message_form = VisitorMessageForm(request.POST or None)

    if request.method == 'POST' and message_form.is_valid():
        try:
            send_visitor_message(
                sender_name=message_form.cleaned_data.get('name', 'name_unreadable'),
                sender_email=message_form.cleaned_data.get('email', 'email_unreadable'),
                message=message_form.cleaned_data.get('message', 'message_unreadable')
            )
        except SendMessageError:
            messages.error(
                request,
                'Your message wasn\'t sent due to internall erorr. Please, try to send it again.'
            )
        return redirect('home_page')

    context = {
        'title': PAGE_TITLES.get('home_page', ''),
        'board_photos': get_boards_photos_for_home_page(),
        'message_form': message_form
    }
    return render(request, 'website/index.html', context)


def product_page(request, product_slug):
    context = {
        'title': PAGE_TITLES.get('product_page', '')
    }
    return render(request, 'website/product.html', context)
