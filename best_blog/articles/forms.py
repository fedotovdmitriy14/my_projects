from django.forms import ModelForm, TextInput

from articles.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['login', 'user_psw']

        widgets = {
            'login': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "login"
            }),
            'user_psw': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'password'
            }),
        }
