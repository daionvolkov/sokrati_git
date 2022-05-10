from .models import Links
from django import forms




class LinkForm(forms.ModelForm):
    class Meta:
        model = Links
        fields = ['oldLink', 'newLink', 'user']
        labels = {
            'oldLink': 'Длинная ссылка',
            'newLink': 'Короткая ссылка',
        }
        unique = (
            ('newLink'),
        )
        widgets = {
            'user': forms.HiddenInput()
       }








