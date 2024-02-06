from .models import Author, Quote
from django.forms import ModelForm, CharField, TextInput, DateInput, DateField, Textarea


class AuthorForm(ModelForm):
    first_name = CharField(min_length=3, max_length=255, required=True, widget=TextInput())
    last_name = CharField(min_length=3, max_length=255, required=True, widget=TextInput())
    birth_date = DateField(widget=DateInput(attrs={
        'class': 'form-control',
        'type': 'date'
    }
    ))
    biography = CharField(min_length=50, max_length=500, widget=Textarea())

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'birth_date', 'biography']


class QuoteForm(ModelForm):
    quote = CharField(min_length=3, max_length=50, required=True, widget=Textarea())

    class Meta:
        model = Quote
        fields = ['text', 'author']



