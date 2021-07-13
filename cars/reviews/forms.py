from .models import Reviews
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ['author', 'score', 'body']

        widgets = {
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Имя"
            }),
            'score': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оценка'
            }),
            'body': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Отзыв'
            })
        }