from django.forms import ModelForm, TextInput, Textarea

from .models import VisitorMessage
from .config import MESSAGE_FORM_PLACEHOLDERS


class VisitorMessageForm(ModelForm):

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
                    'rows': 3,
                }
            ),
        }
