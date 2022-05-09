from .models import Links
from django import forms
from django.core.exceptions import ValidationError



class LinkForm(forms.ModelForm):
    class Meta:
        model = Links
        fields = ['oldLink', 'newLink']
        labels = {
            'oldLink': 'Длинная ссылка',
            'newLink': 'Короткая ссылка',
        }
        unique = (
            ('newLink'),
        )







