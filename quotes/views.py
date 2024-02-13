from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuoteForm, AuthorForm, TagForm
from .models import Author, Quote, ScrapData
from bs_scraper import find_data
from django.conf import settings


def main(request):
    quotes = Quote.objects.select_related('author').all()
    return render(request, 'quotes/index.html', {"quotes": quotes})


@login_required
def add_quote(request):

    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/add_quote.html', {"authors": authors, 'form': form})

    return render(request, 'quotes/add_quote.html', {"authors": authors, 'form': QuoteForm()})


@login_required
def add_author(request):

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/add_author.html', {'form': form})

    return render(request, 'quotes/add_author.html', {'form': AuthorForm()})


@login_required
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/add_tag.html', {'form': form})

    return render(request, 'quotes/add_tag.html', {'form': TagForm()})


def quote(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'quotes/quote.html', {"quote": quote})


def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotes/author.html', {"author": author})


def scraper(request, option):

    host = settings.HOST
    data = find_data(host, option)

    scrap_data_object = ScrapData(choice=option, dictionary=data)
    scrap_data_object.save()

    return render(request, 'quotes/scraped_data.html', {'scraped_data': data})


