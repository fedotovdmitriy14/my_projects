from captcha.fields import CaptchaField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import forms, TextInput, IntegerField, Textarea, ModelForm, CheckboxSelectMultiple, RadioSelect, \
    PasswordInput, CharField, EmailField, EmailInput
from .models import Movie

class MovieForm(ModelForm):

    class Meta:
        model = Movie
        fields = ['name', 'score', 'text', 'film_name']


        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Название"
            }),
            'score': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оценка'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше мнение о фильме'
            }),
        }

class RegisterUserForm(UserCreationForm):
    username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-input'}))
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-input'}))
    password2 = CharField(label='Повтор пароля', widget=PasswordInput(attrs={'class': 'form-input'}))
    email = EmailField(label='Email', widget=EmailInput(attrs={'class': 'form-input'}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'captcha')
        widgets = {
            'username': TextInput(attrs={'class': 'form-input'}),
            'password1': PasswordInput(attrs={'class': 'form-input'}),
            'password2': PasswordInput(attrs={'class': 'form-input'}),
        }

class LoginUserForm(AuthenticationForm):
    username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-input'}))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-input'}))



# f = MovieForm(initial={'name': 'instance'}, auto_id=False)

        # def __init__(self, my_arg1, *args, **kwargs):
        #     super(MovieForm, self).__init__(*args, **kwargs)
        #     self.fields['film_name'].queryset = Movie.objects.filter(film_name=my_arg1)