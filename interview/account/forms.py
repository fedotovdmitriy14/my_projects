from django.forms import ModelForm, TextInput
from .models import Account

class AccountForm(ModelForm):

    class Meta:
        model = Account
        fields = ['name',]

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Имя"
            })
        }