from django.core.mail import send_mail

from amungo.settings import EMAIL_HOST_USER
from .config import EMAIL_RECEIVERS_LIST, EMAIL_SUBJECT
from .exceptions import SendMessageError
from .models import BoardPhoto


def send_visitor_message(*, sender_name: str, sender_email: str, message: str) -> None:
    """ Generate visitor message from the form and send it to predefined emails """
    email_message = _form_message_text(sender_name, sender_email, message)
    try:
        send_mail(
            EMAIL_SUBJECT,
            email_message,
            EMAIL_HOST_USER,
            EMAIL_RECEIVERS_LIST,
            fail_silently=False
        )
    except Exception:
        raise SendMessageError('Error during message sending')


def _form_message_text(name: str, email: str, message: str) -> str:
    """ Form email content which will be sent"""
    text = f'New message from: {name} <{email}>:\n\n'\
           f'{message}\n\n\n'\
           f'This is an autogenerated message. Reply directly to {email}'
    return text


def get_boards_photos_for_home_page():
    """ Query all title board photos with related boards to be displayed on main page"""
    all_photos = BoardPhoto.objects.filter(is_title=True).select_related('board')
    return all_photos
