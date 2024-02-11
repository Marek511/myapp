from .models import Author, Quote, Tag, ScrapData
from django.forms import ModelForm, CharField, ModelChoiceField, TextInput, DateInput, DateField, Textarea


class AuthorForm(ModelForm):
    first_name = CharField(min_length=3, max_length=255, required=True, widget=TextInput())
    last_name = CharField(min_length=3, max_length=255, required=True, widget=TextInput())
    birth_date = DateField(widget=DateInput(attrs={
        'class': 'form-control',
        'type': 'date'
    }
    ))
    biography = CharField(min_length=30, max_length=500, widget=Textarea())

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'birth_date', 'biography']


class QuoteForm(ModelForm):
    author = ModelChoiceField(queryset=Author.objects.all(), required=True)
    text = CharField(min_length=3, max_length=500, required=True, widget=Textarea())

    class Meta:
        model = Quote
        fields = ['text', 'author']


class TagForm(ModelForm):

    tag = CharField(min_length=3, max_length=20, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['tag']


class ScrapperForm(ModelForm):
    class Meta:
        model = ScrapData
        fields = ['choice', 'dictionary']



