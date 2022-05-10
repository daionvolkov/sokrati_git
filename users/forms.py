from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserRegForm(UserCreationForm):

    username = forms.CharField(label='Имя пользователя', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтвердите пароль', required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Повторно введите пароль'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

    def __init__(self, *args, **kwargs):
        super(UserRegForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['username'].help_text = 'Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_'



class UserUpdateForm(forms.ModelForm):


    class Meta:
        model = User
        fields = ['username', 'email']
