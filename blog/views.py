from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Article

# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    model = Article
    context_object_name = 'articles'

class ArticleView(DetailView):
    template_name = 'article.html'
    model = Article
    context_object_name = 'article'
