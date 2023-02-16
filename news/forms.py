from .models import Article
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class ArtiForm(ModelForm):
    class Meta:
        model = Article

        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title' : TextInput(attrs={
                'placeholder' : 'Название статьи',
            }),
            'anons' : TextInput(attrs={
                'placeholder' : 'Анонс',
            }),
            'full_text' : Textarea(attrs={
                'placeholder' : 'Текст статьи',
            }),
            'date' : DateTimeInput(attrs={
                'placeholder' : 'Дата 2023-01-14',
            }),
        }
