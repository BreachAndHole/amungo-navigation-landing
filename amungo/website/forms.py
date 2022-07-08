from django.forms import ModelForm, TextInput, Textarea

from .models import VisitorMessage
from .config import MESSAGE_FORM_PLACEHOLDERS


class VisitorMessageForm(ModelForm):
    """
    Message from this form will be saved in database
    and sent to all emails listed in EMAIL_RECEIVERS_LIST in website/config.py file
    """
    class Meta:
        model = VisitorMessage

        fields = ['name', 'email', 'message']

        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': MESSAGE_FORM_PLACEHOLDERS.get('name', ''),
                    'class': 'form-control',
                }
            ),
            'email': TextInput(
                attrs={
                    'placeholder': MESSAGE_FORM_PLACEHOLDERS.get('email', ''),
                    'class': 'form-control',
                }
            ),
            'message': Textarea(
                attrs={
                    'placeholder': MESSAGE_FORM_PLACEHOLDERS.get('message', ''),
                    'class': 'form-control',
                    'rows': 5,  # This setting will affect height of message area
                }
            ),
        }
