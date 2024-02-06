from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuoteForm, AuthorForm
from .models import Author, Quote


def main(request):
    quotes = Quote.objects.all()
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


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotes/author_detail.html', {"author": author})


