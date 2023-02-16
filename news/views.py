from django.shortcuts import render, redirect
from .models import Article
from .forms import ArtiForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news(request):
    news = Article.objects.all()

    return render(request, 'news/news.html', {'news' : news})


class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/datails_news.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'news/create.html'
    form_class = ArtiForm


class NewsDeleteView(DeleteView):
    model = Article
    success_url = '/news/'
    template_name = 'news/news_delete.html'


def create(request):
    form = ArtiForm()

    error = ''
    if request.method == 'POST':
        form = ArtiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('news-home')
        else:
            error = 'Форма была не верной'

    data = {
        'form' : form,
        'error' : error,
        }

    return render(request, 'news/create.html', data)